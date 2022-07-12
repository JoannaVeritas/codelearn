'''very simple form of library'''
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        #self.status = status
        # self.quantity = quantity
        
        
    # def add_book(self, add):
    #     '''adds a book to quantity of specific book'''
    #     self.quantity =+ add
    #     return self.quantity
        

    def details(self):
        '''prints out details of given book'''
        print('Title:', self.title)
        print('Author:', self.author)
        print('No of pages:', self.pages)
        print('Quantity in library', self.quantity)
        

class User:
    def __init__(self, name):
        self.name = name
        self.rented_books = []

    def add_to_rented(self, book):
        if len(self.rented_books) < 3:
            self.rented_books.append(book)
            return print(f'{book} added to rented books')
        return print(f'{self.name} has the maximum number of books already rented')

    def details(self):
        print('Name:', self.name)
        print('Rented books: ', self.rented_books)

u1 = User('Tom')
u2 = User('Kate')
u3 = User('Marta')
u4 = User('Kris')

b1 = Book('How to survive', 'Bear Gryls', 243)
b2 = Book('Business book', 'Mr C.', 5)
b3 = Book('Computer Science', 'John W.', 245666)
b4 = Book('Python for everybody', 'Charles Severs', 400)
b5 = Book('Kotlin is fun', 'Marta Nowaczyk', 1000)


def renting(user, book):
    print(f'{user.name} wants to rent {book}')
    if book in list_of_available:
        user.add_to_rented(book)
        list_of_available.remove(book)
        list_of_NOT_available.append(book)
    else:
        print(f'{book} is not available for renting') 

def returnBook(user, book):
    pass


def checkIfAvailable(book):
    if book in list_of_available:
        print(f'Yes, {book} is available for renting')
    else:   
        if book not in list_of_NOT_available:
            print('Our library does not have this book')

list_of_available = [b1.title, b1.title, b1.title, b2.title, b2.title, b3.title, b3.title, b3.title, b4.title, b4.title, b4.title, b5.title, 
b5.title, b5.title]
list_of_NOT_available = []
whole_library_list = [list_of_available, list_of_NOT_available]


renting(u2,b1.title)
u2.details()

renting(u2,b3.title)
renting(u2,b3.title)
renting(u2, b2.title)
renting(u2, b4.title)

checkIfAvailable('Computer Science')