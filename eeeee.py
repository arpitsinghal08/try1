class Library:

    def __init__(self, listofbooks, library_name):
        self.listofbooks = listofbooks
        self.library_name = library_name
        self.user_book = {}
        self.book_count = {}
        for i in range(len(self.listofbooks) - 1):
            counter = 1
            for j in range(i + 1, len(self.listofbooks)):
                if self.listofbooks[i] == self.listofbooks[j]:
                    counter += 1
            self.book_count[self.listofbooks[i]] = counter

    def displaybook(self):
        print("name of the book: number")
        for key, value in self.book_count.items():
            print(key, ':', value)

    def lendbook(self):
        book = input('Enter the name of the book: ')
        if book in self.book_count.keys():
            if self.book_count[book] != 0:
                user_name = input('Enter your name: ')
                try:
                    self.user_book[user_name].append(book)
                except KeyError:
                    self.user_book[user_name] = [book]
                self.book_count[book] -= 1
                print("Book issued Successfully...")
            else:
                print(f"{book} is already issued to:")
                for user, book in self.user_book.items():
                    print(user)
        else:
            print("Book is not available in library")

    def addbook(self):
        book = input('Enter the name of the book: ')
        n = int(input("Enter the number of books: "))
        try:
            self.book_count[book] += n
        except KeyError:
            self.book_count[book] = n
        print("Book added Successfully...")

    def returnbook(self):
        user_name = input('Enter your name: ')
        if user_name in self.user_book.keys():
            book = input('Enter the name of the book: ')
            if book in self.user_book[user_name]:
                self.user_book[user_name].remove(book)
                self.book_count[book] += 1
                print("Book returned Successfully...")
            else:
                print(f"{book} is Not issued to {user_name}")
        else:
            print(f"{user_name} has not issued any book so far")



brajesh_library = Library(['linear algebra', 'control system', 'math', 'physics', 'history', 'chemistry', 'polity'],
                              'Brajesh Library')
while True:
    print("What do you want? Please enter your option(1/2/3/4/5):\n1. Display Books "
          "\n2. Lend Book \n3. Add Book\n4. Return book\n5. Quit")
    option = input()

    if option == '5':
        print("Thank You For Your Visit")
        break
    elif option == '1':
        brajesh_library.displaybook()
    elif option == '2':
        brajesh_library.lendbook()
    elif option == '3':
        brajesh_library.addbook()
    elif option == '4':
        brajesh_library.returnbook()
    else:
        print("Invalid input, Try again !!!")
