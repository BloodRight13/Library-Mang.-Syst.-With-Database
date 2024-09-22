import databse_connection
from mysql.connector import Error
class Author:
    
    def __init__(self, author, biography):
        self.author= author
        self.biography = biography

    def add_author(author):
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO authors (author , biography) VALUES (%s, %s)",
                           (author.author, author.biography))
            connection.commit()
            print("Author added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)
        
    def author_details():
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * biography from author")
            biographies = cursor.fetchall()
            for biography in biographies:
                print(biography)
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)


    def display_authors():
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM authors")
            authors = cursor.fetchall()
            for author in authors:
                print(author)
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)
