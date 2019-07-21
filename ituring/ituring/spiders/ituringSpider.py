# -*- coding: utf-8 -*-
import scrapy
from ..items import IturingBookItem
# from ..items import IturingBookItemSimple
from scrapy.loader import ItemLoader
from pyquery import PyQuery as pq
from urllib.parse import urljoin as urljoin
from scrapy.http import Request
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader


class IturingspiderSpider(CrawlSpider):
    name = 'ituringSpider'
    # allowed_domains = ['www.ituring.com.cn/book']
    start_urls = ['http://www.ituring.com.cn/book']
    rules = (
        Rule(LinkExtractor(allow=('\/book\?tab=book.*?page=\d+'), deny=('#'), restrict_xpaths=('//li[@class="PagedList-skipToNext"]/a[contains(., "下一页")]')), follow=True),
        Rule(LinkExtractor(allow=('\/book\/\d+') ), follow=False, callback='parse_item'),
    )

    # def parse_start_url(self, response):
    #     print(response.text)
    #     return []

    # def parse(self, response):
    #     print(response.request.headers["User-Agent"])
    #     for sel in response.xpath('//div[@id="productsAzLeft"]'):
    #         base_url = 'http://www.ikea.com/'
    #         follow_url = sel.xpath('//span[@class="productsAzLink"]/@href').extract()
    #         complete_url = urljoin(base_url, follow_url)
    #         request = Request(complete_url, callback=self.parse_item)
    #         yield request

    def parse_item(self, response):
        loader = ItemLoader(item=IturingBookItem(), response=response)
        loader.add_css('name', 'div.book-title > h2::text')
        # 作者
        loader.add_css('authors', 'div.book-author > span:nth-child(1)::text')
        # 原名
        loader.add_css('origin_name', 'ul.publish-info > li:nth-last-child(2)::text')
        # 译者
        loader.add_css('translators', 'div.book-author > span:nth-child(2)::text')
        # 出版时间
        loader.add_xpath('pub_date', '//ul[@class="publish-info"]/li[contains(., "出版日期")]/text()')
        # 页数
        loader.add_xpath('pages', '//ul[@class="publish-info"]/li[contains(., "页　　数")]/text()')
        # 纸质定价
        loader.add_xpath('book_price', '//ul[@class="publish-info"]/li[contains(., "定　　价")]/text()')
        # 纸质在售定价
        # loader.add_css('p_book_price', 'div.book-approaches > dl:nth-child(5) > dd > span.price::text')
        loader.add_xpath('p_book_price',
                         '//div[@class="book-approaches"]/dl[contains(., "纸质书")]/dd/span[@class="price"]/text()')
        # 电子书在售定价
        # loader.add_css('e_book_price', 'div.book-approaches > dl:nth-child(1) > dd > span.price::text')
        loader.add_xpath('e_book_price',
                         '//div[@class="book-approaches"]/dl[contains(., "电子书")]/dd/span[@class="price"]/text()')
        # ISBN
        loader.add_xpath('isbn', '//ul[@class="publish-info"]/li[contains(., "书　　号")]/text()')
        # 简介
        loader.add_css('summary', 'div.book-head-upper > div.book-intro.readmore::text')
        # 作者简介
        loader.add_css('about_authors', 'div.block-body > div.intro::text')
        # 推荐数
        loader.add_css('recommend', '#toggle-vote > span.number::text')
        # 阅读人数
        loader.add_css('reading', '#book-fav-vote > div > span.number::text')
        # 出版状态
        loader.add_xpath('pub_status', '//ul[@class="publish-info"]/li[contains(., "出版状态")]/text()')
        return loader.load_item()

        # doc = pq(response.body)
        # item = IturingBookItemSimple()
        # # 书名
        # item['name'] = doc('div.book-title > h2').text()
        # # 作者
        # item['authors'] = doc('div.book-author > span:nth-child(1)').text()
        # # 原名
        # item['origin_name'] = doc('ul.publish-info > li:nth-child(11)').text()
        # # 译者
        # item['translators'] = doc('div.book-author > span:nth-child(2) > a').text()
        # # 出版时间
        # item['pub_date'] = doc('ul.publish-info > li:nth-child(4)').text()
        # # 页数
        # item['pages'] = doc('ul.publish-info > li:nth-child(7)').text()
        # # 纸质定价
        # item['book_price'] = doc('ul.publish-info > li:nth-child(6)').text()
        # # 纸质在售定价
        # item['p_book_price'] = doc('div.book-approaches > dl:nth-child(5) > dd > span.price').text()
        # # 电子书在售定价
        # item['e_book_price'] = doc('div.book-approaches > dl:nth-child(1) > dd > span.price').text()
        # # ISBN
        # item['isbn'] = doc('ul.publish-info > li:nth-child(5)').text()
        # # 简介
        # item['summary'] = doc('div.book-head-upper > div.book-intro.readmore').text()
        # # 作者简介
        # item['about_authors'] = doc('div.block-body > div.intro').text()
        # return item
