from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.finca import Fincas
from app import db

bp = Blueprint('finca', __name__)

@bp.route('/finca')
def index():
    data = Fincas.query.all()
    return render_template('fincas/index.html', data=data)

@bp.route('/finca/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        
        nombre = request.form['nombre']
        ubicacion = request.form['ubicacion']
        tamaño = request.form['tamaño']
        
    
        new_animal = Fincas(nombre=nombre,ubicacion=ubicacion,tamaño=tamaño)
        db.session.add(new_animal)
        db.session.commit()
        
        return redirect(url_for('finca.index'))

    return render_template('fincas/add.html')  

@bp.route('/finca/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    finca = Fincas.query.get_or_404(id)

    if request.method == 'POST':

        finca.nombre = request.form['nombre']
        finca.ubicacion = request.form['ubicacion']
        finca.tamaño = request.form['tamaño']
        

        db.session.commit()
        return redirect(url_for('finca.index'))

    return render_template('fincas/edit.html', finca=finca)
    

@bp.route('/finca/delete/<int:id>')
def delete(id):
    
    finca = Fincas.query.get_or_404(id)
    
    db.session.delete(finca)
    db.session.commit()

    return redirect(url_for('finca.index'))
