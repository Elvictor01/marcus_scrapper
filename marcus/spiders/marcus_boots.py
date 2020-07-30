import scrapy
from ..items import MarcusItem


class MarcusShoeSpider(scrapy.Spider):
    name = 'marcus_boots'

    page_number = 2
    start_urls = [
        'https://www.neimanmarcus.com/c/mens-shoes-boots-cat6750735?navpath=cat000000_cat000470_cat000550_cat6750735&source=leftNav'
    ]

    def parse(self, response):
        items = MarcusItem()

        shoeType = response.css(
            '.active').css('::text').extract()
        shoeName = response.css(
            '.name').css('::text').extract()
        price = response.css(
            '.product-thumbnail__sale-price').css('::text').extract()
        shoeBrand = response.css(
            '.designer').css('::text').extract()
        #       salePrice = response.css(
        #            '.currentPrice .price').css('::text').extract()

        items['shoeType'] = shoeType
        items['shoeBrand'] = shoeBrand
        items['shoeName'] = shoeName
        items['price'] = price
        #        items['salePrice'] = salePrice

        yield items

        next_page = 'https://www.neimanmarcus.com/c/mens-shoes-boots-cat6750735?navpath=cat000000_cat000470_cat000550_cat6750735&page=' + \
            str(MarcusShoeSpider.page_number) + '&source=leftNav'
        if MarcusShoeSpider.page_number <= 2:
            yield response.follow(next_page, callback=self.parse)
