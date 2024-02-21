import pygame

# pygame innit
pygame.init()
clock = pygame.time.Clock()


# Set the caption of the screen 
pygame.display.set_caption('Gwyneth Paltrow')

# the screen is this big
screen = pygame.display.set_mode((450, 800)) 
colon = (0,255,0)
screen.fill(colon)

# Gayme
scroll_speed = 1
bird_start_pos = (80,350)

# ground
ground = pygame.Rect(0,700,450,100)

# bird

class Bird(pygame.Rect):
     def __init__(self):
          self.rect.center = bird_start_pos
          self.rect.fill = (255,0,255)


# class Ground():
#     ground = pygame.Rect(0,700,450,100)
#     def __init__():
#     def update():
        

def quit_game():
    for event in pygame.event.get(): 
        
            # Check for QUIT event       
            if event.type == pygame.QUIT: 
                pygame.quit()
                exit()

def main():

    #bird
    bird = pygame.Rect(0,0,30,20)
    #bird.add(Bird())
    
    # game is run
    run = True

    # game loop 
    while run: 
        # Quit
        quit_game()

        # Reset screen
        screen.fill(colon)

        # draw the ground
        pygame.draw.rect(screen,(255,0,255),ground)

        # draw bird
        #bird.draw(screen)

        clock.tick(60)
        pygame.display.update()

main()