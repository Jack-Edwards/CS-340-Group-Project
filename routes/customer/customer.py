from flask import render_template, request
from . import customer_customer_routes
import database.db_connector as db
from routes import connect_to_database

@customer_customer_routes.route('/view')
@connect_to_database
def customer_menu_view(db_connection):
    query = 'SELECT id, name, price FROM Items;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    items = cursor.fetchall()
    return render_template('customer/menu/view.j2', menu_items=items)

@customer_customer_routes.route('/add', methods = ['GET', 'POST'])
@connect_to_database
def customer_customer_add(db_connection):
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        phone = request.form['phone']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = [fname, lname, phone, street, city, zip_code, state]
        query = 'INSERT INTO Customers (firstName, lastName, phone, street, city, zip, state) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)
    return render_template('customer/customer/add-customer.j2')
