"""
Database Setup Script
Run this once to create the database and tables.
"""
import mysql.connector

# Connect to MySQL (without specifying database first)
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="NewPass123"
)
cursor = conn.cursor()

# Create database
cursor.execute("CREATE DATABASE IF NOT EXISTS crud_app")
cursor.execute("USE crud_app")

# Create users table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        email VARCHAR(100) NOT NULL,
        password VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Create products table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        description TEXT,
        price DECIMAL(10, 2) NOT NULL,
        quantity INT NOT NULL DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
""")

# Check if users table is empty, then add sample data
cursor.execute("SELECT COUNT(*) FROM users")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO users (username, email, password) VALUES
        ('admin', 'admin@example.com', 'admin123'),
        ('john_doe', 'john@example.com', 'password123')
    """)

# Check if products table is empty, then add sample data
cursor.execute("SELECT COUNT(*) FROM products")
if cursor.fetchone()[0] == 0:
    cursor.execute("""
        INSERT INTO products (name, description, price, quantity) VALUES
        ('Laptop', 'High performance laptop', 999.99, 10),
        ('Mouse', 'Wireless mouse', 29.99, 50),
        ('Keyboard', 'Mechanical keyboard', 79.99, 25)
    """)

conn.commit()
cursor.close()
conn.close()

print("✅ Database 'crud_app' setup completed successfully!")
print("✅ Tables 'users' and 'products' created!")
print("✅ Sample data inserted!")
print("\nYou can now run the app with: streamlit run app.py")
