from app import db

class Empleado(db.Model):
    __tablename__='empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)
    animales = db.relationship('Animal', backref='empleado', lazy=True)
    items = db.relationship('Inventario', backref='empleado', lazy=True)
    medicamentos = db.relationship('Medicamento', backref='empleado', lazy=True)
    mantenimientos = db.relationship('Mantenimiento', backref='empleado', lazy=True)
    visitas = db.relationship('Visita', backref='empleado', lazy=True)