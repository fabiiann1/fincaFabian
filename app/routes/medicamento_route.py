from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.finca import Fincas
from app.models.medicamento import Medicamentos
from app.models.animal import Animales
from app.models.empleado import Empleados
from app import db

bp = Blueprint('medicamento', __name__)

@bp.route('/medicamento')
def index():
    data = Medicamentos.query.all()
    return render_template('medicamentos/index.html', data=data)

@bp.route('/medicamento/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        fecha_administracion = request.form['fecha_administracion']
        dosis = request.form['dosis']
        animal_id = request.form['animal_id']
        empleado_id = request.form['empleado_id']
        
        new_medicamento = Medicamentos(nombre=nombre,descripcion=descripcion,fecha_administracion=fecha_administracion,dosis=dosis,animal_id=animal_id,empleado_id=empleado_id)
        db.session.add(new_medicamento)
        db.session.commit()
        
        return redirect(url_for('medicamento.index'))
    
    animales = Animales.query.all()
    empleados = Empleados.query.all()

    return render_template('medicamentos/add.html',animales=animales,empleados=empleados)  

@bp.route('/medicamento/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    medicamento = Medicamentos.query.get_or_404(id)

    if request.method == 'POST':

        medicamento.nombre = request.form['nombre']
        medicamento.descripcion = request.form['descripcion']
        medicamento.fecha_administracion = request.form['fecha_administracion']
        medicamento.dosis = request.form['dosis']
        medicamento.animal_id = request.form['animal_id']
        medicamento.empleado_id = request.form['empleado_id']
        
        

        db.session.commit()
        return redirect(url_for('medicamento.index'))
    
    animales = Animales.query.all()
    empleados = Empleados.query.all()

    return render_template('medicamentos/edit.html',medicamento=medicamento,empleados=empleados,animales=animales)
    

@bp.route('/medicamento/delete/<int:id>')
def delete(id):
    
    medicamento = Medicamentos.query.get_or_404(id)
    
    db.session.delete(medicamento)
    db.session.commit()

    return redirect(url_for('medicamento.index'))
