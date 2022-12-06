from flask import Flask
from config import Config
from form import LoginForm
from flask import render_template,flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
import os

app = Flask(__name__)
app.config.from_object(Config)
app.config['SECRET_KEY'] = 'you-will-never-guess'

#database adn migration are instances in python
db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))

        return redirect(url_for('portfolio'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/image/{id}')
# path to url id to retrieve the specific
def image(id):#fetch the building by id
    images = os.listdir(os.path.join(app.static_folder, "images"))
    return render_template('image.html', images=images)

if __name__ == "__main__":
    app.run(debug=True)


