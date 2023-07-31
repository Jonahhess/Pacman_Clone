import pygame
import sys

from player import *

# Constants for the game window size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ELEMENT_WIDTH, ELEMENT_HEIGHT = 30,30
BACKGROUND_COLOR = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman Clone")


    # Load Pacman and Ghost sprites and other assets here
    background_image = pygame.image.load("assets/background.png")
    pacman_image = pygame.image.load("assets/pacman/pacman_right.png")
    ghost_image = pygame.image.load("assets/red/red_right.png")
    pacman_image = pygame.transform.scale(pacman_image, (ELEMENT_WIDTH, ELEMENT_HEIGHT))
    ghost_image = pygame.transform.scale(ghost_image, (ELEMENT_WIDTH, ELEMENT_HEIGHT))
    pacman_x, pacman_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    ghost_x, ghost_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4
    
    pacman = Pacman(pacman_x,pacman_y)
    red = Ghost(ghost_x,ghost_y)

    clock = pygame.time.Clock()

    while True:
        screen.blit(background_image, (0, 0))   
        screen.blit(pacman_image, (pacman_x, pacman_y))
        screen.blit(ghost_image, (ghost_x, ghost_y))

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pacman_direction = "UP"
                elif event.key == pygame.K_DOWN:
                    pacman_direction = "DOWN"
                elif event.key == pygame.K_LEFT:
                    pacman_direction = "LEFT"
                elif event.key == pygame.K_RIGHT:
                    pacman_direction = "RIGHT"

        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)


def collision_detection(screen,a_x,a_y,b_x,b_y):
    x_difference = abs(a_x - b_x)
    y_difference = abs(a_y - b_y)
    #print(x_difference,y_difference)

    if x_difference < 20 and y_difference < 20:
        font = pygame.font.SysFont('arial', 36)  # None means default font, 36 is the font size
        message = "Collision Detected!"

        # Render the message on the screen
        text_surface = font.render(message, True, (0, 0, 0))  # (0, 0, 0) is black color
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

        # Blit the text surface onto the screen
        screen.blit(text_surface, text_rect)
        return
    else:
        return


if __name__ == "__main__":
    main()

