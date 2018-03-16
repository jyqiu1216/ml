# -*- coding: utf-8 -*-

import scrapy
from football.items import FootballItem

class JingcaiCrawler(scrapy.Spider):
	"""docstring for JingcaiCrawler"""
	name = 'jingcai'
	allowed_domains = ['info.sporttery.cn']
	start_urls = ['http://info.sporttery.cn/football/history/history_data.php?mid=%s' %x for x in range(0, 1250)]

	def parse(self, response):
		league = response.xpath("//div[@class='event season']")
		league_name = league.xpath("./h2/text()").extract_first()
		for sel in response.xpath("//div[@class='integral']//tr"):
			item = FootballItem()
			td = sel.xpath("./td")
			if len(td) < 2:
				continue;
			item['league_id'] = response.url.split("mid=")[1];
			item['league_name'] = league_name
			item['rank'] = td[0].xpath("./text()").extract_first()
			item['team'] = td[1].xpath("./a/text()").extract_first()
			item['total_match'] = td[2].xpath("./text()").extract_first()
			item['total_win'] = td[3].xpath("./text()").extract_first()
			item['total_tie'] = td[4].xpath("./text()").extract_first()
			item['total_lose'] = td[5].xpath("./text()").extract_first()
			item['total_goal'] = td[6].xpath("./text()").extract_first()
			item['total_fumble'] = td[7].xpath("./text()").extract_first()
			item['total_GD'] = td[8].xpath("./text()").extract_first()
			item['home_match'] = td[9].xpath("./text()").extract_first()
			item['home_win'] = td[10].xpath("./text()").extract_first()
			item['home_tie'] = td[11].xpath("./text()").extract_first()
			item['home_lose'] = td[12].xpath("./text()").extract_first()
			item['home_goal'] = td[13].xpath("./text()").extract_first()
			item['home_fumble'] = td[14].xpath("./text()").extract_first()
			item['away_match'] = td[15].xpath("./text()").extract_first()
			item['away_win'] = td[16].xpath("./text()").extract_first()
			item['away_tie'] = td[17].xpath("./text()").extract_first()
			item['away_lose'] = td[18].xpath("./text()").extract_first()
			item['away_goal'] = td[19].xpath("./text()").extract_first()
			item['away_fumble'] = td[20].xpath("./text()").extract_first()
			item['score'] = td[21].xpath("./text()").extract_first()

			yield item
