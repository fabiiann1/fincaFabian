from . import db

class Finca(db.Model):
    __tablename__ = 'finca'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)
    tamaño = db.Column(db.Float, nullable=False)
    empleados = db.relationship('Empleado', backref='finca', lazy=True)
    animales = db.relationship('Animal', backref='finca', lazy=True)
    items = db.relationship('Inventario', backref='finca', lazy=True)
    visitas = db.relationship('Visita', backref='finca', lazy=True)