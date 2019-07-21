from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, Text, DateTime
from sqlalchemy.dialects.mysql import LONGTEXT
# 创建对象的基类：
db = declarative_base()


class Book(db):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    # 书名
    name = Column(String(255))
    # 作者
    authors = Column(Text)
    # 原名
    origin_name = Column(String(255))
    # 翻译者
    translators = Column(String(255))
    # 出版日期
    pub_date = Column(DateTime)
    # 页数
    pages = Column(Integer)
    # 书定价
    book_price = Column(Float)
    # 纸质书价格
    p_book_price = Column(Float)
    # 电子书价格
    e_book_price = Column(Float)
    # 编号
    isbn = Column(String(255))
    # 简介
    summary = Column(Text)
    # 作者简介
    about_authors = Column(LONGTEXT)
    # 推荐数 ***数字类型
    recommend = Column(String(255))
    # 阅读人数 ***数字类型
    reading = Column(String(255))
    # 出版状态
    pub_status = Column(String(255))
    #
    # name = Column(String(255))
    #
    # authors = Column(String(255))
    #
    # publishing_house = Column(String(255))
    # # 出品方
    # publisher = Column(String(255))
    # # 原名
    # origin_name = Column(String(255))
    # # 译者
    # translators = Column(String(255))
    # # 出版时间
    # pub_date = Column(DateTime())
    # # 页数
    # pages = Column(Integer())
    # # 定价
    # price = Column(Float())
    # # ISBN
    # isbn = Column(String(255))
    # # 豆瓣评分
    # rates = Column(Float())
    # # 评价数
    # rating_count = Column(Integer())
    # summary = Column(Text)
    # # 作者简介
    # about_authors = Column(Text)
    # 书名

