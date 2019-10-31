# -*- coding: utf-8 -*-
import time
import scrapy
from football.items import FootballItem
from football.items import ResultItem
from football.tools import tools
from pymongo import MongoClient
host = "127.0.0.1"
port = 27017

client = MongoClient(host, port)
db = client['jc']


class ResultCrawler(scrapy.Spider):
    """docstring for JingcaiCrawler"""
    name = 'allmatch'
    allowed_domains = ['info.sporttery.cn']
    start_urls = ['http://info.sporttery.cn/football/match_result.php?search_league=0&start_date=2017-03-20&end_date=2018-03-20&dan=&page=%s' %
                  x for x in range(0, 386)]
    tool = tools.Tools()

    def parse(self, response):
        div = response.xpath("//div[@class='match_list']")
        for sel in div.xpath(".//tr"):
            item = ResultItem()
            td = sel.xpath("./td")
            if len(td) < 2:
                continue
            item['match_id'] = td[1].xpath("./text()").extract_first()
            item['time'] = td[0].xpath("./text()").extract_first()
            team = td[3].xpath("./a/span")
            item['home_name'] = team[0].xpath("./@title").extract_first()
            item['away_name'] = team[2].xpath("./@title").extract_first()
            item['score'] = td[5].xpath("./span/text()").extract_first()
            item['h_odds'] = td[6].xpath("./span/text()").extract_first()
            item['a_odds'] = td[7].xpath("./span/text()").extract_first()
            item['d_odds'] = td[8].xpath("./span/text()").extract_first()
            item['result'] = self.tool.getResultByScore(item['score'])
            record = item
            matchId = time.strftime("%Y%m%d", time.strptime(
                item['time'], "%Y-%m-%d")) + item['match_id'][-3:]
            record['_id'] = matchId
            db.all_match.insert(item)
            yield item
