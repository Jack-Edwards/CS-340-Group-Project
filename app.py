from flask import Flask, render_template, json
import os
#import database.db_connector as db

# Configuration

app = Flask(__name__)
#db_connection = db.connect_to_database()

# Routes

@app.route('/')
def index():
    return render_template('index.j2')

# Routes (Store)

@app.route('/store/menu/add')
def store_menu_add():
    return render_template('store/menu/add.j2')

@app.route('/store/employee/view')
def store_employee_view():
    return render_template('store/employee/view.j2')

@app.route('/store/employee/add')
def store_employee_add():
    return render_template('store/employee/add.j2')

@app.route('/store/duty/view')
def store_duty_view():
    return render_template('store/duty/view.j2')

@app.route('/store/duty/add')
def store_duty_add():
    return render_template('store/duty/add.j2')

@app.route('/store/duty/assign')
def store_duty_assign():
    return render_template('store/duty/assign.j2')

@app.route('/store/duty/view-assignments')
def store_duty_view_assignments():
    return render_template('store/duty/view-assignments.j2')

@app.route('/store/customer/view')
def store_customer_view():
    return render_template('store/customers/view-customers.j2')

@app.route('/store/order/view')
def store_order_view():
    return render_template('store/orders/view-orders.j2')

@app.route('/store/order/edit')
def store_order_edit():
    return render_template('store/orders/edit-order.j2')

# Routes (Customer)

@app.route('/customer/menu/view')
def customer_menu_view():
    return render_template('customer/menu/view.j2')

@app.route('/customer/customer/add')
def customer_customer_add():
    return render_template('customer/customer/add-customer.j2')

@app.route('/customer/order/add')
def customer_order_add():
    return render_template('customer/order/add-order.j2')

@app.route('/customer/order/assign-item')
def customer_order_assign_item():
    return render_template('customer/order/add-item.j2')

@app.route('/customer/order/view')
def customer_order_view():
    return render_template('customer/order/view-order.j2')

# Listener

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9999))
    app.run(port=port, debug=True)