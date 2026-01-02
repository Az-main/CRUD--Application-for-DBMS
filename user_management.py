from db_connection import get_connection

# CREATE - Add a new user
def create_user(username, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (username, email, password))
    conn.commit()
    cursor.close()
    conn.close()

# READ - Get all users
def get_all_users():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users"
    cursor.execute(query)
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users

# READ - Get a single user by ID
def get_user_by_id(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    return user

# UPDATE - Update a user
def update_user(user_id, username, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s"
    cursor.execute(query, (username, email, password, user_id))
    conn.commit()
    cursor.close()
    conn.close()

# DELETE - Delete a user
def delete_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
