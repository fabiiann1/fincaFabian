from app import db

class Medicamento(db.Model):
    __tablename__='medicamento'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    fecha_administracion = db.Column(db.Date, nullable=False)
    dosis = db.Column(db.String(50), nullable=False)
    animal_id = db.Column(db.Integer, db.ForeignKey('animal.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)