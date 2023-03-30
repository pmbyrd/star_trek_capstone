"""Handles the routes for the forums blueprint."""
from flask import Blueprint, render_template

forums = Blueprint(
    'forums', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/forums/static'
)

@forums.route('/forums')
def show_forums():
    render_template('forums.html')
    