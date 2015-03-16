#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, render_template, request, session
from parse import parsing

app = Flask(__name__, static_url_path='')
app.config.update(dict(
    DEBUG=True,
    SECRET_KEY='development key'
	)
)

@app.route('/')
def main():
	return render_template('search.html')

@app.route('/load')
def parseTest():
	# return jsonify({'Hello':'World'})

	page = request.args.get('page')
	p = parsing(request, page)
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

if __name__ == '__main__':
	app.run()