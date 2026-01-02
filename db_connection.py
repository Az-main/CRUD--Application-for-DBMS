import mysql.connector

def get_connection():
    """Create and return a MySQL database connection."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="NewPass123",
        database="crud_app"
    )
    return connection
