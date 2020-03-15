# 实现多线程获取天气
# -*- coding: utf-8 -*-
import requests, threading

def get_weather(city):
    # 获取网页的信息
    try:
        req = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % city)
        # print(req.text)
    except:
        print('查询失败')

    # 信息格式处理
    dic_city = req.json()
    # print(dic_city)
    # print(type(req.text) )
    # print(type(req.json() ) )

    city_data = dic_city.get('data')
    if city_data:
        city_forecast = city_data['forecast'][0]
        print(
            city_data.get('city'),
            city_forecast.get('date'),
            city_forecast.get('high'),
            city_forecast.get('low'),
            city_forecast.get('type') )
    else:
        print('未获得有效的城市天气信息')


# 主调度
threads = []
cities = ['北京', '上海', '广州', '深圳']

files = range(len(cities) )
for i in files: # 创建线程
    t = threading.Thread(target = get_weather, args = (cities[i], ) )
    threads.append(t)
for i in files:
    threads[i].start()
for i in files:
    threads[i].join()
print('结束')











