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

#    def start_requests(self):

#        for url in self.start_urls:
#            yield Request(url=url, headers=self.default_headers, callback=self.parse)


    def parse(self, response):
        for tr in response.css('tr.alltrObj'):
            item = OkoooItem()
            #item['matchId'] = tr.css('::attr(matchid)').extract_first()
            td1 = tr.css('td.td1')
            index = td1.css('i::text').extract_first()
            item['matchTitle'] = td1.css('a.ls::text').extract_first()
            td2 = tr.css('td.td2')
            item['matchtime'] = td2.css('span.BuyTime::attr(endtime)').extract_first()
            td3 = tr.css('td.td3')
            host = td3.css('a.sbg')
            draw = td3.css('a.pbg')
            guest = td3.css('a.fbg')
            item['host'] = host.css('span.homenameobj::attr(title)').extract_first()
            leageInfo = host.css('p.float_left i::text').extract()
            if leageInfo.len <= 1:
                item['hostLeage'] = item['matchTitle']
                item['hostLeageRank'] = leageInfo[0]
            else:
                item['hostLeage'] = leageInfo[0]
                item['hostLeageRank'] = leageInfo[1]
            item['hostRangfen'] = host.css('span.handicapobj::text').extract_first()
            item['hostSP'] = host.css('em.pltxt::text').extract_first()
            item['drawSP'] = draw.css('em::text').extract_first()
            item['guest'] = guest.css('span.awaynameobj::text').extract_first()
            item['guestSP'] = guest.css('em.pltxt::text').extract_first()
            guestInfo = guest.css('p.float_right i::text').extract()
            if guestInfo.len <= 1:
                item['guestLeage'] = item['matchTitle']
                item['guestLeageRank'] = guestInfo[0]
            else:
                item['guestLeage'] = guestInfo[0]
                item['guestLeageRank'] = guestInfo[1]
            td8 = tr.css('td.td8')
            link = tr.css('td.td8 a::attr(href)').extract()
            tem['oddsLink'] = link[0] 
            tem['historyLink'] = link[1] 
            td9 = tr.css('td.td9')
            item['winOdds'] = td9.css('span.noborder0::text').extract_first()
            item['drawOdds'] = td9.css('span.noborder1::text').extract_first()
            item['loseOdds'] = td9.css('span.noborder2::text').extract_first()
            yield item

