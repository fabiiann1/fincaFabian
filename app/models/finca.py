from app import db

class Fincas(db.Model):
    __tablename__ = 'finca'
    id= db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    ubicacion = db.Column(db.String(200), nullable=False)
    tamaño = db.Column(db.Float, nullable=False)
    
    empleados = db.relationship('Empleados', back_populates='finca')
    animales = db.relationship('Animales', back_populates='finca')
    inventario = db.relationship('Inventarios', back_populates='finca')
    visitas = db.relationship('Visitas', back_populates='finca')