import databse_connection
from mysql.connector import Error

class User:
    def __init__(self, id, name, library_id):
        self.id = id
        self.name = name
        self.library_id = library_id

    def add_user(user):
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (name, library_id) VALUES (%s, %s)",
                           (user.name, user.library_id))
            connection.commit()
            print("User added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)
            

    def display_users():
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM users")
            users = cursor.fetchall()
            for user in users:
                print(user)
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)
