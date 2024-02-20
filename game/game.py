import pygame

screen = pygame.display.set_mode((1600, 900)) 

# Set the caption of the screen 
pygame.display.set_caption('Gwyneth Paltrow')

# screen is green
colon = (0,255,0)
screen.fill(colon)

# update is game
pygame.display.flip()

# game is run
running = True

# game loop 
while running: 
    
# for loop through the event queue   
    for event in pygame.event.get(): 
      
        # Check for QUIT event       
        if event.type == pygame.QUIT: 
            running = False
