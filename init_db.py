from peewee import *

from person import Person
from dimensions import Dimensions

db = SqliteDatabase('people.db')

db.create_tables([Person, Dimensions])
