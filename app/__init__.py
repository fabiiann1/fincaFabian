from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    db.init_app(app)


    from app.routes import home_route,finca_routes,animal_route,empleado_route,proveedor_route,inventario_route,medicamento_route,mantenimiento_route,visita_route
    app.register_blueprint(home_route.bp)
    app.register_blueprint(finca_routes.bp)
    app.register_blueprint(animal_route.bp)
    app.register_blueprint(empleado_route.bp)
    app.register_blueprint(proveedor_route.bp)
    app.register_blueprint(inventario_route.bp)
    app.register_blueprint(medicamento_route.bp)
    app.register_blueprint(mantenimiento_route.bp)
    app.register_blueprint(visita_route.bp)
    

    return app