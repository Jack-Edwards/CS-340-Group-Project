from functools import wraps
import database.db_connector as db

def connect_to_database(function):
    @wraps(function)
    def wrap_function(*args, **kwargs):
        connection = db.connect_to_database()
        return function(connection, *args, **kwargs)
    return wrap_function
