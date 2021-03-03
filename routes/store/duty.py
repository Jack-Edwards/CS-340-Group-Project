from flask import render_template, request, redirect, url_for
from . import store_duty_routes
from routes import connect_to_database
import database.db_connector as db

@store_duty_routes.route('/view')
@connect_to_database
def store_duty_view(db_connection):
    query = 'SELECT id, name FROM Duties;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    duties = cursor.fetchall()
    return render_template('store/duty/view.j2', duties=duties)

@store_duty_routes.route('/add', methods = ['GET', 'POST'])
@connect_to_database
def store_duty_add(db_connection):
    if request.method == 'POST':
        name = request.form['name']
        data = [name]
        query = 'INSERT INTO Duties (name) VALUES (%s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    return render_template('store/duty/add.j2')

@store_duty_routes.route('/assign', methods = ['GET', 'POST'])
@connect_to_database
def store_duty_assign(db_connection):
    if request.method == 'POST':
        employee_id = request.form['employee']
        duty_id = request.form['duty']
        data = [employee_id, duty_id]
        query = 'INSERT IGNORE INTO EmployeeDuties (employeeId, dutyId) VALUES (%s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    employee_query = 'SELECT id, firstName, lastName FROM Employees;'
    cursor = db.execute_query(db_connection=db_connection, query=employee_query)
    employees = cursor.fetchall()

    duty_query = 'SELECT id, name FROM Duties;'
    cursor = db.execute_query(db_connection=db_connection, query=duty_query)
    duties = cursor.fetchall()
    return render_template('store/duty/assign.j2', employees=employees, duties=duties)

@store_duty_routes.route('/view-assignments')
@connect_to_database
def store_duty_view_assignments(db_connection):
    query = 'SELECT employeeId, dutyId FROM EmployeeDuties;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    assignments = cursor.fetchall()
    return render_template('store/duty/view-assignments.j2', assignments=assignments)

@store_duty_routes.route('/delete/<int:id>', methods= ['POST'])
@connect_to_database
def store_duty_delete(db_connection, id):
    delete_from_employee_duties = 'DELETE FROM EmployeeDuties WHERE dutyId = %s';
    db.execute_query(db_connection=db_connection, query=delete_from_employee_duties, query_params=[id])

    delete_from_duties = 'DELETE FROM Duties WHERE id = %s;'
    db.execute_query(db_connection=db_connection, query=delete_from_duties, query_params=[id])
    return redirect(url_for('store_duty_routes.store_duty_view'))
