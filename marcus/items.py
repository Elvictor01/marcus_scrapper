# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MarcusItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    shoeType = scrapy.Field()
    shoeBrand = scrapy.Field()
    shoeName = scrapy.Field()
    price = scrapy.Field()
    #salePrice = scrapy.Field()

    pass
