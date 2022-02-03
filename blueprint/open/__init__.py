from flask import Blueprint, render_template, redirect, url_for, request, flash
from models import User
from werkzeug.security import generate_password_hash


bp_open = Blueprint('bp_open', __name__)

@bp_open.get('/')
def index():
    return render_template("index.html")

@bp_open.get('/login')
def login_get():
    return render_template('login.html')

@bp_open.post('/login')
def login_post():
    email = request.form['email']
    password = request.form['password']
    user = User.query.filter_by(email=email).first()
    if user is None:
        flash('Wrong email or password')
        redirect(url_for('bp_open.login_get'))

   if not argon2.verify(password, user.password)
        flash('Wrong email or password')
        redirect(url_for('bp_open.login_get'))

    return redirect(url_for('bp_user.user_get'))

@bp_open.get('/signup')
def signup_get():
    return render_template('signup.html')

@bp_open.post('/signup')
def signup_post():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password, method='sha256')

    # check ig user with this password exict in database
    user = User.query.filter_by(email=email).first() # first will give us if user exist
    if user:
        flash("Email is already in use")
        return redirect(url_for('bp_open.signup_get'))

    new_user = User(name=name, email=email, password=hashed_password)

    from app import db
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('bp_open.login_get'))