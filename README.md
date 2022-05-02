# 软件工程大作业后端

[![Python](https://img.shields.io/badge/python-3.8.10-blue.svg?style=flat-square)](https://www.python.org/downloads/release/python-3810/)
[![Django](https://img.shields.io/badge/django-4.0.4-blue.svg?style=flat-square)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/django_rest_framework-3.13.1-blue.svg?style=flat-square)](http://www.django-rest-framework.org/)

## 使用方法

1. 在项目文件下创建 db.sqlite3 文件

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
python manage.py runserver
```
