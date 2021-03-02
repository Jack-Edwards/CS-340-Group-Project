from flask import render_template, request
from . import customer_menu_routes
import database.db_connector as db
from routes import connect_to_database

@customer_menu_routes.route('/view')
@connect_to_database
def customer_menu_view(db_connection):
    query = 'SELECT id, name, price FROM Items;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    items = cursor.fetchall()
    return render_template('customer/menu/view.j2', menu_items=items)
