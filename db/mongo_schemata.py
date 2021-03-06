# -*- coding:utf-8 -*-
from app import db

class Stock(db.Document):
    ticker = db.StringField(required = True, max_length = 4)


class Portfolio(db.Document):
    name = db.StringField(required = True, max_length = 120)
    user = db.ReferenceField(User)
    stocks = ListField(ReferenceField(Stock))


class User(db.Document):
    email = db.EmailField(unique = True)
    password = db.StringField(required = True, default = True, min_length = 8)
    timestamp = db.DateTimeField(default = datetime.datetime.now())
    portfolios = ListField(ReferenceField(Portfolio))
