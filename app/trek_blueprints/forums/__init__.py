from flask import Blueprint

forums_bp = Blueprint(
    'forums', __name__,
    static_folder='static',
    static_url_path='/forums/static',
    template_folder='templates'
)

from app.trek_blueprints.forums import routes