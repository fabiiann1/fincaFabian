from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.proveedor import Proveedores
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
        contacto = request.form['contacto']
        direccion = request.form['direccion']
        
        new_proveedor = Proveedores(nombre=nombre,contacto=contacto,direccion=direccion)
        db.session.add(new_proveedor)
        db.session.commit()

        return redirect(url_for('proveedor.index'))
        
    

    return render_template('proveedores/add.html')  

@bp.route('/proveedores/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):

    proveedor = Proveedores.query.get_or_404(id)

    if request.method == 'POST':


        proveedor.nombre = request.form['nombre']
        proveedor.contacto = request.form['contacto']
        proveedor.direccion = request.form['direccion']
        

        db.session.commit()
        return redirect(url_for('proveedor.index'))
    

    return render_template('proveedores/edit.html', proveedor=proveedor)
    

@bp.route('/proveedor/delete/<int:id>')
def delete(id):
    
    proveedor = Proveedores.query.get_or_404(id)
    
    db.session.delete(proveedor)
    db.session.commit()

    return redirect(url_for('proveedor.index'))
