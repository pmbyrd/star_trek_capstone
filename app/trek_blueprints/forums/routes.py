"""Handles the routes for the forums blueprint."""
from flask import render_template
from app.trek_blueprints.forums import forums_bp

@forums_bp.route('/forums')
def show_forums():
    return "This is a test of the forums blueprint."
    