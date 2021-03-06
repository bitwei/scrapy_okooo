# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class OkoooItem(scrapy.Item):
    matchId = scrapy.Field()
    matchTitle = scrapy.Field()
    matchtime = scrapy.Field()
    host = scrapy.Field()
    hostRangfen = scrapy.Field()
    hostSP = scrapy.Field()
    hostLeage = scrapy.Field()
    hostLeageRank = scrapy.Field()
    drawSP = scrapy.Field()
    guest = scrapy.Field()
    guestSP = scrapy.Field()
    guestLeage = scrapy.Field()
    guestLeageRank = scrapy.Field()
    winOdds = scrapy.Field()
    drawOdds = scrapy.Field()
    loseOdds = scrapy.Field()
