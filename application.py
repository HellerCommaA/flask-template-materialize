from flask import Flask, render_template
from flask_material import Material
from forms import ExampleForm
from flask.ext.sqlalchemy import SQLAlchemy

# initializes app
application = Flask(__name__)
app = application

# sets up sqlalchemy bindings for app
db = SQLAlchemy(app)

# applies matieral design
Material(app)

#loads config values from config.py
app.config.from_object('config')

@app.route('/')
def hello_world():
    form = ExampleForm()
    return render_template('test.html', form = form)

if __name__ == '__main__':
    app.run(debug = True) # disable debug on production server!!
