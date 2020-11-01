#Hangman game made using Python and pygame
import pygame
import math

#Setting up display
pygame.init()
width, height = 800, 500
win = pygame.display.set_mode((width,height))
pygame.display.set_caption(("Hangman"))

#Button variables
radius = 20
gap = 15
letters = []    #quadruplet with x,y co ordinates, letter ascii value and boolean variable
startx = round((width - (radius * 2 + gap) * 13) / 2)
starty = 400
A =65

for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap) * (i % 13))
    y = starty + ((i // 13) * (gap + radius * 2))
    letters.append([x, y, chr(A + i), True])


#Draw function
def draw():
    win.fill(WHITE)

    #draw buttons
    for letter in letters:
        x, y, char, visible = letter
        if visible:
            pygame.draw.circle(win, BLACK, (x,y), radius, 3)
            text = LETTER_FONT.render(char,1,BLACK)
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
WHITE = (255,255,255)
BLACK = (0,0,0)

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
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, char, visible = letter
                #Adding collision detection
                if visible:
                    dis = math.sqrt((x - mouse_x) ** 2 + (y - mouse_y) ** 2)
                    if dis < radius:
                        letter[3] = False
            

pygame.quit()           
