# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader.processors import TakeFirst, MapCompose, Compose, Identity, Join
from w3lib.html import remove_tags
from datetime import datetime
from .util.processors import Number, Date, Price, Text, CleanText


class IturingBookItem(Item):
    # 书名
    name = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
    # 作者
    authors = Field(input_processor=MapCompose(lambda v: v.replace('(作者)', '').replace(' ', '').strip(), stop_on_none=True), output_processor=TakeFirst())
    # 原名
    origin_name = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('原书名', '').strip(), stop_on_none=True), output_processor=TakeFirst())
    # 译者
    translators = Field(input_processor=MapCompose(lambda v: v.replace('(译者)', '').strip(), stop_on_none=True), output_processor=TakeFirst())
    # 出版时间 ***时间类型
    # lambda time_str: datetime.strptime(time_str, '%Y-%m-%d')
    pub_date = Field(input_processor=MapCompose(remove_tags,
                                                lambda v: datetime.strptime(v.replace('出版日期', '').strip(), '%Y-%m-%d'), stop_on_none=True), output_processor=TakeFirst())
    # 页数 ***数字类型
    pages = Field(input_processor=MapCompose(remove_tags,
                                             lambda v: int(v.replace('页　　数', '').strip()), stop_on_none=True), output_processor=TakeFirst())
    # 纸质定价 ***价格类型
    book_price = Field(input_processor=MapCompose(remove_tags,
                                                  lambda v: float(v.replace('定　　价', '').replace('元', '').strip()),
                                                  stop_on_none=True), output_processor=TakeFirst())
    # 纸质在售定价 ***价格类型
    p_book_price = Field(input_processor=MapCompose(lambda v: float(v.replace('￥', '').strip()), stop_on_none=True),
                         output_processor=TakeFirst())
    # 电子书在售定价 ***价格类型
    e_book_price = Field(input_processor=MapCompose(lambda v: float(v.replace('￥', '').strip()), stop_on_none=True),
                         output_processor=TakeFirst())
    # ISBN
    isbn = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('书　　号', '').strip(), stop_on_none=True),
                 output_processor=TakeFirst())
    # 简介
    summary = Field(input_processor=MapCompose(remove_tags, str.strip, stop_on_none=True), output_processor=TakeFirst())
    # 作者简介
    about_authors = Field(input_processor=MapCompose(remove_tags, str.strip, stop_on_none=True), output_processor=TakeFirst())
    # 推荐数 ***数字类型
    recommend = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
    # 阅读人数 ***数字类型
    reading = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
    # 出版状态
    pub_status = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())




# class IturingBookItem(Item):
#     # 书名
#     name = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
#     # 作者
#     authors = Field(input_processor=MapCompose(lambda v: v.replace('(作者)', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 原名
#     origin_name = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('原书名', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 译者
#     translators = Field(input_processor=MapCompose(lambda v: v.replace('(译者)', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 出版时间 ***时间类型
#     pub_date = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('出版日期', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 页数 ***数字类型
#     pages = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('页　　数', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 纸质定价 ***价格类型
#     book_price = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('定　　价', '').replace('元', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 纸质在售定价 ***价格类型
#     p_book_price = Field(input_processor=MapCompose(lambda v: v.replace('￥', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 电子书在售定价 ***价格类型
#     e_book_price = Field(input_processor=MapCompose(lambda v: v.replace('￥', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # ISBN
#     isbn = Field(input_processor=MapCompose(remove_tags, lambda v: v.replace('书　　号', '').strip(), stop_on_none=True), output_processor=TakeFirst())
#     # 简介
#     summary = Field(input_processor=MapCompose(remove_tags, str.strip, stop_on_none=True), output_processor=TakeFirst())
#     # 作者简介
#     about_authors = Field(input_processor=MapCompose(remove_tags, str.strip, stop_on_none=True), output_processor=TakeFirst())
#     # 推荐数 ***数字类型
#     recommend = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
#     # 阅读人数 ***数字类型
#     reading = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())
#     # 出版状态
#     pub_status = Field(input_processor=MapCompose(str.strip, stop_on_none=True), output_processor=TakeFirst())


# class IturingBookItemSimple(Item):
#     # 书名
#     name = Field()
#     # 作者
#     authors = Field()
#     # 原名
#     origin_name = Field()
#     # 译者
#     translators = Field()
#     # 出版时间
#     pub_date = Field()
#     # 页数
#     pages = Field()
#     # 纸质定价
#     book_price = Field()
#     # 纸质在售定价
#     p_book_price = Field()
#     # 电子书在售定价
#     e_book_price = Field()
#     # ISBN
#     isbn = Field()
#     # 简介
#     summary = Field()
#     # 作者简介
#     about_authors = Field()

class IturingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
