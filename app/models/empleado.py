from app import db

class Empleados(db.Model):
    __tablename__='empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    fecha_ingreso = db.Column(db.Date, nullable=False)

    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)

    inventario = db.relationship('Inventarios', back_populates='empleado')
    medicamento = db.relationship('Medicamentos', back_populates='empleado')
    mantenimiento = db.relationship('Mantenimientos', back_populates='empleado')
    animal = db.relationship('Animales',back_populates='empleado')
    finca = db.relationship('Fincas',back_populates='empleado')