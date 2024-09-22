import databse_connection
from Author_Class import Author
from Book_Class import Book
from User_Class import User

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []
        self.genres = []

    def main_menu(self):
        while True:
            print("\nWelcome to the Library Management System!\n")
            print("Main Menu:")
            print("1. Book Operations")
            print("2. User Operations")
            print("3. Author Operations")
            print("4. Quit")

            choice = input("Select an option: ")
            if choice == '1':
                self.book_operations()
            elif choice == '2':
                self.user_operations()
            elif choice == '3':
                self.author_operations()
            elif choice == '4':
                print("Thank you for using or Library Managment System. \nGoodbye!")
                break
            else:
                print("Sorry you choice was invalid. Please try again.")

    def book_operations(self):
        while True:
            print("\nBook Operations:")
            print("1. Add a new book")
            print("2. Borrow a book")
            print("3. Return a book")
            print("4. Search for a book")
            print("5. Display all books")
            print("6. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_book()
            elif choice == '2':
                self.borrow_book()
            elif choice == '3':
                self.return_book()
            elif choice == '4':
                self.search_book()
            elif choice == '5':
                self.display_all_books()
            elif choice == '6':
                break
            else:
                print("Sorry you choice was invalid. Please try again.")

    def user_operations(self):
        while True:
            print("\nUser Operations:")
            print("1. Add a new user")
            print("2. View user details")
            print("3. Display all users")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_user()
            elif choice == '2':
                self.view_user_details()
            elif choice == '3':
                self.display_all_users()
            elif choice == '4':
                break
            else:
                print("Sorry you choice was invalid. Please try again.")

    def author_operations(self):
        while True:
            print("\nAuthor Operations:")
            print("1. Add a new author")
            print("2. View author details")
            print("3. Display all authors")
            print("4. Back to Main Menu")

            choice = input("Select an option: ")
            if choice == '1':
                self.add_author()
            elif choice == '2':
                self.view_author_details()
            elif choice == '3':
                self.display_authors()
            elif choice == '4':
                break
            else:
                print("Sorry you choice was invalid. Please try again.")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main_menu()
