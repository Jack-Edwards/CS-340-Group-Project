from flask import render_template, request
from . import store_employee_routes
from routes import connect_to_database
import database.db_connector as db

@store_employee_routes.route('/view')
@connect_to_database
def store_employee_view(db_connection):
    query = 'SELECT id, firstName, lastName, phone, street, city, zip, state FROM Employees;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    employees = cursor.fetchall()
    return render_template('store/employee/view.j2', employees=employees)

@store_employee_routes.route('/add', methods = ['GET', 'POST'])
@connect_to_database
def store_employee_add(db_connection):
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        phone = request.form['phone']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = [first_name, last_name, phone, street, city, zip_code, state]
        query = 'INSERT INTO Employees (firstName, lastName, phone, street, city, zip, state) VALUES (%s, %s, %s, %s, %s, %s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    return render_template('store/employee/add.j2')
