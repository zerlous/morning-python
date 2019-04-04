#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : zerlous
# @File : crawler.py
# @Time : 2019-04-04 12:46
# @Desc : 豆瓣Top250 数据爬虫

import requests
import json
from bs4 import BeautifulSoup as bs


def main():
    url = 'https://movie.douban.com/top250'
    result = []
    for start in range(0, 250, 25):
        res = requests.get(url, {'start': start}, )
        soup = bs(res.text, 'lxml')
        lis = soup.find('ol').find_all('li')
        for index in range(0, len(lis)):
            li = lis[index]
            one = {
                'number': li.find('em').text,
                'img_url': li.find('img').attrs['src'],
                'movie_name': li.find('div', {'class': 'hd'}).find('a').get_text(),
                'movie_info': li.find('div', {'class': 'bd'}).find('p', {'class': ''}).get_text(),
                'movie_rating': li.find('span', {'class': 'rating_num'}).text,
                'movie_quote': '无' if li.find('span', {'class': 'inq'}) == None else li.find('span',
                                                                                             {'class': 'inq'}).text
            }
            result.append(one)
    with open('001-spider-json.json', 'w') as f:
        json.dump({'top250': result}, f)
        print('------write finished------')


if __name__ == '__main__':
    main()
