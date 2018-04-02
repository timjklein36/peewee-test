from peewee import *

from dimensions import Dimensions

db = SqliteDatabase('people.db')


class Person(Model):
    dimensions = ForeignKeyField(Dimensions, backref='person')

    class Meta:
        database = db
