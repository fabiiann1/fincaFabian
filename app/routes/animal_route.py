from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.animal import Animales
from app.models.finca import Fincas
from app.models.empleado  import Empleados
from app.models.proveedor import Proveedores
from app import db
bp = Blueprint('animal', __name__)

@bp.route('/Animal')
def index():
    
    data = Animales.query.all()
    return render_template('animals/index.html', data=data)

@bp.route('/Animal/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        especie = request.form['especie']
        raza = request.form['raza']
        edad = request.form['edad']
        finca_id = request.form['finca_id']
        empleado_id = request.form['empleado_id']
        proveedor_id = request.form['proveedor_id']
    
        new_animal = Animales(nombre=nombre,especie=especie,raza=raza,edad=edad,finca_id=finca_id,empleado_id=empleado_id,proveedor_id=proveedor_id)
        db.session.add(new_animal)
        db.session.commit()
        
        return redirect(url_for('animal.index'))
    fincas = Fincas.query.all()
    empleados = Empleados.query.all()
    proveedores = Proveedores.query.all()

    return render_template('animals/add.html',fincas=fincas,empleados=empleados,proveedores=proveedores)  

@bp.route('/Animal/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    animal = Animales.query.get_or_404(id)

    if request.method == 'POST':

        animal.nombre = request.form['nombre']
        

        db.session.commit()
        return redirect(url_for('animal.index'))

    return render_template('animals/edit.html', animal=animal)
    

@bp.route('/Animal/delete/<int:id>')
def delete(id):
    
    animal = Animales.query.get_or_404(id)
    
    db.session.delete(animal)
    db.session.commit()

    return redirect(url_for('animal.index'))
