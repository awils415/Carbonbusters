from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user,login_required,logout_user,current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods= ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in successfully!", category= 'success')
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route('/sign-up', methods= ['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        first_Name = request.form.get('firstName')
        last_Name = request.form.get('lastName')
        email = request.form.get('email')
        co2emissions = request.form.get('co2emissions')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email has already been used.', category='error')
        elif len(first_Name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif len(last_Name) < 1:
            flash('Last name field must not be empty.', category='error')
        elif len(email) < 5:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(co2emissions) < 1:
            flash('CO2 emissions field must not be empty.', category='error')
        elif len(password1) < 7:
            flash('Password must be greater than 6 characters.', category='error')
        elif password1 != password2:
            flash('Passwords must match.', category='error')
        else:
            trees = int(float(co2emissions)*(41.67))
            one_year = round(trees/12, 0)
            two_years = round(trees/24, 0)
            three_years = round(trees/36, 0)
            ten_dollar = round(trees/120,1)
            
            new_user = User(email=email, first_Name=first_Name, last_Name=last_Name, co2emissions=co2emissions, password=generate_password_hash(password1, method='sha256'), trees=trees, one_year=one_year, two_years=two_years, three_years=three_years, ten_dollar=ten_dollar)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Your carbon offset goal has been calculated! We\'re so proud of you!', category='success')            
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)