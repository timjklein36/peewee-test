from peewee import *

db = SqliteDatabase('people.db')


class Dimensions(Model):
    height = FloatField()
    weight = FloatField()

    class Meta:
        database = db
