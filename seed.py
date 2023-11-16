"""Seed file to make sample data for users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()

# Add users
a = User(first_name='Adam', last_name='Ant')
b = User(first_name='Betty', last_name='Boop', image_url='https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Betty_Boop%2C_front.svg/640px-Betty_Boop%2C_front.svg.png')
c = User(first_name='John Christopher', last_name='Carter')


# https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png
# https://upload.wikimedia.org/wikipedia/commons/thumb/b/bd/Betty_Boop%2C_front.svg/640px-Betty_Boop%2C_front.svg.png

# Add to session so they'll persist
db.session.add(a)
db.session.add(b)
db.session.add(c)

db.session.commit()

