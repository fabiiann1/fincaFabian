from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.finca import Fincas
from app.models.mantenimiento import Mantenimientos
from app.models.inventario import Inventarios
from app.models.empleado import Empleados
from app import db

bp = Blueprint('mantenimiento', __name__)

@bp.route('/mantenimiento')
def index():
    data = Mantenimientos.query.all()
    return render_template('mantenimientos/index.html', data=data)

@bp.route('/mantenimiento/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
 
        descripcion = request.form['descripcion']
        fecha = request.form['fecha']
        inventario_id = request.form['inventario_id']
        empleado_id = request.form['empleado_id']

        new_mantenimiento = Mantenimientos(descripcion=descripcion,fecha=fecha,inventario_id=inventario_id,empleado_id=empleado_id)
        db.session.add(new_mantenimiento)
        db.session.commit()
        
        return redirect(url_for('mantenimiento.index'))
    
    inventarios = Inventarios.query.all()
    empleados = Empleados.query.all()

    return render_template('mantenimientos/add.html',inventarios=inventarios,empleados=empleados)  

@bp.route('/mantenimiento/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    mantenimiento= Mantenimientos.query.get_or_404(id)

    if request.method == 'POST':

        mantenimiento.descripcion = request.form['descripcion']
        mantenimiento.fecha = request.form['fecha']
        mantenimiento.inventario_id = request.form['inventario_id']
        mantenimiento.empleado_id = request.form['empleado_id']
    
        db.session.commit()
        return redirect(url_for('mantenimiento.index'))
    inventarios = Inventarios.query.all()
    empleados = Empleados.query.all()

    return render_template('mantenimientos/edit.html', mantenimiento=mantenimiento,inventarios=inventarios,empleados=empleados)
    

@bp.route('/mantenimiento/delete/<int:id>')
def delete(id):
    
    mantenimiento = Mantenimientos.query.get_or_404(id)
    
    db.session.delete(mantenimiento)
    db.session.commit()

    return redirect(url_for('mantenimiento.index')  )
