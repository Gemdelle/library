# Título, 
# Autor (hasta tres
# Cantidad de páginas
# Código ISBN
# Año de edición
# Editorial
# Género (ficción, política, biografía, historia, aventura, etc)


# FUNCIONES
# [X] Dar de alta un libro (se deberá verificar que el libro no exista).
# [X] Dar de baja un libro (se deberá verificar que el libro exista).
# [X] Consultar por un libro de un determinado título.
# [-] Modificar los datos de un libro.
# Listados: 
    #  [-] Listar todos los autores.
    #  [O] Listar todos los libros.
    #  [O] Listar todos los libros de un género determinado.
    #  [O] Listar todos los libros que posee un autor determinado.
    #  [O] Listar todos los libros de una editorial determinada.
    #  [O] Listar todos los libros de una editorial determinada en un rango de años de edición.
    #  [O] Listar todos los autores de una determinada editorial.
    #  [O] Listar todos los libros que fueron editados en un determinado año.
    #  [O] Listar todos los libros de los autores cuyos apellidos comienzan con una letra
    #  determinada.
    #  [O] Listar todos los libros cuyos títulos contengan una palabra determinada.

# ----------------------------------------------------------------------------------------------------------------------------

# SUMMARY 
    # Commit the changes
    # conn.commit()

import sqlite3
from datetime import datetime, timedelta
import random

def createDataBase(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS books
                        (isbn INTEGER PRIMARY KEY,
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

    cursor.execute("INSERT INTO books (isbn, title, author, pages, edition_date, editorial, genre) VALUES (?, ?, ?, ?, ?, ?, ?)", (isbn, author, title, pages, edition_date, editorial, genre))

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

    # Print data with field names and values
    columns = [column[0] for column in cursor.description]
    for row in data:
        for column, value in zip(columns, row):
            print(f"{column.upper()}: {value}")
        print("---")

# def modifyBook(conn):
#     cursor = conn.cursor()

#     isbn_to_modify = input('Ingrese el ISBN del libro a modificar: ')
#     print()

#     cursor.execute("SELECT * FROM books WHERE isbn = ?", (isbn_to_modify,))

#     data = cursor.fetchall() # Agarra todos los campos del registro
#     columns = [column[0] for column in cursor.description]
#     for row in data:
#         for column, value in zip(columns, row):
#             modification = (f'Desea modificar el "{column}" de este libro? [Y/N]: ')
#             if modification == 'Y':
#                 if column == 'pages':
#                     new_value = int(input('Ingrese el nuevo valor: '))
#                 else:
#                     new_value = input('Ingrese el nuevo valor: ')
#                 column_name = column
#                 cursor.execute(f"UPDATE books SET {column_name} = ? WHERE isbn = ?", (new_value, isbn_to_modify))

#     conn.commit()

def listAuthors(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT author FROM books")

    distinct_authors = cursor.fetchall()

    for author in distinct_authors:
        print(author[0])

    # # Print data with field names and values
    # columns = [column[0] for column in cursor.description]
    # for row in data:
    #     for column, value in zip(columns, row):
    #         print(f"{column.upper()}: {value}")
    #     print("---")

def listEverything(conn):
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    data = cursor.fetchall()
    for row in data:
        print(row)

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
        # elif action == 'M':
        #     modifyBook(conn)
        elif action == 'LA':
            listAuthors(conn)
        action = defineAction()

    # Close connection
    conn.close()
    print('Gracias por visitar la biblioteca')

main()

