# peewee test
This repository was created so that I could test some code while
learning and messing around with the
[peewee ORM](http://docs.peewee-orm.com/en/latest/index.html).

## Setup
You can set up the project using `virtualenv`. Activate the repo
with `virtualenv` and then run the following to install the
dependencies:
```
pip install -r requirements.txt
```

## Database
The code is set up to connect to a SQLite database called
`people.db`. If you have your own version of the database that
you would like to use instead, simply rename the original to
something else (or delete it for all I care) and name your
database `people.db`.

If you would like to start with a fresh database (without any
data) and populate it yourself, you can delete the database
file (`people.db`) and run the `init_db` script:

```
python init_db.py
```

This will create the database file and the tables that are
defined as Models in the python class files. Right now,
everything is in the root directory, because I'm lazy. That
might change if I do more with this project (like 
consolidating the Models into a common directory).

To populate the database with the dummy data I used, run the
`populate` script after you have a clean database with
tables set up:
```
python populate.py
```

## Running commands
So far the only command is...
### get_people
This was used as a test of the possibilities of passing
Model properties to python defined functions inside of a
peewee `where` clause.

Simply run:
```
python get_people.py
```