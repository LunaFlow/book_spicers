# -*- coding: utf-8 -*-

# Scrapy settings for ituring project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ituring'

SPIDER_MODULES = ['ituring.spiders']
NEWSPIDER_MODULE = 'ituring.spiders'

# 配置并启用redis去重过滤器 RedisDupeFilter
DUPEFILTER_CLASS = 'ituring.dupefilters.RedisDupeFilter.RedisDupeFilter'


# 输出json文件配置
# FEED_FORMAT = 'json'
# FEED_URI = 'result.json'
# FEED_EXPORT = 'utf-8'

# 日志等级
# LOG_LEVEL = 'WARNING'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# redis 配置
REDIS_HOST = 'localhost'  # 配置Redis的安装地址
REDIS_PORT = 6379        # Redis的连接端口
REDIS_DUP_DB = 0 		  # Redis去重过滤器的数据库

# mysql 配置
MYSQL_HOST = 'localhost'                # 配置Redis的安装地址
MYSQL_PORT = 3306                       # Mysql的连接端口
MYSQL_USER = 'root'                     # Mysql的用户
MYSQL_PASSWORD = '5648.luna.sama'       # Mysql的密码
MYSQL_DB = 'mmall' 		                    # Mysql的数据库

# ORM 配置
ORM_MODULE = 'ituring.modals.book'  # 数据模型所在的模块
ORM_METABASE = 'db' 			    # 数据元定义类
ORM_ENTITY = 'Book'  			    # 数据实体类

FEED_FORMAT = 'entity'      # 数据导出的格式
FEED_EXPORTERS = {          # 关联导出格式与数据项导出器
    'entity': 'ituring.db.extensions.SQLItemExporter'
}

# 数据库的连接字符串
FEED_URI = 'mysql://{user}:{password}@{host}:{port}/{db}?charset=utf8'.format(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOST, port=MYSQL_PORT, db=MYSQL_DB)

# 增加对sqlite，postgresql和mysql内种协议的存储端支持
FEED_STORAGES = {
    # 'sqlite': 'douban.extensions.SQLFeedStorage',
    # 'postgresql': 'douban.extensions.SQLFeedStorage',
    'mysql': 'ituring.db.extensions.SQLFeedStorage'
}

# MongoDBPipeline
MONGODB_SERVER = 'localhost'
MONGODB_PORT = '27017'
MONGODB_DB = "ituring"
MONGODB_COLLECTION = "books"


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# 反爬配置
REFERRER_POLICY = 'no-referrer-when-downgrade'

USER_AGENTS = {
    # 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0',
    # 'Mozilla/5.0 (Windows NT 5.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1',
    # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6',

    'Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)',
    'Mozilla/5.0+(compatible;+bingbot/2.0;++http://www.bing.com/bingbot.htm)',
    'Mozilla/5.0+(compatible;+Googlebot/2.1;++http://www.google.com/bot.html)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
}

# 自动降速(AutoThrottle)
AUTOTHROTTLE_ENABLED = True  # 一定要打开，否则自动降速就会禁用
AUTOTHROTTLE_START_DELAY = 5
AUTOTHROTTLE_MAX_DELAY = 60
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
AUTOTHROTTLE_DEBUG = False

# 禁止cookie
COOKIES_ENABLES = False


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES={
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'ituring.middlewares.RandomUserAgentMiddleware': 800,
    # 'ituring.middlewares.RandomProxyMiddleware': 501,
}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'ituring.pipelines.MongoDBPipeline': 300,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ituring (+http://www.yourdomain.com)'





# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ituring.middlewares.IturingSpiderMiddleware': 543,
#}



# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}



# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
