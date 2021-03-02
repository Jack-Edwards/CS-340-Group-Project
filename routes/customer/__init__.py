from flask import Blueprint

customer_customer_routes = Blueprint('customer_customer_routes', __name__)
customer_order_routes = Blueprint('customer_order_routes', __name__)
customer_menu_routes = Blueprint('customer_menu_routes', __name__)

from .customer import *
from .order import *
from .menu import *
