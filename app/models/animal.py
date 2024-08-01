from app import db

class Animales(db.Model):
    __tablename__='animal'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especie = db.Column(db.String(50), nullable=False)
    raza = db.Column(db.String(50), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)

    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    medicamento = db.relationship('Medicamentos', backref='animal')
    empleado = db.relationship('Animales', back_populates='animal')
    proveedor = db.relationship('Proveedores',back_populates='animal')