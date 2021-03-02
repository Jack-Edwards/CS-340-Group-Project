from flask import Blueprint

store_menu_routes = Blueprint('store_menu_routes', __name__)
store_employee_routes = Blueprint('store_employee_routes', __name__)
store_duty_routes = Blueprint('store_duty_routes', __name__)
store_customer_routes = Blueprint('store_customer_routes', __name__)
store_order_routes = Blueprint('store_order_routes', __name__)

from .menu import *
from .employee import *
from .duty import *
from .customer import *
from .order import *
