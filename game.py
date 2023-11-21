import pygame
import sys
from library import *

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Library")

line_height = 25
height = 280
processed_text = []
processed_text_book_title = []
processed_text_list_everything = []
x_id = 160
x_isbn = 200
x_title = 400
x_author = 820
x_pages = 1050
x_editiondate = 1150
x_editorial = 1380
x_genre = 1650
header_y = 215

# FUNCTIONS

def scaleBook(book):
    book = pygame.transform.scale(book,(40, 45))
    return book

def renderAllAuthors(line_height, height):

    all_authors_flat = [element for tuple_item in processed_text for element in tuple_item]

    for author in all_authors_flat:
        book_info = font.render(f'{author}',True, (0, 0, 0))
        screen.blit(book_info, (x_author, height))
        height += line_height

def renderQueryTitleBook(height):
    all_book_titles_flat = [element for tuple_item in processed_text_book_title for element in tuple_item]
    if len(all_book_titles_flat) == 0:
        return

    id = font.render(str(all_book_titles_flat[0]),True,(0,0,0))
    isbn = font.render(str(all_book_titles_flat[1]),True,(0,0,0))
    title = font.render(str(all_book_titles_flat[2]),True,(0,0,0))
    author = font.render(str(all_book_titles_flat[3]),True,(0,0,0))
    pages = font.render(str(all_book_titles_flat[4]),True,(0,0,0))
    edition_date = font.render(str(all_book_titles_flat[5]),True,(0,0,0))
    editorial = font.render(str(all_book_titles_flat[6]),True,(0,0,0))
    genre = font.render(str(all_book_titles_flat[7]),True,(0,0,0))
    screen.blit(id,(x_id,height))
    screen.blit(isbn,(x_isbn,height))
    screen.blit(title,(x_title,height))
    screen.blit(author,(x_author,height))
    screen.blit(pages,(x_pages,height))
    screen.blit(edition_date,(x_editiondate,height))
    screen.blit(editorial,(x_editorial,height))
    screen.blit(genre,(x_genre,height))

def renderListEverything(height):
    local_height = height
    all_list_everything_flat = [element for tuple_item in processed_text_list_everything for element in tuple_item]
    if len(all_list_everything_flat) == 0:
        return

    for index, book in enumerate(processed_text_list_everything):
        book_id, book_isbn,book_title, book_author, book_pages, book_edition_date, book_editorial, book_genre = book
        id = font.render(str(book_id), True, (0, 0, 0))
        isbn = font.render(str(book_isbn), True, (0, 0, 0))
        title = font.render(str(book_title), True, (0, 0, 0))
        author = font.render(str(book_author), True, (0, 0, 0))
        pages = font.render(str(book_pages), True, (0, 0, 0))
        edition_date = font.render(str(book_edition_date), True, (0, 0, 0))
        editorial = font.render(str(book_editorial), True, (0, 0, 0))
        genre = font.render(str(book_genre), True, (0, 0, 0))
        screen.blit(id, (x_id, local_height))
        screen.blit(isbn, (x_isbn, local_height))
        screen.blit(title, (x_title, local_height))
        screen.blit(author, (x_author, local_height))
        screen.blit(pages, (x_pages, local_height))
        screen.blit(edition_date, (x_editiondate, local_height))
        screen.blit(editorial, (x_editorial, local_height))
        screen.blit(genre, (x_genre, local_height))
        local_height += line_height
def processInput(text):
    global processed_text,processed_text_book_title, processed_text_list_everything
    processed_text = []
    processed_text_book_title = []
    processed_text_list_everything = []
    split_text = text.split('-')
    action = split_text[0]

    # if action == 'A':
    #         addBook(conn)
#     elif action == 'D':
#         deleteBook(conn)
    if action == 'L':
         processed_text_list_everything = listEverything(conn)
    elif action == 'QT':
        book_info = split_text[1]
        processed_text_book_title = queryTitleBook(conn,book_info)

#     elif action == 'M':
#         modifyBook(conn)
    elif action == 'LAA':
        processed_text = listAllAuthors(conn)
#     elif action == 'LT':
#         listBookTitles(conn)
#     elif action == 'LG':
#         listGenre(conn)
#     elif action == 'LA':
#         listAuthor(conn)
#     elif action == 'LE':
#         listEditorial(conn)
#     elif action == 'LEY':
#         listEditorialYears(conn)
#     elif action == 'LY':
#         listAYear(conn)
#     elif action == 'WT':
#         listWordInTitle(conn)

# Set up 
font = pygame.font.Font('font/Alkhemikal.ttf', 28)
text = ""

running = True

# IMAGES ------------------------------------------------------------------------------------------------------------------------------------
# Base
background = pygame.image.load('graphics/base/background.png')
background = pygame.transform.scale(background,(1920,1080))
background_rect = background.get_rect(center=(960, 540))

welcome = pygame.image.load('graphics/base/welcome.png')
welcome_rect = welcome.get_rect(center = (960,120))

# Books
    # Images
book_random1 = scaleBook(pygame.image.load('graphics/books/random1.png'))

book_random2 = pygame.image.load('graphics/books/random1.png')
book_random3 = pygame.image.load('graphics/books/random1.png')
book_random4 = pygame.image.load('graphics/books/random1.png')
book_random5 = pygame.image.load('graphics/books/random1.png')

    # Rectangles
book1_rect = book_random1.get_rect(center = (1620,270))

# GAME --------------------------------------------------------------------------------------------------------------------------------------

while running:

    # IMAGES
    screen.blit(background,background_rect)
    
    shelves = pygame.image.load('graphics/base/shelves.png')
    shelves_rect = shelves.get_rect(center = (960, 540))
    screen.blit(shelves,shelves_rect)

    input = pygame.image.load('graphics/base/input.png')
    input_rect = input.get_rect(topleft = (140, 920))
    screen.blit(input,input_rect)

    book1_rect = book_random1.get_rect(center = (1760,298))

    screen.blit(welcome,welcome_rect)
    screen.blit(book_random1,book1_rect)

    # TEXT
    book_header_id = font.render('ID',True, (0, 0, 0))
    book_header_isbn = font.render('ISBN',True, (0, 0, 0))
    book_header_title = font.render('TITLE',True, (0, 0, 0))
    book_header_author = font.render('AUTHOR',True, (0, 0, 0))
    book_header_pages = font.render('PAGES',True, (0, 0, 0))
    book_header_editiondate = font.render('EDITION_DATE ',True, (0, 0, 0))
    book_header_editorial = font.render('EDITORIAL',True, (0, 0, 0))
    book_header_genre = font.render('GENRE',True, (0, 0, 0))
    screen.blit(book_header_id, (x_id, header_y))
    screen.blit(book_header_isbn, (x_isbn, header_y))
    screen.blit(book_header_title, (x_title, header_y))
    screen.blit(book_header_author, (x_author, header_y))
    screen.blit(book_header_pages, (x_pages, header_y))
    screen.blit(book_header_editiondate, (x_editiondate, header_y))
    screen.blit(book_header_editorial, (x_editorial, header_y))
    screen.blit(book_header_genre, (x_genre, header_y))

    # INPUT
    text_surface = font.render(text, True, (255, 255, 220))
    screen.blit(text_surface, (210, 950))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            elif event.key == pygame.K_RETURN:
                text_copy = str(text)
                text = ""
                
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RETURN:                
                processInput(text_copy)
        
    renderAllAuthors(line_height, height)
    renderQueryTitleBook(height)
    renderListEverything(height)
        # processed_text = text.render(processed_text,True,(0,0,0))
        # screen.blit(processed_text,)

    # Update the display
    pygame.display.flip()
