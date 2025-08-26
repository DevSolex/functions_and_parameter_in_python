library = ["Python for Biginners","Data Structure in C","AI Basics"]
borrowed_books = []
# student can borrow book.

# book_name = input('Enter the book name to borrow:\n>>')
# 	if book_name in library:
		# library.pop(book_name)
#	else:
#		print('book name not found')



def start():
	while True:
		option = int(input('''
		1. Display all book.
		2. Add book.
		3. Borrow book.
		4. Return book.
		5. Borrowed Books.
		6. Students that borrow books.
		7. Exit.
Enter option:\n>>'''))
		call_function(option)


def call_function(option):
	if option == 1:
		display_books()
	elif option == 2:
		add_book()
	elif option == 3:
		borrow_book()
	elif option == 4:
		return_book()
	elif option == 5:
		borrowed_book()

def display_books():
	if len(library) != 0:
		for book in library:
			print(book)

def add_book():
	book_name = input('Enter book name to add:\n>>')
	if book_name in library:
		print('BOOK ALREADY EXIST!')
	else:
		library.append(book_name.capitalize())
		print(f'YOU SUCCESSFULLY ADDED {book_name}')
def borrow_book():
	book_name = input('Enter book name to borrow:\n>>')
	if book_name in library:
		print(f'YOU SUCCESSFULLY BORROW {book_name}')
		borrowed_books.append(book_name)
		library.remove(book_name)
	else:
		print('BOOK DOES NOT EXIST!')

def return_book():
	book_name = input('Enter book name to return:\n>>')
	if book_name in borrowed_books:
		library.append(book_name)
		print(f'YOU SUCCESSFULLY RETURN {book_name}!')
	else:
		print("HAVEN'T BORROW THIS BOOK!")
def borrowed_book():
	print(borrowed_books)

start()
