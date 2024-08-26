from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os

app = Flask(__name__)



db = SQLAlchemy()

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(24)
    app.config.from_object('config.Config')

    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    @login_manager.user_loader
    def load_user(user_id):
 
        from .models.user import Usuario
        return Usuario.query.get(int(user_id))


    from app.routes import home_route,finca_routes,animal_route,empleado_route,proveedor_route,inventario_route,medicamento_route,mantenimiento_route,visita_route,user_route
    app.register_blueprint(home_route.bp)
    app.register_blueprint(finca_routes.bp)
    app.register_blueprint(animal_route.bp)
    app.register_blueprint(empleado_route.bp)
    app.register_blueprint(proveedor_route.bp)
    app.register_blueprint(inventario_route.bp)
    app.register_blueprint(medicamento_route.bp)
    app.register_blueprint(mantenimiento_route.bp)
    app.register_blueprint(visita_route.bp)
    app.register_blueprint(user_route.auth_bp)
    

    return app