# Título,
# Autor (hasta tres
# Cantidad de páginas
# Código ISBN
# Año de edición
# Editorial
# Género (ficción, política, biografía, historia, aventura, etc)

# SUMMARY
# Commit the changes
# conn.commit()

# BOOK LIST
# The Garden of Forking Paths

import sqlite3
from datetime import datetime, timedelta
import random

original_books = {
    '9780143116622': {
        'title': 'The Adventures of Sherlock Holmes',
        'author': 'Arthur Conan Doyle',
        'pages': 320,
        'edition_date': '2009-10-06',
        'editorial': 'Penguin Classics',
        'genre': 'Mystery'
    },
    '9780316486482': {
        'title': "The Cuckoo's Calling",
        'author': 'J.K. Rowling',
        'pages': 464,
        'edition_date': '2018-04-03',
        'editorial': 'Mulholland Books',
        'genre': 'Mystery'
    },
    '9780679727550': {
        'title': 'In Cold Blood',
        'author': 'Truman Capote',
        'pages': 368,
        'edition_date': '1994-02-01',
        'editorial': 'Vintage',
        'genre': 'Mystery'
    },
    '9780441172719': {
        'title': 'Dune',
        'author': 'Frank Herbert',
        'pages': 896,
        'edition_date': '2010-09-01',
        'editorial': 'Ace',
        'genre': 'Sci-Fi'
    },
    '9780316129081': {
        'title': 'The Expanse',
        'author': 'James S.A. Corey',
        'pages': 561,
        'edition_date': '2011-06-15',
        'editorial': 'Orbit',
        'genre': 'Sci-Fi'
    },
    '9780553382563': {
        'title': 'I, Robot',
        'author': 'Isaac Asimov',
        'pages': 304,
        'edition_date': '2008-04-29',
        'editorial': 'Spectra',
        'genre': 'Sci-Fi'
    },
    '9780553560732': {
        'title': 'Red Mars',
        'author': 'Kim Stanley Robinson',
        'pages': 572,
        'edition_date': '1993-05-01',
        'editorial': 'Spectra',
        'genre': 'Sci-Fi'
    },
    '9780316091011': {
        'title': 'Jurassic Park',
        'author': 'Michael Crichton',
        'pages': 448,
        'edition_date': '2012-11-20',
        'editorial': 'Ballantine Books',
        'genre': 'Sci-Fi'
    },
    '9780553573404': {
        'title': 'A Game of Thrones',
        'author': 'George R.R. Martin',
        'pages': 864,
        'edition_date': '2002-08-06',
        'editorial': 'Bantam',
        'genre': 'Fantasy'
    },
    '9780544272996': {
        'title': 'The Lord of the Rings',
        'author': 'J.R.R. Tolkien',
        'pages': 1178,
        'edition_date': '2012-09-25',
        'editorial': 'Mariner Books',
        'genre': 'Fantasy'
    },
    '9780060762732': {
        'title': 'The Chronicles of Narnia',
        'author': 'C.S. Lewis',
        'pages': 206,
        'edition_date': '2002-08-22',
        'editorial': 'HarperCollins',
        'genre': 'Fantasy'
    },
    '9780439064873': {
        'title': 'Harry Potter & the Secret Chamber',
        'author': 'J.K. Rowling',
        'pages': 352,
        'edition_date': '2000-06-02',
        'editorial': 'Scholastic',
        'genre': 'Fantasy'
    },
    '9781408880715': {
        'title': 'Fantastic Creatures',
        'author': 'J.K. Rowling',
        'pages': 160,
        'edition_date': '2017-11-07',
        'editorial': 'Arthur A. Levine Books',
        'genre': 'Fantasy'
    },
    '9780553296983': {
        'title': 'The Notebook',
        'author': 'Nicholas Sparks',
        'pages': 240,
        'edition_date': '1997-10-01',
        'editorial': 'Grand Central Publishing',
        'genre': 'Romance'
    },
    '9780440241164': {
        'title': 'Outlander',
        'author': 'Diana Gabaldon',
        'pages': 896,
        'edition_date': '2014-07-02',
        'editorial': 'Dell',
        'genre': 'Romance'
    },
    '9780525436471': {
        'title': 'Attachments',
        'author': 'Rainbow Rowell',
        'pages': 368,
        'edition_date': '2012-04-14',
        'editorial': 'Dutton',
        'genre': 'Romance'
    },
    '9781501173219': {
        'title': 'All the Light We Cannot See',
        'author': 'Anthony Doerr',
        'pages': 544,
        'edition_date': '2017-09-05',
        'editorial': 'Scribner',
        'genre': 'History'
    },
    '9781491957660': {
        'title': 'Python in a Nutshell',
        'author': 'Alex Martelli',
        'pages': 738,
        'edition_date': '2017-11-30',
        'editorial': 'O\'Reilly Media',
        'genre': 'History'
    },
    '9781941270007': {
        'title': 'My Great Predecessors',
        'author': 'Garry Kasparov',
        'pages': 544,
        'edition_date': '2003-10-01',
        'editorial': 'Everyman Chess',
        'genre': 'History'
    },
    '9780307588506': {
        'title': 'Catholicism',
        'author': 'Robert Barron',
        'pages': 304,
        'edition_date': '2011-10-18',
        'editorial': 'Image',
        'genre': 'History'
    },
    '9788401012917': {
        'title': "Charlotte's Web",
        'author': 'E.B. White',
        'pages': 192,
        'edition_date': '2015-02-17',
        'editorial': 'DeBolsillo',
        'genre': 'Children'
    },
    '9780241003008': {
        'title': 'The Very Hungry Caterpillar',
        'author': 'Eric Carle',
        'pages': 32,
        'edition_date': '2011-03-03',
        'editorial': 'Penguin Publishing Group',
        'genre': 'Children'
    },
    '9780545042207': {
        'title': 'The Polar Express',
        'author': 'Chris Van Allsburg',
        'pages': 32,
        'edition_date': '2013-09-24',
        'editorial': 'Houghton Mifflin Harcourt',
        'genre': 'Children'
    },
    '9780061124952': {
        'title': 'The Sword in the Stone',
        'author': 'T.H. White',
        'pages': 256,
        'edition_date': '2001-08-01',
        'editorial': 'HarperCollins',
        'genre': 'Children'
    },
}


