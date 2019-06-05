import requests
import json

# 爬取网站：http://huoche.tuniu.com/station_200_1102

param_date = '2019-05-09'
param_start_station = '鸡西'
param_end_station = '牡丹江'

# 常用地区码：鸡西：1109、北京：200、哈尔滨：1102、牡丹江：1110
r = requests.get(
    'http://huoche.tuniu.com/tn?r=train/trainTicket/getTickets'
    '&primary%5BdepartureDate%5D=' + param_date +
    '&primary%5BdepartureCityCode%5D=200'
    '&primary%5BdepartureCityName%5D=' + param_start_station +
    '&primary%5BarrivalCityCode%5D=1109'
    '&primary%5BarrivalCityName%5D=' + param_end_station +
    '&start=0'
    '&limit=0')

result = r.text

y = json.loads(result)

trainList = y["data"]["list"]

print('火车票数量 %s' % len(trainList))

print('日期：%s 地点：%s - %s' % (param_date, param_start_station, param_end_station))
for train in trainList:
    hour = train["durationStr"]
    startStation = train["departStationName"]
    endStation = train["destStationName"]
    trainNum = train["trainNum"]
    startTime = train["departDepartTime"]
    endTime = train["destArriveTime"]
    print('%s %s,  %s,  %s,  %s,  %s,  %s' % (param_date, startTime, endTime, hour, trainNum, startStation, endStation))
    # print(train["prices"])
