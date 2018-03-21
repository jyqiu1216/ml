# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FootballItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    league_id = scrapy.Field()
    league_name = scrapy.Field()
    rank = scrapy.Field()
    team = scrapy.Field()
    total_match = scrapy.Field()
    total_win = scrapy.Field()
    total_tie = scrapy.Field()
    total_lose = scrapy.Field()
    total_goal = scrapy.Field()
    total_fumble = scrapy.Field()
    total_GD = scrapy.Field()
    home_match = scrapy.Field()
    home_win = scrapy.Field()
    home_tie = scrapy.Field()
    home_lose = scrapy.Field()
    home_goal = scrapy.Field()
    home_fumble = scrapy.Field()
    away_match = scrapy.Field()
    away_win = scrapy.Field()
    away_tie = scrapy.Field()
    away_lose = scrapy.Field()
    away_goal = scrapy.Field()
    away_fumble = scrapy.Field()
    score = scrapy.Field()


class ResultItem(scrapy.Item):
    _id = scrapy.Field()
    home_name = scrapy.Field()
    away_name = scrapy.Field()
    time = scrapy.Field()
    match_id = scrapy.Field()
    result = scrapy.Field()
    score = scrapy.Field()
    odds = scrapy.Field()
    a_odds = scrapy.Field()
    h_odds = scrapy.Field()
    d_odds = scrapy.Field()
