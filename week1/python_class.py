
from datetime import date, timedelta

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, book, member):
        if book.available:
            book.available = False
            due_date = date.today() + timedelta(days=14)
            print(f"{member.name} has borrowed '{book.title}'. Please return by {due_date}.")
        else:
            print(f"'{book.title}' is currently unavailable.")

    def return_book(self, book, member):
        if not book.available:
            book.available = True
            print(f"{member.name} has returned '{book.title}'. Thank you!")
        else:
            print(f"'{book.title}' is not borrowed by {member.name}.")

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id

# Test the Library management system
library = Library()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")
book4 = Book("The catcher in the rye", "J. D. Salinger")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

member1 = Member("Maryam Hashemi", "001")
member2 = Member("Francisco Cruz", "002")

library.borrow_book(book4, member1)
library.borrow_book(book2, member2)
library.borrow_book(book3, member2)

library.return_book(book2, member2)
library.return_book(book2, member1)

library.borrow_book(book3,member1)