def createDataBase(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        isbn INTEGER,
                        title TEXT,
                        author TEXT,
                        pages INTEGER,
                        edition_date DATE,
                        editorial TEXT,
                        genre TEXT
                        )''')

    cursor.execute("SELECT COUNT(*) FROM books")
    row_count = cursor.fetchone()[0]

    if row_count == 0:
        for isbn, book_data in original_books.items():

            title = book_data['title']
            author = book_data['author']
            pages = book_data['pages']
            edition_date = book_data['edition_date']
            editorial = book_data['editorial']
            genre = book_data['genre']

            cursor.execute("INSERT INTO books (isbn, title, author, pages, edition_date, editorial, genre) VALUES (?, ?, ?, ?, ?, ?, ?)",
                           (isbn, title, author, pages, edition_date, editorial, genre))

    conn.commit()


def defineAction():
    print(
        '\nAcciones\n\n[A] Dar de alta un libro\n[B] Dar de baja un libro\n[M] Modificar un libro\n[L] Listar los libros\n')
    return input('Ingrese la acción que desea realizar: ').upper()


def generate_isbn13():
    # Generate the first 12 digits of the ISBN-13 code
    first_12_digits = ''.join(str(random.randint(0, 9)) for _ in range(12))

    # Calculate the check digit
    check_digit = 10 - (sum(int(digit) * (3 if index % 2 == 0 else 1)
                        for index, digit in enumerate(first_12_digits)) % 10)

    # Ensure the check digit is between 0 and 9
    check_digit = check_digit % 10

    # Combine the first 12 digits and the check digit to form the complete ISBN-13 code
    isbn_code = f"{first_12_digits}{check_digit}"

    return isbn_code


def printColumns(data, cursor):
    columns = [column[0] for column in cursor.description]

    # Define the default width for missing fields
    default_width = 15

    # Define the widths for specific fields
    widths_mapping = {
        'id': 4,
        'isbn': 20,
        'title': 40,
        'author': 25,
        'pages': 10,
        'edition_date': default_width,
        'editorial': 30,
        'genre': default_width
    }

    # Adjust the width for each column in the header
    header_widths = [widths_mapping.get(column, default_width)
                    for column in columns]

    # Print column headers
    header_str = "|".join(str(column).upper().ljust(width)
                        for column, width in zip(columns, header_widths))
    print(header_str)
    print("-" * sum(header_widths))  # Print separator line

    # Print data rows
    for row in data:
        # Adjust the width for each column in the data rows
        formatted_row = [str(value).ljust(widths_mapping.get(
            column, default_width)) for column, value in zip(columns, row)]
        row_str = "|".join(formatted_row)
        print(row_str)

def addBook(conn):
    cursor = conn.cursor()

    print('Ingrese los datos del libro a agregar: ')
    isbn = generate_isbn13()
    title = input('Título: ')
    author = input('Autor/es: ')
    pages = int(input('Páginas: '))
    edition_date = input('Fecha de edición [YYYY-MM-DD]: ')
    editorial = input('Editorial: ')
    genre = input('Genre: ')

    cursor.execute("INSERT INTO books (isbn, title, author, pages, edition_date, editorial, genre) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (isbn, title, author, pages, edition_date, editorial, genre))

    conn.commit()


def deleteBook(conn):
    cursor = conn.cursor()

    # Delete a book with a specific ISBN
    isbn_to_delete = input('Ingrese el ISBN del libro a eliminar: ')
    cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn_to_delete,))

    conn.commit()


def queryTitleBook(conn,title):
    cursor = conn.cursor()

    # title = input('Ingrese el título del libro a consultar: ')
    # print()

    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))

    data = cursor.fetchall()  # Agarra todos los campos del registro
    
    # printColumns(data, cursor)
    return data

def modifyBook(conn):
    cursor = conn.cursor()

    isbn_to_modify = input('Ingrese el ISBN del libro a modificar: ')
    print()

    cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn_to_modify,))

    data = cursor.fetchall()  # Agarra todos los campos del registro
    columns = [column[0] for column in cursor.description]
    for row in data:
        for column, value in zip(columns, row):
            modification = input(
                f'Desea modificar el "{column}" de este libro? [Y/N]: ').upper()
            if modification == 'Y':
                if column == 'pages':
                    new_value = int(input('Ingrese el nuevo valor: '))
                else:
                    new_value = input('Ingrese el nuevo valor: ')
                column_name = column
                cursor.execute(
                    f"UPDATE books SET {column_name} = ? WHERE isbn = ?", (new_value, isbn_to_modify))

    conn.commit()

# LIST FUNCTIONS --------------------------------------------------------------------------------------------------------


def listAllAuthors(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT author FROM books ORDER BY author")

    distinct_authors = cursor.fetchall()

    # printColumns(distinct_authors, cursor)
    return distinct_authors


def listBookTitles(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT title FROM books ORDER BY title")

    distinct_titles = cursor.fetchall()
    printColumns(distinct_titles, cursor)

# ALL DATA


def listEverything(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()

    return data


def listGenre(conn):
    cursor = conn.cursor()

    genre = input('Ingrese el género a listar: ')

    print('\nTítulos: ')
    cursor.execute("SELECT * FROM books WHERE genre = ? ORDER BY genre", (genre,))

    distinct_genres = cursor.fetchall()
    printColumns(distinct_genres, cursor)


def listAuthor(conn):
    cursor = conn.cursor()

    author = input('Ingrese el autor a listar: ')

    cursor.execute("SELECT * FROM books WHERE author = ? ORDER BY title", (author,))

    author_data = cursor.fetchall()
    printColumns(author_data, cursor)


def listEditorial(conn):
    cursor = conn.cursor()

    editorial = input('Ingrese la editorial a listar: ')

    cursor.execute("SELECT * FROM books WHERE editorial = ? ORDER BY title", (editorial,))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data, cursor)


def listEditorialYears(conn):
    cursor = conn.cursor()

    editorial = input('Ingrese la editorial a listar: ')
    edition_date_1 = input('Ingrese la primera fecha: ')
    edition_date_2 = input('Ingrese la segunda fecha: ')

    cursor.execute("SELECT * FROM books WHERE editorial = ? and edition_date BETWEEN ? and ? ORDER BY edition_date, title",
                   (editorial, edition_date_1, edition_date_2,))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data, cursor)


def listAYear(conn):
    cursor = conn.cursor()

    edition_year = input('Ingrese el año a listar: ')

    cursor.execute("SELECT * FROM books WHERE edition_date LIKE ? ORDER BY title",
                   (f'%{edition_year}%',))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data, cursor)


def listLetterAuthor(conn):
    cursor = conn.cursor()

    author_letter = input('Ingrese la letra del apellido del autor a listar: ')

    cursor.execute(
        "SELECT * FROM books WHERE SUBSTR(author, 1, 1) = ?", (author_letter,))

    author_data = cursor.fetchall()
    printColumns(author_data, cursor)


def listWordInTitle(conn):
    cursor = conn.cursor()

    title_word = input(
        'Ingrese la palabra que deben contener los títulos a listar: ')

    cursor.execute("SELECT * FROM books WHERE title LIKE ? ORDER BY title",
                   (f'%{title_word}%',))

    data = cursor.fetchall()
    printColumns(data, cursor)

# MAIN ------------------------------------------------------------------------------------------------------------------------------

conn = sqlite3.connect('library.db')

def main():
    
    createDataBase(conn)

    action = defineAction()
    while action != 'E':
        if action == 'A':
            addBook(conn)
        elif action == 'D':
            deleteBook(conn)
        elif action == 'L':
            listEverything(conn)
        elif action == 'QT':
            queryTitleBook(conn)
        elif action == 'M':
            modifyBook(conn)
        elif action == 'LAA':
            listAllAuthors(conn)
        elif action == 'LT':
            listBookTitles(conn)
        elif action == 'LG':
            listGenre(conn)
        elif action == 'LA':
            listAuthor(conn)
        elif action == 'LE':
            listEditorial(conn)
        elif action == 'LEY':
            listEditorialYears(conn)
        elif action == 'LY':
            listAYear(conn)
        elif action == 'WT':
            listWordInTitle(conn)

        action = defineAction()

    # Close connection
    conn.close()
    print('Gracias por visitar la biblioteca')


# main()
