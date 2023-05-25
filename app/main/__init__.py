from flask import Blueprint

main = Blueprint('main', __name__)

 #*This allows the routes to be imported from the app/main/__init__.py file
from app.main import routes
print("main blueprint imported")
print("hello from main blueprint")