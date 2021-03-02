from flask import render_template, request
from . import store_customer_routes
from routes import connect_to_database
import database.db_connector as db

@store_customer_routes.route('/view')
@connect_to_database
def store_customer_view(db_connection):
    query = 'SELECT id, firstName, lastName, phone, street, city, zip, state FROM Customers;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    customers = cursor.fetchall()
    return render_template('store/customers/view-customers.j2', customers_list = customers)
