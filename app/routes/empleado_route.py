from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.empleado import Empleados
from app import db

bp = Blueprint('empleado', __name__)

@bp.route('/empleado')
def index():
    data = Empleados.query.all()
    return render_template('empleados/index.html', data=data)

@bp.route('/empleado/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        fecha = request.form['fecha']
        motivo = request.form['motivo']
        
    
        new_empleado = Empleados(nombre=nombre,fecha=fecha,motivo=motivo)
        db.session.add(new_empleado)
        db.session.commit()
        
        return redirect(url_for('empleado.index'))

    return render_template('empleados/add.html')  

@bp.route('/empleado/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    empleado = Empleados.query.get_or_404(id)

    if request.method == 'POST':


        empleado.nombre = request.form['nombre']
        empleado.fecha = request.form['fecha']
        empleado.motivo = request.form['motivo']

        db.session.commit()
        return redirect(url_for('empleado.index'))

    return render_template('empleados/edit.html', empleado=empleado)
    

@bp.route('/empleado/delete/<int:id>')
def delete(id):
    
    empleado = Empleados.query.get_or_404(id)
    
    db.session.delete(empleado)
    db.session.commit()

    return redirect(url_for('empleado.index'))
