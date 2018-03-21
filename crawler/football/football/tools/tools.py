# -*- coding: utf-8 -*-


class Tools(object):
    def getResultByScore(self, score):
        homeScore = int(score.split(':')[0])
        awayScore = int(score.split(':')[1])
        if homeScore > awayScore:
            return 3
        elif homeScore == awayScore:
            return 1
        else:
            return 0


if __name__ == "__main__":
    tools = Tools()
    result = tools.getResultByScore('2:1')
    print(result)
