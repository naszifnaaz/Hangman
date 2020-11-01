#Hangman game made using Python and pygame
import pygame

#Setting up display
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption(("Hangman"))

#Button variables
radius = 20
gap = 15
letters = []    #triplet with x,y co ordinates and letter ascii value
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
A =65

for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i)])


#Draw function
def draw():
    win.fill(white)

    #draw buttons
    for letter in letters:
        x, y, char = letter
        pygame.draw.circle(win, black, (x,y), radius, 3)
        text = LETTER_FONT.render(char,1,black)
        win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    win.blit(images[hangman_state], (150, 100))
    pygame.display.update()


#Fonts
LETTER_FONT = pygame.font.SysFont('comicsans',40)


#Loading assets
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)
print(images)

#Game variables
hangman_state = 6

#Colors
white = (255,255,255)
black = (0,0,0)

#Basic game loop
FPS = 60
clock = pygame.time.Clock()
run = True

while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)
pygame.quit()           
