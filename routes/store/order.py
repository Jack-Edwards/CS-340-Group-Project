from flask import render_template, request
from . import store_order_routes
from routes import connect_to_database
import database.db_connector as db

@store_order_routes.route('/view')
@connect_to_database
def store_order_view(db_connection):
    query = 'SELECT id, customerId, employeeDriverId, status, statusTime, street, city, zip, state FROM Orders;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    orders = cursor.fetchall()
    return render_template('store/orders/view-orders.j2', orders_list=orders)

@store_order_routes.route('/edit/<int:id>', methods = ['GET', 'POST'])
def store_order_edit(id):
    db_connection = db.connect_to_database()
    if request.method == 'GET':
        order_query = 'SELECT id, customerId, employeeDriverId, status, street, city, zip, state FROM Orders WHERE id = %s;'
        order_cursor = db.execute_query(db_connection=db_connection, query=order_query, query_params=[id])
        order = order_cursor.fetchone()

        drivers_query = "SELECT Employees.id, Employees.firstName, Employees.lastName FROM Employees INNER JOIN EmployeeDuties ON Employees.id = EmployeeDuties.employeeId INNER JOIN Duties ON EmployeeDuties.dutyId = Duties.id WHERE Duties.name = 'Driver';"
        drivers_cursor = db.execute_query(db_connection=db_connection, query=drivers_query)
        drivers = drivers_cursor.fetchall()

        customers_query = "SELECT id, firstName, lastName from Customers;"
        customers_cursor = db.execute_query(db_connection=db_connection, query=customers_query)
        customers = customers_cursor.fetchall()

        return render_template('store/orders/edit-order.j2', order=order, drivers=drivers, customers=customers)
    elif request.method == 'POST':
        order_id = request.form['orderid']
        customer_id = request.form['customerid']
        driver_id = request.form['driverid']
        status = request.form['orderstatus']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        
        query = "UPDATE Orders SET customerId=%s, employeeDriverId=%s, status=%s, statusTime = CURRENT_TIMESTAMP, street=%s, city=%s, zip=%s, state=%s WHERE id=%s;"
        data = [int(customer_id), int(driver_id), int(status), street, city, zip_code, state, int(order_id)]
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

        orders_query = 'SELECT id, customerId, employeeDriverId, status, statusTime, street, city, zip, state FROM Orders;'
        orders_cursor = db.execute_query(db_connection=db_connection, query=orders_query)
        orders = orders_cursor.fetchall()
        return render_template('store/orders/view-orders.j2', orders_list=orders)
        
