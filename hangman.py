#Hangman game made using Python and pygame
import pygame

#Setting up display
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption(("Hangman"))

#Loading assets
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
print(images)

#Game variables
hangman_state = 0

#Color codes
white = (255,255,255)
black = (0,0,0)

#Basic game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    win.fill(white)
    win.blit(images[hangman_state], (150, 100))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()           
