""" read from a SQLite database and return data """

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# the name of the database; add path if necessary
db_name = '../prices_tracker.db'

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

# routes


@app.route('/')
def index():
    try:
        properties = Property.query.filter_by(
            type_id=1, location='Majadahonda').order_by(Property.id_product).all()
        property_text = '<ul>'
        for property in properties:
            property_text += '<li>' + property.url + \
                ', ' + str(property.price) + '€' + '</li>'
        property_text += '</ul>'
        return property_text
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


if __name__ == '__main__':
    app.run(debug=True)
