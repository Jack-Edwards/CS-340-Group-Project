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

@store_order_routes.route('/edit')
def store_order_edit():
    return render_template('store/orders/edit-order.j2')
