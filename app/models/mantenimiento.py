from app import db 

class Mantenimientos(db.Model):
    __tablname__='mantenimiento'
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.Text, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('inventario.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
