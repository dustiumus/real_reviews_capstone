from flask import Flask, render_template, redirect, flash, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
import jinja2  

app = Flask(__name__)
Bootstrap(app)

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')



@app.route('/')
def show_home():
    return render_template("home.html")

@app.route('/login', methods=['GET'])
def login():
    form = LoginForm
    return render_template("login.html", form=form)

@app.route('/realreviews', methods=['GET'])
def show_real_reviews():

    return render_template('real_reviews.html')

@app.route('/wishlist', methods=['GET'])
def show_wishlist():

    return render_template('wishlist.html')











if __name__ == '__main__':
    app.run(debug=True, port=3500)

