from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from scrapy.cmdline import execute
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def scrapy_genspider(name, domain, template='basic'):
    """
    # 创建爬虫
    # 语法：scrapy genspider [-t template] <name> <domain>
    # Available templates:
    # 四种模板 basic crawl csvfeed xmlfeed
    """
    execute(['scrapy', 'genspider', '-t', template, name, domain])


def execute_spider(name):
    # 你需要将此处的spider_name替换为你自己的爬虫名称
    execute(['scrapy', 'crawl', name, '--nolog', '-o', name+'.json', '-s', "FEED_EXPORT_ENCODING='utf-8'"])


def execute_debug(name):
    # 你需要将此处的spider_name替换为你自己的爬虫名称
    execute(['scrapy', 'crawl', name, '-o', name+'.json', '-s', "FEED_EXPORT_ENCODING='utf-8'"])


def crawle(name):
    process = CrawlerProcess(get_project_settings())
    process.crawl(name)  # 你需要将此处的spider_name替换为你自己的爬虫名称
    process.start()


def scrapy_fetch(url):
    execute(['scrapy', 'fetch', '--nolog', '--headers', url])


if __name__ == '__main__':
    # scrapy_fetch('http://www.ituring.com.cn/book')
    # execute_debug('ituringSpider')
    execute(['scrapy', 'crawl', 'ituringSpider'])
    # execute_spider('ituringSpider')
    # execut('sina')
    # scrapy_fetch("http://www.ituring.com.cn/book")
    # scrapy_genspider("ituringSpider", "http://www.ituring.com.cn/book", "basic")

