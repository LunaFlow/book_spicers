# book_spicers
图灵社区图书信息爬取

![1563771924771](D:\800-vsCode-work\820Python\book_spicers\assets\1563771924771.png)

* 支持版本:  ![](https://img.shields.io/badge/Python-3.x-blue.svg)

### 下载安装

* 下载源码:

```shell
git clone git@github.com:jhao104/proxy_pool.git

或者直接到https://github.com/jhao104/proxy_pool 下载zip文件
```

* 安装依赖:

```shell
pip install -r requirements.txt
```

* 配置ituring/ituring/setting.py:

```shell
# 修改scrapy 的 setting.py 配置文件
# 主要修改 redis 和 mysql 的配置

# redis 配置
REDIS_HOST = 'localhost'  # 配置Redis的安装地址
REDIS_PORT = 6379        # Redis的连接端口
REDIS_DUP_DB = 0 		  # Redis去重过滤器的数据库

# mysql 配置
MYSQL_HOST = 'localhost'                # 配置Redis的安装地址
MYSQL_PORT = 3306                       # Mysql的连接端口
MYSQL_USER = 'root'                     # Mysql的用户
MYSQL_PASSWORD = 'password'       		# Mysql的密码
MYSQL_DB = 'mmall' 		                # Mysql的数据库
```



### 启动与使用

运行 ituring/main.py 

或者在命令行运行 scrapy crawl ituringSpider