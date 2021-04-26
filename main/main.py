from dataclasses import dataclass

from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:root@db/admin"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
CORS(app)

db = SQLAlchemy(app)

@dataclass
class Product(db.Model):

	id: int
	title: str
	image: str

	id = db.Column(db.Integer, primary_key=True, autoincrement=False)
	title = db.Column(db.String(200))
	image = db.Column(db.String(200))


@app.route('/api/products')
def index():
	return jsonify(Product.query.all())

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')