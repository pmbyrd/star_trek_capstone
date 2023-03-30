"""Routes for the admin blueprint."""

#First I must import the blueprint object
from flask import render_template
from app.trek_blueprints.admin import admin_bp

@admin_bp.route('/admin')
def show_admin():
    return "This is the admin page."