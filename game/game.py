import pygame

# pygame innit
pygame.init()
clock = pygame.time.Clock()

# the screen is this big
screen = pygame.display.set_mode((450, 800)) 
colon = (0,255,0)
screen.fill(colon)

# Set the caption of the screen 
pygame.display.set_caption('Gwyneth Paltrow')

# Gayme
scroll_speed = 1

# class Ground():
     # def __init__(self,x,y):
          

def quit_game():
    for event in pygame.event.get(): 
        
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

def main():
    # game is run
    run = True

    # game loop 
    while run: 
        quit_game()
        screen.fill(colon)
        clock.tick(60)
        pygame.display.update()

main()