"""Handles the routes for the forums blueprint."""
from flask import render_template
from app.trek_blueprints.forums import forums_bp
from app.extensions import db
from app.trek_blueprints.forums.models.posts import Post

@forums_bp.route('/forums')
def index():
    """Displays the index page."""
    posts = Post.query.all()
    return render_template('forums.html', posts=posts)
    