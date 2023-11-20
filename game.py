import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Library")

# FUNCTIONS

def scaleBook(book):
    book = pygame.transform.scale(book,(40, 45))
    return book

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
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()
            if event.key == pygame.K_RETURN:
                print("Entered text:", text)
                text = ""
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode

    # IMAGES
    screen.blit(background,background_rect)
    
    shelves = pygame.image.load('graphics/base/shelves.png')
    shelves_rect = shelves.get_rect(center = (960, 540))
    screen.blit(shelves,shelves_rect)

    input = pygame.image.load('graphics/base/input.png')
    input_rect = input.get_rect(topleft = (140, 920))
    screen.blit(input,input_rect)

    book1_rect = book_random1.get_rect(center = (1760,320))

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
    screen.blit(book_header_id, (160, 215))
    screen.blit(book_header_isbn, (200, 215))
    screen.blit(book_header_title, (400, 215))
    screen.blit(book_header_author, (820, 215))
    screen.blit(book_header_pages, (1050, 215))
    screen.blit(book_header_editiondate, (1150, 215))
    screen.blit(book_header_editorial, (1380, 215))
    screen.blit(book_header_genre, (1650, 215))

    book_info = font.render('12  ISBN                Harry Potter & the Secret Chamber       J.K. Rowling             352       2000-06-02     Scholastic                    Fantasy',True, (0, 0, 0))
    screen.blit(book_info, (160, 300))
    screen.blit(book_info, (160, 355))

    # INPUT
    text_surface = font.render(text, True, (255, 255, 220))
    screen.blit(text_surface, (210, 950))

    # Update the display
    pygame.display.flip()
