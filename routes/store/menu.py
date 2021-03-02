from flask import render_template, request
from . import store_menu_routes
from routes import connect_to_database
import database.db_connector as db

@store_menu_routes.route('/add', methods = ['GET', 'POST'])
@connect_to_database
def store_menu_add(db_connection):
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        data = [name, price]
        query = 'INSERT INTO Items (name, price) VALUES (%s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    return render_template('store/menu/add.j2')
