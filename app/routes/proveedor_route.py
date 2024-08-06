from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.proveedor import Proveedores
from app.models.empleado import Empleados
from app.models.finca import Fincas
from app import db

bp = Blueprint('proveedor', __name__)

@bp.route('/proveedor')
def index():
    data = Proveedores.query.all()
    return render_template('proveedores/index.html', data=data)

@bp.route('/proveedor/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        cargo = request.form['cargo']
        fecha_ingreso = request.form['fecha_ingreso']
        finca_id = request.form['finca_id']
        
        new_empleado = Empleados(nombre=nombre,cargo=cargo,fecha_ingreso=fecha_ingreso,finca_id=finca_id)
        db.session.add(new_empleado)
        db.session.commit()

        return redirect(url_for('proveedor.index'))
        
    fincas = Fincas.query.all()

    return render_template('proveedores/add.html',fincas=fincas)  

@bp.route('/proveedores/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    empleado = Empleados.query.get_or_404(id)

    if request.method == 'POST':


        empleado.nombre = request.form['nombre']
        empleado.fecha = request.form['fecha_ingreso']
        empleado.finca_id = request.form['finca_id']
        

        db.session.commit()
        return redirect(url_for('empleado.index'))
    fincas = Fincas.query.all()

    return render_template('empleados/edit.html', empleado=empleado,fincas=fincas)
    

@bp.route('/empleado/delete/<int:id>')
def delete(id):
    
    empleado = Empleados.query.get_or_404(id)
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))
