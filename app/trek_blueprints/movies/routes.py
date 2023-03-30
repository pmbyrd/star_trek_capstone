"""Handles the routes for the main blueprint."""

from flask import Blueprint, render_template

movie_bp = Blueprint(
    'movies', __name__, 
    template_folder='templates',
    static_folder='static', 
    static_url_path='/movies/static'
)

@movie_bp.route('/movies')
def show_movies():
    return render_template('movies.html')