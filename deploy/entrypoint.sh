#!/bin/sh

APP=/app
DATA=/data

mkdir -p $DATA/log $DATA/config $DATA/ssl $DATA/res/obj_cover $DATA/res/obj_model

if [ ! -f "$DATA/config/secret.key" ]; then
    echo $(cat /dev/urandom | head -1 | md5sum | head -c 32) > "$DATA/config/secret.key"
fi

if [ ! -f "$DATA/res/obj_cover/default/default.png" ]; then
    cp data/res/obj_cover/default/default.png $DATA/res/obj_cover/default
fi

if [ ! -f "$DATA/res/obj_model/default/default.obj" ]; then
    cp data/res/obj_model/default/default.obj $DATA/res/obj_model/default
fi

SSL="$DATA/ssl"
if [ ! -f "$SSL/server.key" ]; then
    openssl req -x509 -newkey rsa:2048 -keyout "$SSL/server.key" -out "$SSL/server.crt" -days 1000 \
        -subj "/C=CN/ST=Beijing/L=Beijing/O=Beijing OnlineJudge Technology Co., Ltd./OU=Service Infrastructure Department/CN=`hostname`" -nodes
fi

cd $APP/deploy/nginx
ln -sf locations.conf https_locations.conf
if [ -z "$FORCE_HTTPS" ]; then
    ln -sf locations.conf http_locations.conf
else
    ln -sf https_redirect.conf http_locations.conf
fi

if [ ! -z "$LOWER_IP_HEADER" ]; then
    sed -i "s/__IP_HEADER__/\$http_$LOWER_IP_HEADER/g" api_proxy.conf;
else
    sed -i "s/__IP_HEADER__/\$remote_addr/g" api_proxy.conf;
fi

if [ -z "$MAX_WORKER_NUM" ]; then
    export CPU_CORE_NUM=$(grep -c ^processor /proc/cpuinfo)
    if [[ $CPU_CORE_NUM -lt 2 ]]; then
        export MAX_WORKER_NUM=2
    else
        export MAX_WORKER_NUM=$(($CPU_CORE_NUM))
    fi
fi

cd $APP

n=0
while [ $n -lt 5 ]
do
    python manage.py migrate --no-input &&
    python manage.py inituser --username=admin --password=admin --action=create_super_admin &&
    break
    n=$(($n+1))
    echo "Failed to migrate, going to retry..."
    sleep 8
done

addgroup -g 12003 serverGroup
adduser -u 12000 -S -G serverGroup server

exec supervisord -c /app/deploy/supervisord.conf
