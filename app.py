#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, session, jsonify
from flask.ext.sqlalchemy import SQLAlchemy
import parser
from video_controller import VideoController

app = Flask(__name__, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://orpheus:orpheus@localhost/orpheus'
app.config.update(
	dict (
    	DEBUG=True,
    	SECRET_KEY='development key'
	)
)

# DB 초기화 시작
db = SQLAlchemy(app)

from model.music import *
from model.user import *
from model.playlist import *
import video_controller

db.create_all()
db.session.commit()
# DB 초기화 끝

videoController = VideoController()

@app.route('/')
def main():
	return render_template('main.html')

@app.route('/load')
def parseTest():
	page = request.args.get('page')
	query = request.args.get('query')

	# if page is 0 or page == '':
	p = parser.parse(query, 0)
	print(jsonify(p))
	# else:
		# p = parser.parsing(page)
	# print(p.keys())
	# sample = ''
	# a = 1
	# for data in p:
	#   if a % 2:
	#   	sample += '<br/>'
	#   sample += '<img src=' + data + ' width=200 height=200/>'
	#   a += 1
	# print(p)
	return jsonify(p)
# , {'Content-Type': 'application/json; charset=utf-8'}
	# return render_template('search.html', keys=p.keys(), data=p)

@app.route('/play')
def playMusic():
	return render_template('playlist.html')

@app.route('/video/<uniqueId>')
def getVideo(uniqueId):
	# uniqueId = request.args.get('uniqueId')
	# return uniqueId
	return videoController.getVideoInfo(uniqueId)

if __name__ == '__main__':
	app.run()