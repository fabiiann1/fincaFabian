from app import db

class Visitas(db.Model):
    __tablename__='visita'
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    motivo = db.Column(db.Text, nullable=False)
    resultado = db.Column(db.Text, nullable=False)
    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)