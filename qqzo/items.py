# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QqzoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id1 = scrapy.Field()
    type = scrapy.Field()
    create_time = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    desp = scrapy.Field()
    platform = scrapy.Field()
    user_agent = scrapy.Field()
    origin_img_list = scrapy.Field()
    album_info = scrapy.Field()
    photo_list = scrapy.Field()
    img_list = scrapy.Field()
    share_info = scrapy.Field()
    shuoshuo_info =  scrapy.Field()



