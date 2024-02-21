import pygame
import random

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
bird = pygame.Rect(100,350,45,35)

# class Bird(pygame.Rect):
#      def __init__(self):
#           self.rect.center = bird_start_pos
#           self.rect.fill = (255,0,255)


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

    #bird.add(Bird())
    vel = 0
    flap = False

    # game is run
    run = True

    # game loop 
    while run: 

        user_input = pygame.key.get_pressed()

        # Quit
        quit_game()

        # Reset screen
        screen.fill(colon)

        #bird.draw(screen)

        # draw the ground
        pygame.draw.rect(screen,(255,0,255),ground)

        # draw bird
        pygame.draw.rect(screen,(120,0,255),bird)

        if bird.y >= 659:
          bird.y -= bird.y-659
        bird.y += int(vel)
        vel += .5
        if (vel > 6):
             vel = 6
        if vel == 0:
             flap = False

        if user_input[pygame.K_SPACE] == True and not flap and bird.y > 10:
             flap = True
             vel = -8
        
        clock.tick(60)
        pygame.display.update()

main()