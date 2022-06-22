# 软件工程大作业后端

[![Python](https://img.shields.io/badge/python-3.8.10-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3810/)
[![Django](https://img.shields.io/badge/django-4.0.4-blue.svg?style=flat-square)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/django_rest_framework-3.13.1-blue.svg?style=flat-square)](http://www.django-rest-framework.org/)



## 环境搭建

   在项目目录下执行以下命令来安装python库

```shell
pip install -r ./deploy/requirements.txt
```



## 项目文件说明

1. 目录结构说明

| 文件夹       | 说明       |
|-----------|----------|
| seBackEnd | 项目配置相关   |
| account   | 用户模块相关   |
| history   | 历史记录模块相关 |
| objModel  | 3d模型相关   |
| utils     | 通用代码文件   |
| data      | 运行数据文件夹  |
| deploy    | 部署相关     |

2. 模块文件夹说明

| 文件(夹)          | 说明                |
|----------------|-------------------|
| migrations     | 数据库迁移文件记录         |
| admin.py       | Django admin 站点配置 |
| apps.py        | 子应用配置             |
| decorators.py  | 装饰器相关             |
| middleware.py  | 中间件相关             |
| models.py      | 数据库模型相关           |
| serializers.py | 序列化和反序列化相关        |
| urls.py        | 接口url相关           |
| views.py       | 视图相关              |

   

## 数据库设置

   本项目默认使用`sqlite`作为系统数据库，如果需要使用其他数据库，请先修改`seBackEnd/settings.py`文件的数据库配置(第78-83行)。默认为如下：

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': str(BASE_DIR / 'db.sqlite3'),
    }
}
```

   例如想要修改为`postgresql`，则可以改为如下内容：

```python
 DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'HOST': 'YOUR_HOST',  # 修改为数据库地址
         'PORT': "YOUR_PORT",  # 修改为数据库端口
         'NAME': "DB_NAME",    # 修改为数据库名称
         'USER': "DB_USER",    # 修改为数据库登录用户名
         'PASSWORD': 'DB_PWD'  # 修改为数据库登录密码
     }
 }
```

   **注意：** 使用其他数据库时，请先建立好相关数据库和用户。可以没有数据表但要确保可以登录指定的数据库。



## 使用方法

1. 若使用默认数据库，请先在项目文件(与`manage.py`同级)下创建 db.sqlite3 文件

2. 设置环境变量
   - APP_ID : 小程序的app_id
   - APP_SECRET : 小程序的app_secret

3. 执行迁移命令
```shell
python manage.py makemigrations
python manage.py migrate
```

5. 创建管理员(可选)
```shell
python manage.py createsuperuser
```

6. 运行
```shell
python manage.py runserver 0.0.0.0:8000
```



## 管理站点

   若在在上一节的第5步创建了管理员，那么就可以访问管理站点，网址为`127.0.0.1:8000/admin`

