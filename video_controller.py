#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pafy, json
# from model.music import *

YOUTUBE_URL = 'https://youtube.com/watch?v='

class VideoController:
	def getVideoInfo(self, uniqueId):
		VIDEO_URL = YOUTUBE_URL + uniqueId
		video = pafy.new(VIDEO_URL)

		from model.music import Music
		rawMusic = Music(video.title, video.videoid, video.length, video.thumb, video.audiostreams[0].url)
	# print(video)
		# def __init__ (self, title, unique_id, duration, date, thumbnail):
	# return json.dumps(video)
	# print(video)
		result = dict({
			"title": rawMusic.title,
			"unique_id": rawMusic.uniqueId,
			"length": rawMusic.length,
			"src": rawMusic.src,
			"cover_image_url": rawMusic.coverImageUrl
		})


	
	# index = db.Column(db.Integer, primary_key=True)
	# title = db.Column(db.TEXT, nullable=False)
	# uniqueId = db.Column('unique_id', db.String(15), nullable=False)
	# length = db.Column(db.Integer, nullable=False)
	# coverImageUrl = db.Column('cover_image_url', db.TEXT, nullable=False)
	# src = db.Column(db.TEXT, nullable=False)

	# print(result)
		print(result)
		return json.dumps(result)

# Title: EPIK HIGH - BORN HATER M/V
# Author: OfficialEpikHigh
# ID: 3s1jaFDrp5M
# Duration: 00:05:36
# Rating: 4.95094516748
# Views: 5271910
# Thumbnail: http://i.ytimg.com/vi/3s1jaFDrp5M/default.jpg
# Keywords: EPIK HIGH, EPIK, HIGH, 에픽하이, TABLO, Mithra, DJ Tukutz (Record Producer), 타블로, 미쓰라, 미쓰라진, 투컷, 투컷츠, 신발장, SHOEBOX, 본헤이터, 본, 헤이터, BORN HATET, BORN, HATER