from app import db

class Proveedor(db.Model):
    __tablename__='proveedor'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    contacto = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(200), nullable=False)
    animales = db.relationship('Animal', backref='proveedor', lazy=True)
    items = db.relationship('Inventario', backref='proveedor', lazy=True)