import databse_connection
from mysql.connector import Error

class Book:
    def __init__(self, id, title, author_id, genre_id, isbn, publication_date, ):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.genre_id = genre_id
        self.isbn = isbn
        self.publication_date = publication_date

    def add_book(book):
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO books (title, author_id, genre_id, isbn, publication_date) VALUES (%s, %s, %s, %s, %s)",
                           (book.title, book.author_id, book.genre_id, book.isbn, book.publication_date))
            connection.commit()
            print("Book added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)

    def display_books():
        connection = databse_connection.create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM books")
            books = cursor.fetchall()
            for book in books:
                print(book)
        except Error as e:
            print(f"Error: {e}")
        finally:
            databse_connection.close_connection(connection)
