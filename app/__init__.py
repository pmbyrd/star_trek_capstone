from flask import Flask

from config import Config


# from app import routes

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # *Initialize Flask extensions here*
    
    # *Register Blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    @app.route('/')
    def index():
        return 'Hello Test index 2'
    
    @app.route('/test')
    def test_page():
        return 'This is a test page'
    
    return app