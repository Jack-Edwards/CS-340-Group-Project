from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)
#db_connection = db.connect_to_database()

# Routes

@app.route('/')
def index():
    return render_template("main.j2")

# Routes (Store)

@app.route('/store/menu')
def store_menu():
    return render_template("construct.j2")

@app.route('/store/employees')
def store_employees():
    return render_template("construct.j2")

@app.route('/store/duties')
def store_duties():
    return render_template("construct.j2")

@app.route('/store/orders')
def store_orders():
    return render_template("construct.j2")

# Routes (Customer)

@app.route('/customer/menu')
def customer_menu():
    return render_template("construct.j2")

@app.route('/customer/new-order')
def customer_new_order():
    return render_template("construct.j2")

@app.route('/customer/view-order')
def customer_view_order():
    return render_template("construct.j2")

# Routes (Customer)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 9999))
    app.run(port=port, debug=True)