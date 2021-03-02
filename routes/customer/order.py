from flask import render_template, request
from . import customer_order_routes
from routes import connect_to_database
import database.db_connector as db

@customer_order_routes.route('/add', methods = ['GET', 'POST'])
@connect_to_database
def customer_order_add(db_connection):
    if request.method == 'POST':
        cid = request.form['customerid']
        street = request.form['street']
        city = request.form['city']
        zip_code = request.form['zip']
        state = request.form['state']
        data = [int(cid), street, city, zip_code, state]
        query = 'INSERT INTO Orders (customerId, street, city, zip, state) VALUES (%s, %s, %s, %s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    query = 'SELECT id, firstName, lastName FROM Customers;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    customers = cursor.fetchall()
    return render_template('customer/order/add-order.j2', customers_list = customers)

@customer_order_routes.route('/assign-item', methods = ['GET', 'POST'])
@connect_to_database
def customer_order_assign_item(db_connection):
    if request.method == 'POST':
        oid = request.form['orderid']
        item_id = request.form['itemid']
        quantity = request.form['quantity']
        data = [int(oid), int(item_id), int(quantity)]
        query = 'INSERT INTO OrderItems (orderId, itemId, quantity) VALUES (%s, %s, %s);'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=data)

    query = 'SELECT id from Orders ORDER BY id ASC;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    orders = cursor.fetchall()

    query = 'SELECT id, name FROM Items;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    items = cursor.fetchall()
    
    return render_template('customer/order/add-item.j2', orders=orders, items=items)

@customer_order_routes.route('/view', methods = ['GET', 'POST'])
@connect_to_database
def customer_order_view(db_connection):
    if request.method == 'POST':
        oid = [int(request.form['orderID'])]
        query = 'SELECT OrderItems.orderId, OrderItems.itemId, Items.name, Items.price, OrderItems.quantity FROM OrderItems INNER JOIN Items ON OrderItems.itemId = Items.id WHERE orderId=%d;'
        cursor = db.execute_query(db_connection=db_connection, query=query, query_params=oid)
        orderItems = cursor.fetchall()
    elif request.method == 'GET':
        query = 'SELECT OrderItems.orderId, OrderItems.itemId, Items.name, Items.price, OrderItems.quantity FROM OrderItems INNER JOIN Items ON OrderItems.itemId = Items.id;'
        cursor = db.execute_query(db_connection=db_connection, query=query)
        orderItems = cursor.fetchall()

    query = 'SELECT id from Orders ORDER BY id ASC;'
    cursor = db.execute_query(db_connection=db_connection, query=query)
    ids = cursor.fetchall()
    return render_template('customer/order/view-order.j2', orderItems_list = orderItems, ids=ids)
