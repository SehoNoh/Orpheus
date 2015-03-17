#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pafy, json

YOUTUBE_URL = 'https://youtube.com/watch?v='

class VideoController:

	def getVideoInfo(uniqueId):
		VIDEO_URL = YOUTUBE_URL + uniqueId
		video = pafy.new(VIDEO_URL)
		video = data.Video(video.title, video.videoid, video.duration, video.published, video.thumb)
	# print(video)
		# def __init__ (self, title, unique_id, duration, date, thumbnail):
	# return json.dumps(video)
	# print(video)
		result = dict({
			"title": video.title,
			"unique_id": video.uniqueId,
			"duration": video.duration,
			"date": video.date,
			"thumbnail": video.thumbnail
		})


	# id = db.Column(db.Integer, primary_key=True)
	# title = db.Column(db.String(50))
	# unique_id = db.Column(db.String(10), unique=True)
	# duration = db.Column(db.String(10))
	# date = db.Column(db.String(30))
	# thumbnail = db.Column(db.String(100))

	# print(result)
		return json.dumps(result)

# Title: EPIK HIGH - BORN HATER M/V
# Author: OfficialEpikHigh
# ID: 3s1jaFDrp5M
# Duration: 00:05:36
# Rating: 4.95094516748
# Views: 5271910
# Thumbnail: http://i.ytimg.com/vi/3s1jaFDrp5M/default.jpg
# Keywords: EPIK HIGH, EPIK, HIGH, 에픽하이, TABLO, Mithra, DJ Tukutz (Record Producer), 타블로, 미쓰라, 미쓰라진, 투컷, 투컷츠, 신발장, SHOEBOX, 본헤이터, 본, 헤이터, BORN HATET, BORN, HATER