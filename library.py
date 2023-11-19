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

    conn.commit()

def defineAction():
    print('\nAcciones\n\n[A] Dar de alta un libro\n[B] Dar de baja un libro\n[M] Modificar un libro\n[L] Listar los libros\n')
    return input('Ingrese la acción que desea realizar: ').upper()

def generate_isbn13():
    # Generate the first 12 digits of the ISBN-13 code
    first_12_digits = ''.join(str(random.randint(0, 9)) for _ in range(12))

    # Calculate the check digit
    check_digit = 10 - (sum(int(digit) * (3 if index % 2 == 0 else 1) for index, digit in enumerate(first_12_digits)) % 10)

    # Ensure the check digit is between 0 and 9
    check_digit = check_digit % 10

    # Combine the first 12 digits and the check digit to form the complete ISBN-13 code
    isbn_code = f"{first_12_digits}{check_digit}"

    return isbn_code

def printColumns(data,cursor):
    columns = [column[0] for column in cursor.description]

    # Adjust the width for the 'title' column in the header
    header_widths = [35 if column == 'title' else 6 if column == 'id' else 20 for column in columns]

    # Print column headers
    header = "|".join(column.upper().ljust(width) for column, width in zip(columns, header_widths))
    print(header)
    print("-" * (len(header)-5))

    # Print data rows
    for row in data:
        # Adjust the width for the 'title' column in the data rows
        title_width = 35
        id_width = 6
        formatted_row = [
            str(value).ljust(title_width) if column == 'title' else str(value).ljust(id_width) if column == 'id' else str(value).ljust(20)
            for column, value in zip(columns, row)
        ]
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

    cursor.execute("INSERT INTO books (isbn, title, author, pages, edition_date, editorial, genre) VALUES (?, ?, ?, ?, ?, ?, ?)", (isbn, title, author, pages, edition_date, editorial, genre))

    conn.commit()

def deleteBook(conn):
    cursor = conn.cursor()

    # Delete a book with a specific ISBN
    isbn_to_delete = input('Ingrese el ISBN del libro a eliminar: ')
    cursor.execute("DELETE FROM books WHERE isbn = ?", (isbn_to_delete,))

    conn.commit()

def queryTitleBook(conn):
    cursor = conn.cursor()

    title = input('Ingrese el título del libro a consultar: ')
    print()

    cursor.execute("SELECT * FROM books WHERE title = ?", (title,))

    data = cursor.fetchall() # Agarra todos los campos del registro

    printColumns(data,cursor)

def modifyBook(conn):
    cursor = conn.cursor()

    isbn_to_modify = input('Ingrese el ISBN del libro a modificar: ')
    print()

    cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn_to_modify,))

    data = cursor.fetchall() # Agarra todos los campos del registro
    columns = [column[0] for column in cursor.description]
    for row in data:
        for column, value in zip(columns, row):
            modification = input(f'Desea modificar el "{column}" de este libro? [Y/N]: ').upper()
            if modification == 'Y':
                if column == 'pages':
                    new_value = int(input('Ingrese el nuevo valor: '))
                else:
                    new_value = input('Ingrese el nuevo valor: ')
                column_name = column
                cursor.execute(f"UPDATE books SET {column_name} = ? WHERE isbn = ?", (new_value, isbn_to_modify))

    conn.commit()

# LIST FUNCTIONS --------------------------------------------------------------------------------------------------------

def listAllAuthors(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT author FROM books")

    distinct_authors = cursor.fetchall()

    printColumns(distinct_authors,cursor)
        
def listBookTitles(conn):
    cursor = conn.cursor()

    print('\nTítulos: ')
    cursor.execute("SELECT DISTINCT title FROM books")

    distinct_titles = cursor.fetchall()
    printColumns(distinct_titles,cursor)

# ALL DATA 

def listEverything(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()

    print(data)

    printColumns(data,cursor)

def listGenre(conn):
    cursor = conn.cursor()

    genre = input('Ingrese el género a listar: ')

    print('\nTítulos: ')
    cursor.execute("SELECT * FROM books WHERE genre = ?", (genre,))

    distinct_genres = cursor.fetchall()
    printColumns(distinct_genres,cursor)

def listAuthor(conn):
    cursor = conn.cursor()

    author = input('Ingrese el autor a listar: ')

    cursor.execute("SELECT * FROM books WHERE author = ?", (author,))

    author_data = cursor.fetchall()
    printColumns(author_data,cursor)

def listEditorial(conn):
    cursor = conn.cursor()

    editorial = input('Ingrese la editorial a listar: ')

    cursor.execute("SELECT * FROM books WHERE editorial = ?", (editorial,))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data,cursor)

def listEditorialYears(conn):
    cursor = conn.cursor()

    editorial = input('Ingrese la editorial a listar: ')
    edition_date_1 = input('Ingrese la primera fecha: ')
    edition_date_2 = input('Ingrese la segunda fecha: ')

    cursor.execute("SELECT * FROM books WHERE editorial = ? and edition_date BETWEEN ? and ? ORDER BY edition_date", (editorial,edition_date_1,edition_date_2,))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data,cursor)

def listAYear(conn):
    cursor = conn.cursor()

    edition_year = input('Ingrese el año a listar: ')
    
    cursor.execute("SELECT * FROM books WHERE edition_date LIKE ?", (f'%{edition_year}%',))

    editorial_data = cursor.fetchall()
    printColumns(editorial_data,cursor)

def listLetterAuthor(conn):
    cursor = conn.cursor()

    author_letter = input('Ingrese la letra del apellido del autor a listar: ')
    
    cursor.execute("SELECT * FROM books WHERE SUBSTR(author, 1, 1) = ?", (author_letter,))

    author_data = cursor.fetchall()
    printColumns(author_data,cursor)

def listWordInTitle(conn):
    cursor = conn.cursor()

    title_word = input('Ingrese la palabra que deben contener los títulos a listar: ')
    
    cursor.execute("SELECT * FROM books WHERE title LIKE ?", (f'%{title_word}%',))

    data = cursor.fetchall()
    printColumns(data,cursor)

# MAIN ------------------------------------------------------------------------------------------------------------------------------

def main():
    # Open connection
    conn = sqlite3.connect('library.db')

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

main()

