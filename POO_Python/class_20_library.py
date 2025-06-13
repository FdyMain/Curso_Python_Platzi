class Book:
    def __init__(self,tittle,author):
        self.tittle = tittle
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"El libro {self.tittle} ha sido prestado")
        else:
            print(f"El libro {self.tittle} no está disponible")

    def return_book(self):
        self.is_available = True
        print(f"El libro {self.tittle} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"El libro {book.tittle} no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.tittle} no está en la lista de prestados")

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"El libro  {book.tittle} ha sido agregado")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Los libros disponibles:")
        for book in self.books:
            if book.is_available:
                print(f"{book.tittle} por {book.author}")

#Crear los libros
book_1 = Book("Crea", "Tony Fadel")
book_2 = Book("Si lo crees lo creas", "Byan Tryci")

#Crear un usuario
user_1 = User("Fdy", "001")

#Crear la biblioteca
library = Library()
library.add_book(book_1)
library.add_book(book_2)
library.register_user(user_1)

#Mostrar Libros
library.show_available_books()

#Prestar un libro
user_1.borrow_book(book_1)

#Mostrar Libros
library.show_available_books()

#Devolver libro
user_1.return_book(book_1)

#Mostrar Libros
library.show_available_books()

        