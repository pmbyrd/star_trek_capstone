"""Creates the Forums database model."""

from app.trek_blueprints.forums.models import db, Post

class Post(db.Model):
    """Generates a table for Post in the database"""
    __tablename__ = "posts"
    
    
    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True) 
    
    title = db.Column(db.String(80),
                      nullable = False)

    content = db.Column(db.Text,
                         nullable=False)