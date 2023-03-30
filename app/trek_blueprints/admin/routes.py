"""Routes for the admin blueprint."""

#First I must import the blueprint object
from flask import render_template
from app.trek_blueprints.admin import admin_bp
# import database models and instances here
from app.trek_blueprints.admin.models.user import User
from app.extensions import db

@admin_bp.route('/admin')
def show_admin():
    """Displays the admin page."""
    users = User.query.all()
    return render_template('/admin/index.html', users=users)