""" read from a SQLite database and return data """

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# the name of the database; add path if necessary
db_name = '../num_days_test.db'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_name

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# this variable, db, will be used for all SQLAlchemy commands
db = SQLAlchemy(app)

# each table in the database needs a class to be created for it
# db.Model is required - don't change it
# identify all columns by name and data type


class Property(db.Model):
    __tablename__ = 'properties'
    id_product = db.Column(db.Integer, primary_key=True)
    retrieved_date = db.Column(db.Date)
    created_date = db.Column(db.Date)
    url = db.Column(db.Text)
    mobile = db.Column(db.Integer)
    agency = db.Column(db.Text)
    real_estate_id = db.Column(db.Integer)
    price = db.Column(db.Integer)
    type_id = db.Column(db.Integer)
    trans_type_id = db.Column(db.Integer)
    location = db.Column(db.Text)
    num_days = db.Column(db.Integer)


# routes

@app.route('/')
def index():
    # get a list of unique values in the url column
    locations = Property.query.with_entities(Property.location).distinct()
    return render_template('index.html', locations=locations)


@app.route('/property/<location>')
def property(location):
    properties = Property.query.filter_by(
        type_id=1, location=location).order_by(Property.id_product).distinct()
    return render_template('list.html', properties=properties, location=location)


if __name__ == '__main__':
    app.run(debug=True)
