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
    book = pygame.transform.scale(book,(60, 90))
    return book

# Set up 
font = pygame.font.Font('font/Alkhemikal.ttf', 36)
text = ""

running = True

# IMAGES ------------------------------------------------------------------------------------------------------------------------------------
# Base
background = pygame.image.load('graphics/base/background.png')
background = pygame.transform.scale(background,(1920,1080))
background_rect = background.get_rect(center=(960, 540))

welcome = pygame.image.load('graphics/base/welcome.png')
welcome_rect = welcome.get_rect(center = (960,150))

# Books
    # Images
book_random1 = scaleBook(pygame.image.load('graphics/books/random1.png'))

book_random2 = pygame.image.load('graphics/books/random1.png')
book_random3 = pygame.image.load('graphics/books/random1.png')
book_random4 = pygame.image.load('graphics/books/random1.png')
book_random5 = pygame.image.load('graphics/books/random1.png')

    # Rectangles
book1_rect = book_random1.get_rect(center = (1700,400))
 

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
    screen.blit(welcome,welcome_rect)

    pygame.draw.rect(screen, (255, 0, 0), (200, 250, 1600, 600))
    pygame.draw.rect(screen, (0, 0, 255), (250, 300, 1400, 60))
    pygame.draw.rect(screen, (0, 255, 255), (200, 900, 1600, 50))

    screen.blit(book_random1,book1_rect)

    # INPUT
    text_surface = font.render(text, True, (0, 0, 0))
    screen.blit(text_surface, (210, 908))

    # Update the display
    pygame.display.flip()
