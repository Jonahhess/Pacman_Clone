import pygame
import sys

# Constants for the game window size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pacman Clone")

    # Load Pacman and Ghost sprites and other assets here
    background_image = pygame.image.load("assets/background.png")
    pacman_image = pygame.image.load("assets/pacman.png")
    ghost_image = pygame.image.load("assets/ghost.png")

    # Desired width and height for Pacman and Ghost sprites
    pacman_width, pacman_height = 30, 30
    ghost_width, ghost_height = 30, 30
    background_width, background_height = 800,600

    pacman_image = pygame.transform.scale(pacman_image, (pacman_width, pacman_height))
    ghost_image = pygame.transform.scale(ghost_image, (ghost_width, ghost_height))
    background_image = pygame.transform.scale(background_image, (background_width, background_height))

    pacman_x, pacman_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    ghost_x, ghost_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4

    pacman_direction = "RIGHT"
    pacman_speed = 5

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

        # Update Pacman's position and check for collisions here
            if pacman_direction == "UP":
                pacman_y -= pacman_speed
            elif pacman_direction == "DOWN":
                pacman_y += pacman_speed
            elif pacman_direction == "LEFT":
                pacman_x -= pacman_speed
            elif pacman_direction == "RIGHT":
                pacman_x += pacman_speed
                    
        

        # Draw Pacman, Ghosts, pellets, walls, and other game elements here
        pygame.display.flip()

        # Set the frame rate
        clock.tick(60)

if __name__ == "__main__":
    main()