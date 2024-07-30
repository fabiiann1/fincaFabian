from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from app import db

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('index.html', data=data)