# coding: utf-8
from redis import Redis
from scrapy.utils.request import request_fingerprint
from scrapy.dupefilters import BaseDupeFilter
import logging


"""
基于Redis的去重过滤器
"""


class RedisDupeFilter(BaseDupeFilter):
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = Redis(host=host, port=port, db=db)
        self.logger = logging.getLogger(__name__)

    @classmethod
    def from_settings(cls, settings):
        """
        读取配置信息
        """
        host = settings.get('REDIS_HOST', 'localhost')
        redis_port = settings.getint('REDIS_PORT')
        redis_db = settings.get('REDIS_DUP_DB')
        return cls(host, redis_port, redis_db)

    def request_seen(self, request):
        fp = self.request_fingerprint(request)
        key = 'UrlFingerprints'
        if not self.redis.sismember(key, fp):
            self.redis.sadd(key, fp)
            return False
        return True

    def request_fingerprint(self, request):
        """
        用Hash生成URL指纹
        :param request:
        :return:
        """
        return request_fingerprint(request)

    def log(self, request, spider):
        msg = ("已过滤的重复请求: %(request)s")
        self.logger.debug(msg, {'request': request}, extra={'spider': spider})
        spider.crawler.stats.inc_value('dupefilter/filtered', spider=spider)
