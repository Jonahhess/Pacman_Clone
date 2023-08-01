import pygame, sys
import block,character,level

# Constants for the game window size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ELEMENT_WIDTH, ELEMENT_HEIGHT = 30,30
BACKGROUND_COLOR = (0, 0, 0)
background_image = pygame.image.load("assets/background.png")

class Game:
    score: int
    characters: list[character.Character]
    screen: pygame.Surface

    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pacman Clone")
        font = pygame.font.Font(None,36)

        # Render the message on the screen
        message = "Welcome to my game!"
        text_surface = font.render(message, True, (255, 255, 255))  # (0, 0, 0) is black color
        text_rect = text_surface.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)
        pygame.display.flip()
        self.play()

    def play(self):
        clock = pygame.time.Clock()
        clock.tick(60)

        pacman_x, pacman_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
        ghost_x, ghost_y = SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4

        pacman = character.Pacman(pacman_x,pacman_y)
        self.characters = []
        self.characters.append(character.Ghost(ghost_x,ghost_y,"red"))
        self.characters.append(character.Ghost(ghost_x + 50 ,ghost_y,"orange"))
        self.characters.append(character.Ghost(ghost_x + 100,ghost_y,"blue"))
        self.characters.append(character.Ghost(ghost_x - 50,ghost_y,"pink"))
        
        for c in self.characters:
            self.draw(c)
        
        
        while True:
            self.screen.blit(background_image, (0, 0))   
            self.draw(pacman)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if pacman.chooseDirection("UP"):
                            pacman.image = pacman.setImage()
                    elif event.key == pygame.K_DOWN:
                        if pacman.chooseDirection("DOWN"):
                            pacman.image = pacman.setImage()
                    elif event.key == pygame.K_LEFT:
                        if pacman.chooseDirection("LEFT"):
                            pacman.image = pacman.setImage()
                    elif event.key == pygame.K_RIGHT:
                        if pacman.chooseDirection("RIGHT"):
                            pacman.image = pacman.setImage()

                # update screen
                pacman.move()            
                pygame.display.flip()
                pygame.display.update()

    def draw(self,character:character.Character):
        self.screen.blit(character.image,character.getLocation())
        return

    def drawBlock(self,block:block.Block):
        block_x = block.x_pos
        block_y = block.y_pos
        block_length = block.length

        left_wall = block.left_wall
        right_wall = block.right_wall
        up_wall = block.up_wall
        down_wall = block.down_wall

        if left_wall:
            pygame.draw.line(self.screen, (0,0,255), (block_x,block_y), (block_x,block_y + block_length))
        if right_wall:
            pygame.draw.line(self.screen, (0,0,255), (block_x + block_length,block_y), (block_x,block_y + block_length))
        if up_wall:
            pygame.draw.line(self.screen, (0,0,255), (block_x,block_y), (block_x  + block.length, block_y))
        if down_wall:
            pygame.draw.line(self.screen, (0,0,255), (block_x,block_y + block.length), (block_x + block_length ,block_y ))

        pygame.display.flip()

