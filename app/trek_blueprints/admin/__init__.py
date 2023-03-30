"""Init file for admin blueprint."""
from flask import Blueprint

#First create the blueprint object
#Here in the init file I am telling the blueprint where to find the templates and static files
#Next I must implement the blueprint in the app/__init__.py file
admin_bp = Blueprint(
    'admin', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='/admin/static'
)

# Need to import the routes here to avoid circular imports
# Todo import the routes from the admin blueprint
from app.trek_blueprints.admin import routes