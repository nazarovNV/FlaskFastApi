from flask import Blueprint, jsonify
from models import db, User, Product

routes = Blueprint('routes', __name__)

@routes.route('/users')
def get_users():
    users = User.query.all()
    return jsonify([user.username for user in users])

@routes.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([product.name for product in products])
