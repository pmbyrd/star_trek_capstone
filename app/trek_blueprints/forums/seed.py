"""A seed file to populate the database with sample date for the forums and post tables"""

from app.trek_blueprints.forums.models.posts import db, Post

# Create all tables
db.drop_all()
db.create_all()

#Todo Create 5 sample posts with different titles and content, form it as a dictionary to make it easier to add them all to the database
posts = [
    
]
