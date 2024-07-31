from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)


    from app.routes import home_route,finca_routes
    app.register_blueprint(home_route.bp)
    app.register_blueprint(finca_routes.bp)
    

    return app