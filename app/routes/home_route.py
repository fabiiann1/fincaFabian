from flask import Blueprint, render_template, request, redirect, url_for, jsonify

bp = Blueprint('home', __name__)

@bp.route('/')
def index():
    return render_template('home/index.html')