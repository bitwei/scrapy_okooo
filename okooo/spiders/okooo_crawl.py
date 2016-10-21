import scrapy
from scrapy import Request
from okooo.items import OkoooItem

class QuotesSpider(scrapy.Spider):
    name = "okooo"
    start_urls = [
        'http://www.okooo.com/danchang/',
    ]

    default_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch, br',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': 'www.douban.com',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    }

    def start_requests(self):

        for url in self.start_urls:
            yield Request(url=url, headers=self.default_headers, callback=self.parse)


    def parse(self, response):
        for tr in response.css('tr.alltrObj'):
            item = OkoooItem()
            print tr.css('::attr(id)').extract_first()
            item['matchId'] = tr.css('::attr(matchid)').extract_first()
            item['matchTitle'] = tr.css('a.ls::attr(title)').extract_first()
            matchtime = tr.css('td.td2::attr(title)').extract_first()
            item['matchtime'] = matchtime.encode('utf-8')

#            sbg = tr.css('a.sbg').extract_first()
            host = tr.css('span.homenameobj::attr(title)').extract_first()
            item['host'] = host.encode('utf-8')

#            item['hostRangfen'] = site.css('').extract_first()
#            item['hostOdds'] = site.css('').extract_first()
#            item['hostLeage'] = site.css('').extract_first()
#            item['hostLeageRank'] = site.css('').extract_first()
#            item['guest'] = site.css('').extract_first()
#            item['guestOdds'] = site.css('').extract_first()
#            item['guestLeage'] = site.css('').extract_first()
#            item['guestLeageRank'] = site.css('').extract_first()
#            item['winOdds'] = site.css('').extract_first()
#            item['drawOdds'] = site.css('').extract_first()
#            item['loseOdds'] = site.css('').extract_first()
            yield item

