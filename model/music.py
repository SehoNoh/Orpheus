# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# # from app import db

# # class Video(db.Model):
# # 	__tablename__ = 'video'
	
# # 	id = db.Column(db.Integer, primary_key=True)
# # 	title = db.Column(db.String(50))
# # 	uniqueId = db.Column(db.String(10), unique=True)
# # 	duration = db.Column(db.String(10))
# # 	date = db.Column(db.String(30))
# # 	thumbnail = db.Column(db.String(100))

# # 	def __init__ (self, title, uniqueId, duration, date, thumbnail):
# # 		self.title = title
# # 		self.uniqueId = uniqueId
# # 		self.duration = duration
# # 		self.date = date
# # 		self.thumbnail = thumbnail

# # 	def __repr__ (self):
# # 		return '<TITLE : %r, UNIQUE_ID : %r, DURATION : %r, DATE : %r, THUMBNAIL : %r>' % (self.title, self.uniqueId, self.duration, self.date, self.thumbnail)

# class Music(db.Model):
# 	__tablename__ = 'music'
	
# 	index = db.Column(db.Integer, primary_key=True)
# 	title = db.Column(db.TEXT, nullable=False)
# 	uniqueId = db.Column('unique_id', db.String(15), nullable=False)
# 	length = db.Column(db.Integer, nullable=False)
# 	coverImageUrl = db.Column('cover_image_url', db.TEXT, nullable=False)
# 	src = db.Column(db.TEXT, nullable=False)

# 	def __init__ (self, title, uniqueId, length, coverImageUrl, src):
# 		self.title = title
# 		self.uniqueId = uniqueId
# 		self.length = length
# 		self.coverImageUrl = coverImageUrl
# 		self.src = src