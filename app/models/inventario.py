from app import db 

class Inventarios(db.Model):
    __tablename__='inventario'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha_adquisicion = db.Column(db.Date, nullable=False)
    
    finca_id = db.Column(db.Integer, db.ForeignKey('finca.id'), nullable=False)
    empleado_id = db.Column(db.Integer, db.ForeignKey('empleado.id'), nullable=False)
    proveedor_id = db.Column(db.Integer, db.ForeignKey('proveedor.id'), nullable=False)

    mantenimiento = db.relationship('Mantenimientos', back_populates='inventario')
    empleado = db.relationship('Empleados',back_populates='inventario')
    finca = db.relationship('Fincas',back_populates='inventario')
    proveedor = db.relationship('Proveedores',back_populates='inventario')