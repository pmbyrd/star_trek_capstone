"""Seed file to make sample date for the imported models to test the app for development."""

from app import app
from models import db, Post

# create all tables in the database
db.create_all()

# Create sample posts
post1 = Post(title='First Post', content='This is the first post')
post2 = Post(title='Second Post', content='This is the second post')
post3 = Post(title='Third Post', content='This is the third post')
post4 = Post(title='Fourth Post', content='This is the fourth post')
post5 = Post(title='Fifth Post', content='This is the fifth post')

# Add the posts to the database
db.session.add_all([post1, post2, post3, post4, post5])
db.session.commit()
