#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import db

class User(db.Model):
	__tablename__ = 'user'

	index = db.Column(db.Integer, primary_key=True)
	password = db.Column(db.String(255), nullable=False)
	playlist = db.Column(db.TEXT, nullable=False)

	def __init__ (self):
		pass