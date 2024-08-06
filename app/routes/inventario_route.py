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

@bp.route('/inventarios/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    inventarios = Inventarios.query.get_or_404(id)

    if request.method == 'POST':

        inventarios.nombre = request.form['nombre']
        inventarios.categoria = request.form['categoria']
        inventarios.descripcion = request.form['descripcion']
        inventarios.cantidad= request.form['cantidad']
        inventarios.fecha_adquisicion = request.form['fecha_adquisicion']
        

        db.session.commit()
        return redirect(url_for('inventario.index'))

    return render_template('inventarios/edit.html')
    

@bp.route('/inventario/delete/<int:id>')
def delete(id):
    
    invenatario = Inventarios.query.get_or_404(id)
    
    db.session.delete(invenatario)
    db.session.commit()

    return redirect(url_for('inventario.index'))
