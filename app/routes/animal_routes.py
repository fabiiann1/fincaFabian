from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.animal import Animal
from app.models.movie import Movie
from app import db

bp = Blueprint('aniamal', __name__)

@bp.route('/')
def index():
    data = Movie.query.all()
    return render_template('movies/index.html', data=data)


@bp.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form['titulo']
        
        
        newMovie = Movie(titulo=titulo)
        db.session.add(newMovie)
        db.session.commit()
        
        return redirect(url_for('movie.index'))
    data = Actor.query.all()
    return render_template('movies/add.html', data=data)

@bp.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    movie = Movie.query.get_or_404(id)

    if request.method == 'POST':
        movie.titulo = request.form['titulo']

        db.session.commit()

        return redirect(url_for('movie.index'))

    return render_template('movies/edit.html', movie=movie)


@bp.route('/delete/<int:id>')
def delete(id):
    movie = Movie.query.get_or_404(id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('movie.index'))
    