from flask import Flask

from config import Config
from app.extensions import db, migrate


# from app import routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # *Initialize Flask extensions here*
    db.init_app(app)
    migrate.init_app(app, db)
    
    # *Register Blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.trek_blueprints.movies.routes import movie_bp
    app.register_blueprint(movie_bp)
    
    from app.trek_blueprints.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    from app.trek_blueprints.forums import forums_bp
    app.register_blueprint(forums_bp)
    
    @app.route('/')
    def index():
        return 'Hello Test index 2'
    
    @app.route('/test')
    def test_page():
        return 'This is a test page'
    
    return app

