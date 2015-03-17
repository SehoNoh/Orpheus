#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pafy
import requests
from flask import session
from bs4 import BeautifulSoup

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}

def parsing(page):
	s = requests.Session()
	r = s.get('https://youtube.com/results?search_query=Epik+High?page='+page, headers=headers)
	cookies = requests.utils.dict_from_cookiejar(s.cookies)
	# print(cookies['YSC'])
	# print(cookies['PREF'])
	# print(cookies['VISITOR_INFO1_LIVE'])

	session['YSC'] = cookies['YSC']
	session['PREF'] = cookies['PREF']
	session['VISITOR_INFO1_LIVE'] = cookies['VISITOR_INFO1_LIVE']

	# {'YSC': 'G0cfNqwweIs', 'PREF': 'f1=50000000', 'VISITOR_INFO1_LIVE': '_ifQmz45RQw'}
	soup = BeautifulSoup(r.text)

	divList = []

# Youtube 고유 ID를 가진 div 태그를 가져옴
	for div in soup.find_all('div'):
		if div.get('data-context-item-id') is not None:
			divList.append(div.get('data-context-item-id'))

	aList = []

# 썸네일 이미지와 비디오 이름을 가진 a 태그를 가져옴
	for a in soup.find_all('a'):
		for data in divList:
			if a.get('href') == ('/watch?v=' + data):
				aList.append(a)

	data = dict()
	imgList = []
	textList = []

	for a in aList:
		img = ''

		if a.img is not None:
			if 'data-thumb' in a.img.attrs:
				img = a.img['data-thumb']
			elif 'src' in a.img.attrs:
				img = a.img['src']
	
			imgList.append(img)
		
		else:
			textList.append(a.text)

	for count in range(len(divList)):
		videoId = divList[count]
		imgSrc = imgList[count]
		text = textList[count]

		data[videoId] = {'title': text, 'imgSrc': imgSrc}

	# video = pafy.new('https://youtube.com/watch?v=' + data[0])

	# print(aList)
	# print(data)

	return data