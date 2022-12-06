class BasicLibrary:
    def __init__(self, first_name, last_name, email, reader_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.reader_code = reader_code

    def __str__(self):
        return f'{self.first_name} {self.last_name}, with email \"{self.email}\"'
    
    def print_users(self):
        for data in readers_list:
            print(data)

    def create_reader(self, first_name, last_name, email):
        reader_code = str(len(first_name)) + first_name[0] + first_name[-1] +last_name[0] + last_name[-1] + str(len(email))
        new_reader = BasicLibrary(first_name, last_name, email, reader_code)
        readers_list.append(new_reader)

    def remove_reader(self, first_name, last_name, email):
        count = 0
        reader_code = str(len(first_name)) + first_name[0] + first_name[-1] +last_name[0] + last_name[-1] + str(len(email))
        for data in who_borrowed_book:
            if data[0] == reader_code:
                count += 1
        if count == 0:
            for data in readers_list:
                if data.first_name == first_name and data.last_name == last_name and data.email == email:
                    readers_list.remove(data)
        if count != 0:
            print(f'{first_name}, You still have some book(s) to return')

    def find_reader_by_code(self, reader_code):
        for i in range(readers_list.__len__()):
            if readers_list[i].reader_code == reader_code:
                print(readers_list[i].first_name, readers_list[i].last_name)

    def find_code_by_reader(self, first_name, last_name, email):
        count = 0
        for i in range(readers_list.__len__()):
            if readers_list[i].first_name == first_name and readers_list[i].last_name == last_name and readers_list[i].email == email:
                reader_code = str(len(first_name)) + first_name[0] + first_name[-1] +last_name[0] + last_name[-1] + str(len(email))
                print(f'dear {first_name}, Your \'readers code\' is: {reader_code}')
                count += 1
        if count == 0:
            print(f'I`m terrible sorry, but there is no {first_name} {last_name} with email: \"{email}\" in our Library Readers List')

    def book_borrow(self, searched_author, searched_book_name, reader_code):
        count = 0
        for author, book_info in author_books_name_copies.items():
            for book_name in book_info:
                if searched_author == author and searched_book_name == book_name and book_info[book_name] == 0:
                    print(f'Sorry, but all books with the title \"{book_name}\" by {author} are already on loan')
                    count += 1
                    break
                if searched_author == author and searched_book_name == book_name and book_info[book_name] > 0:
                    book_info[book_name] -= 1
                    who_borrowed_book.append([reader_code, author, book_name])
                    count += 1
                    break
        if count == 0:
            print(f'Ups.. \"{searched_book_name}\" written by {searched_author} is not available in this Library')

    def book_return(self, book_author, borrowed_book_name, reader_code):
        count = 0
        for data in who_borrowed_book:
            if data[0] == reader_code and data[1] == book_author and data[2] == borrowed_book_name:
                who_borrowed_book.remove(data)
                count += 1
        for author, book_info in author_books_name_copies.items():
            for book_name in book_info:
                if borrowed_book_name == book_name and author == book_author: 
                    book_info[book_name] += 1          
        if count == 0:
            print('Sorry Mate, but are you absolutely sure that this book was borrowed from this Library?')

    def how_many_books_to_return(self, reader_code):
        count = 0
        for data in who_borrowed_book:
            if data[0] == reader_code:
                count += 1
        print(f'User with code {reader_code}, you have {count} books to return.')
        BasicLibrary('','','','').what_book_to_return(reader_code)

    def what_book_to_return(self, reader_code):
        count = 0
        BasicLibrary('','','','').find_reader_by_code(reader_code)
        for data in who_borrowed_book:
            if data[0] == reader_code:
                print(f'{data[1]} by {data[2]}')
                count += 1
        if count == 0:
            print('you don`t have any books to return to the library')
                
    def add_new_book(self, book_author, book_name, how_many_copies):
        count = 0
        if book_author in author_books_name_copies:
            for author, book_info in author_books_name_copies.items():
                if book_name not in book_info and author == book_author:
                    author_books_name_copies[author].update({book_name: int(how_many_copies)})
                    count += 1
                    break
                for searched_book_name in book_info:
                    if searched_book_name == book_name:
                        book_info[book_name] += int(how_many_copies)
                        count += 1
                        break
        if count == 0:
            author_books_name_copies[book_author] = {book_name : int(how_many_copies)}

    def remove_book(self, book_author, book_name, how_many_copies):
        count = 0
        for author, book_info in author_books_name_copies.items():
            if author == book_author:
                for searched_book_name in book_info:
                    if searched_book_name == book_name:
                        book_info[book_name] -= int(how_many_copies)
                        count += 10
                        if book_info[book_name] == 0 and author == book_author:
                            print(f'There are now, after this operation, no copies of \"{book_name}\" by \" {author} in Library')
                            count += 10
                            break
        if count != 10 and count != 20:
            print(f'there is no such book as {book_name} with author {book_author} in this Library right now')
        

readers_list = []
who_borrowed_book = []
author_books_name_copies= {'Stanislaw Lem': {'Solaris': 2,
                                    'The Invincible': 3,
                                    'Fiasco': 1,
                                    'Return from the stars': 1},
                    'Stev Erikson': {'Gardens of the Moon': 5,
                                    'The Bonehunters': 2,
                                    'Deadhause Gates': 1},
                    'Samantha Shannon': {'The Priory of the Orange Tree': 2,
                                        'A Day of Fallen Night': 1}}