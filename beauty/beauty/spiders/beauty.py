import scrapy
from scrapy_splash import SplashRequest

class BeautySpider(scrapy.Spider):
    name = "beauty"

    def start_requests(self):
        urls = ["https://www.86bft.com/tupian/173321.html"]
        # urls = ["https://baike.baidu.com/item/%E6%A2%81%E5%B9%B3%E5%8C%BA/19947574"]
        for url in urls:
            # yield scrapy.Request(url=url, callback=self.parse)
            yield SplashRequest(
                    url, self.parse, endpoint='execute',
                    args={'value': 3600})
    
    def parse(self, response):
        fname = response.url.split("/")[-1]
        with open(fname, 'wb') as f:
            f.write(response.body)
        print('Saved file %s.' % fname)