# -*- coding: utf-8 -*-

import scrapy
from football.items import FootballItem
from football.items import ResultItem


class ResultCrawler(scrapy.Spider):
    """docstring for JingcaiCrawler"""
    name = 'result'
    allowed_domains = ['okooo.com']
    # start_urls = ['http://info.sporttery.cn/football/history/history_data.php?mid=%s' %
    #               x for x in range(0, 100)]
    start_urls = ['http://www.okooo.com/jingcai/kaijiang/']

    def parse(self, response):
        league = response.xpath("//div[@class='event season']")
        league_name = league.xpath("./h2/text()").extract_first()
        for sel in response.xpath("//tr[@align='center']"):
            item = ResultItem()
            td = sel.xpath("./td")
            if len(td) < 2:
                continue
            item['match_id'] = td[0].xpath("./text()").extract_first()
            item['time'] = td[2].xpath("./text()").extract_first()
            item['home_name'] = td[3].xpath("./a/text()").extract_first()
            item['away_name'] = td[4].xpath("./a/text()").extract_first()
            item['result'] = td[7].xpath("./b/text()").extract_first()
            item['score'] = td[6].xpath("./text()").extract_first()
            item['odds'] = td[8].xpath("./text()").extract_first()
            yield item