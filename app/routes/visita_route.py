from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.proveedor import Proveedores
from app.models.visita import Visitas
from app.models.finca import Fincas
from app.models.empleado import Empleados
from app import db

bp = Blueprint('visita', __name__)

@bp.route('/visita')
def index():
    data = Visitas.query.all()
    return render_template('visitas/index.html', data=data)

@bp.route('/visita/add', methods=['GET', 'POST'])
def add():

    if request.method == 'POST':
        
        fecha = request.form['fecha']
        motivo = request.form['motivo']
        finca_id = request.form['finca_id']
        
        
        new_visita = Visitas(fecha=fecha,motivo=motivo,finca_id=finca_id)
        db.session.add(new_visita)
        db.session.commit()

        return redirect(url_for('visita.index'))
        
    fincas = Fincas.query.all()
    

    return render_template('visitas/add.html',fincas=fincas)  

@bp.route('/visita/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    visita = Visitas.query.get_or_404(id)

    if request.method == 'POST':

        visita.fecha = request.form['nombre']
        visita.motivo = request.form['motivo']
        visita.finca_id = request.form['finca_id']
        
        
        db.session.commit()
        return redirect(url_for('visita.index'))
    

    return render_template('visitas/edit.html',visita=visita)

    

@bp.route('/visita/delete/<int:id>')
def delete(id):
    
    visita = Visitas.query.get_or_404(id)
    
    db.session.delete(visita)
    db.session.commit()

    return redirect(url_for('visita.index'))
