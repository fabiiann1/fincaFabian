from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.finca import Fincas
from app.models.inventario import Inventarios
from app.models.empleado import Empleados
from app.models.proveedor import Proveedores
from app import db

bp = Blueprint('inventario', __name__)

@bp.route('/inventario')
def index():
    data = Inventarios.query.all()
    return render_template('inventarios/index.html', data=data)

@bp.route('/inventario/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        descripcion = request.form['descripcion']
        cantidad = request.form['cantidad']
        fecha_adquisicion = request.form['fecha_adquisicion']
        finca_id = request.form['finca_id']
        empleado_id = request.form['empleado_id']
        proveedor_id = request.form['proveedor_id']        
        new_inventario = Inventarios(nombre=nombre,categoria=categoria,descripcion=descripcion,cantidad=cantidad,fecha_adquisicion=fecha_adquisicion,finca_id=finca_id,empleado_id=empleado_id,proveedor_id=proveedor_id)
        db.session.add(new_inventario)
        db.session.commit()
        
        return redirect(url_for('inventario.index'))
    
    fincas = Fincas.query.all()
    empleados = Empleados.query.all()
    proveedores = Proveedores.query.all()

    return render_template('inventarios/add.html',fincas=fincas,empleados=empleados,proveedores=proveedores)  

@bp.route('/inventario/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    inventario = Inventarios.query.get_or_404(id)

    if request.method == 'POST':

        inventario.nombre = request.form['nombre']
        inventario.categoria = request.form['categoria']
        inventario.descripcion = request.form['descripcion']
        inventario.cantidad= request.form['cantidad']
        inventario.fecha_adquisicion = request.form['fecha_adquisicion']
        inventario.finca_id = request.form['finca_id']
        inventario.empleado_id = request.form['empleado_id']
        inventario.proveedor_id = request.form['proveedor_id'] 

        db.session.commit()
        return redirect(url_for('inventario.index'))
    
    fincas = Fincas.query.all()
    empleados = Empleados.query.all()
    proveedores = Proveedores.query.all()

    return render_template('inventarios/edit.html', inventario=inventario,fincas=fincas,empleados=empleados,proveedores=proveedores)
    

@bp.route('/inventario/delete/<int:id>')
def delete(id):
    
    invenatario = Inventarios.query.get_or_404(id)
    
    db.session.delete(invenatario)
    db.session.commit()

    return redirect(url_for('inventario.index'))
