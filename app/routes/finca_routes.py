from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app.models.finca import Finca
from app import db

bp = Blueprint('finca', __name__)

@bp.route('/finca')
def index():
    data = Finca.query.all()
    return render_template('fincas/index.html', data=data)

