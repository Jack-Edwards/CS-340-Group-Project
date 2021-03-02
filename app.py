import os
from flask import Flask, render_template
from routes.store import store_menu_routes, store_employee_routes, store_duty_routes, store_customer_routes, store_order_routes
from routes.customer import customer_customer_routes, customer_order_routes, customer_menu_routes

# Configuration

app = Flask(__name__)

# Routes

@app.route('/')
def index():
    return render_template('index.j2')

# Routes (Store)

app.register_blueprint(store_menu_routes, url_prefix='/store/menu')
app.register_blueprint(store_employee_routes, url_prefix='/store/employee')
app.register_blueprint(store_duty_routes, url_prefix='/store/duty')
app.register_blueprint(store_customer_routes, url_prefix='/store/customer')
app.register_blueprint(store_order_routes, url_prefix='/store/order')

# Routes (Customer)

app.register_blueprint(customer_customer_routes, url_prefix='/customer/customer')
app.register_blueprint(customer_order_routes, url_prefix='/customer/order')
app.register_blueprint(customer_menu_routes, url_prefix='/customer/menu')

# Listener
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9999))
    app.run(port=port, debug=True)
