from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", booelan= True)

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_Name = request.form.get('firstName')
        last_Name = request.form.get('lastName')
        email = request.form.get('email')
        co2emissions = request.form.get('co2emissions')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(first_Name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_Name) < 1:
            flash('Last name field must not be empty.', category='error')
        elif len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(co2emissions) < 2:
            flash('CO2 emissions field must not be empty.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match.', category='error')
        else:
            new_user = User(email=email, first_Name=first_Name, last_Name=last_Name, co2emissions=co2emissions, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Your carbon offset goal has been calculated!', category='success')
            return redirect(url_for("/"))

    return render_template("signup.html")