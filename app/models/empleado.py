from app import db

class Empleado(db.Model):
    __tablename__='empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)
    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)

    
    items = db.relationship('Inventario', back_populates='empleado')
    medicamentos = db.relationship('Medicamento', back_populates='empleado')
    mantenimientos = db.relationship('Mantenimiento', back_populates='empleado')
    visitas = db.relationship('Visita', back_populates='empleado')