from flask import Flask, render_template, json, request
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
db_connection = db.connect_to_database()

# Routes

@app.route('/')
def index():
    return render_template('index.j2')

# Routes (Store)

@app.route('/store/menu/add', methods = ['GET', 'POST'])
def store_menu_add():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        data = (name, price)
        query = "INSERT INTO Items (name, price) VALUES ('%s', '%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)

    return render_template('store/menu/add.j2')

@app.route('/store/employee/view')
def store_employee_view():
    query = 'SELECT id, firstName, lastName, phone, street, city, zip, state FROM Employees;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    employees = cursor.fetchall()
    return render_template('store/employee/view.j2', employees=employees)

@app.route('/store/employee/add', methods = ['GET', 'POST'])
def store_employee_add():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        phone = request.form['phone']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = (first_name, last_name, phone, street, city, zip_code, state)
        query = "INSERT INTO Employees (firstName, lastName, phone, street, city, zip, state) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)

    return render_template('store/employee/add.j2')

@app.route('/store/duty/view')
def store_duty_view():
    query = 'SELECT id, name FROM Duties;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    duties = cursor.fetchall()
    return render_template('store/duty/view.j2', duties=duties)

@app.route('/store/duty/add', methods = ['GET', 'POST'])
def store_duty_add():
    if request.method == 'POST':
        name = request.form['name']
        data = (name)
        query = "INSERT INTO Duties (name) VALUES ('%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)

    return render_template('store/duty/add.j2')

@app.route('/store/duty/assign', methods = ['GET', 'POST'])
def store_duty_assign():
    if request.method == 'POST':
        employee_id = request.form['employee']
        duty_id = request.form['duty']
        data = (employee_id, duty_id)
        query = "INSERT IGNORE INTO EmployeeDuties (employeeId, dutyId) VALUES ('%s', '%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)

    employee_query = 'SELECT id, firstName, lastName FROM Employees;'
    cursor = db.execute_query(db_connection=db_connection, query=employee_query)
    employees = cursor.fetchall()

    duty_query = 'SELECT id, name FROM Duties;'
    cursor = db.execute_query(db_connection=db_connection, query=duty_query)
    duties = cursor.fetchall()
    return render_template('store/duty/assign.j2', employees=employees, duties=duties)

@app.route('/store/duty/view-assignments')
def store_duty_view_assignments():
    query = 'SELECT employeeId, dutyId FROM EmployeeDuties;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    assignments = cursor.fetchall()
    return render_template('store/duty/view-assignments.j2', assignments=assignments)

@app.route('/store/customer/view')
def store_customer_view():
    query = 'SELECT id, firstName, lastName, phone, street, city, zip, state FROM Customers;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    customers = cursor.fetchall()
    return render_template('store/customers/view-customers.j2', customers_list = customers)

@app.route('/store/order/view')
def store_order_view():
    query = 'SELECT id, customerId, employeeDriverId, status, statusTime, street, city, zip, state FROM Orders;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    orders = cursor.fetchall()
    return render_template('store/orders/view-orders.j2', orders_list = orders)

@app.route('/store/order/edit')
def store_order_edit():
    return render_template('store/orders/edit-order.j2')

# Routes (Customer)

@app.route('/customer/menu/view')
def customer_menu_view():
    query = 'SELECT id, name, price FROM Items;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    items = cursor.fetchall()
    return render_template('customer/menu/view.j2', menu_items=items)

@app.route('/customer/customer/add', methods = ['GET', 'POST'])
def customer_customer_add():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = (fname, lname, phone, street, city, zip_code, state)
        query = "INSERT INTO Customers (firstName, lastName, phone, street, city, zip, state) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)
    return render_template('customer/customer/add-customer.j2')

@app.route('/customer/order/add', methods = ['GET', 'POST'])
def customer_order_add():
    if request.method == 'POST':
        cid = request.form['customerid']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = (int(cid), street, city, zip_code, state)
        query = "INSERT INTO Orders (customerId, street, city, zip, state) VALUES (%d, '%s', '%s', '%s', '%s');" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)
    return render_template('customer/order/add-order.j2')

@app.route('/customer/order/assign-item', methods = ['GET', 'POST'])
def customer_order_assign_item():
    if request.method == 'POST':
        oid = request.form['orderid']
        item_id = request.form['itemid']
        quantity = request.form['quantity']
        data = (int(oid), int(item_id), int(quantity))
        query = "INSERT INTO OrderItems (orderId, itemId, quantity) VALUES (%d, %d, %d);" % data
        cursor = db.execute_query(db_connection=db_connection, query=query)
    return render_template('customer/order/add-item.j2')

@app.route('/customer/order/view', methods = ['GET', 'POST'])
def customer_order_view():
    if request.method == 'POST':
        oid = int(request.form['orderID'])
        query = 'SELECT orderId, itemId, quantity FROM OrderItems WHERE orderId=%d;' % oid 
        cursor = db.execute_query(db_connection=db_connection, query=query)
        orderItems = cursor.fetchall()
    elif request.method == 'GET':
        query = 'SELECT orderId, itemId, quantity FROM OrderItems;'
        cursor = db.execute_query(db_connection=db_connection, query=query)
        orderItems = cursor.fetchall()
    return render_template('customer/order/view-order.j2', orderItems_list = orderItems)

# Listener
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 9999))
    app.run(port=port, debug=True)