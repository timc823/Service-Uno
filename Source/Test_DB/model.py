from peewee import *
# from datetime import date
import os
# import time

# db = SqliteDatabase(os.getcwd() + os.path.sep + 'service.db')
db = SqliteDatabase('service.db')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    id = IntegerField()
    name = CharField()
    password = CharField()
    sex = IntegerField(default=0)
    create_time = DateField()

    class Meta:
        table_name = 'user'
        primary_key = CompositeKey('id')


class Restaurant(BaseModel):
    id = IntegerField()
    name = CharField()
    tel = CharField()
    contacts = CharField()

    class Meta:
        table_name = 'restaurant'
        primary_key = CompositeKey('id')


class Page(BaseModel):
    id = IntegerField()
    restaurant_id = IntegerField()
    questions = CharField()

    class Meta:
        table_name = 'page'
        primary_key = CompositeKey('id')


class Question(BaseModel):
    id = IntegerField()
    question = CharField()
    restaurant_id = IntegerField()
    sort = IntegerField()
    type = IntegerField(default=1)
    create_time = DateField()

    class Meta:
        table_name = 'question'
        primary_key = CompositeKey('id')


class Option(BaseModel):
    question_id = IntegerField()
    option = CharField()
    value = IntegerField()
    score = IntegerField()
    order = IntegerField()

    class Meta:
        table_name = 'option'
        primary_key = CompositeKey('id')


class Answer(BaseModel):
    page_id = IntegerField()
    question_id = IntegerField()
    answer = CharField()
    score = IntegerField()
    value = IntegerField()
    user_id = IntegerField()
    restaurant_id = IntegerField()
    create_time = DateField()

    class Meta:
        table_name = 'answer'
        primary_key = CompositeKey('id')


class PageRecord(BaseModel):
    id = IntegerField()
    user_id = IntegerField()
    restaurant_id = IntegerField()
    page_id = IntegerField()
    bill_amount = IntegerField()
    total_score = IntegerField()
    tip = IntegerField()
    waiter = CharField()

    class Meta:
        table_name = 'page_record'
        primary_key = CompositeKey('id')
