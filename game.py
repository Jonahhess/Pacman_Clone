from pygame import *
import block,character,level,screen,sys

# Constants for the game window size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ELEMENT_WIDTH, ELEMENT_HEIGHT = 30,30
BACKGROUND_COLOR = (0, 0, 0)
PACMAN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
GHOST_POS = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

class Game:
    score: int
    characters: list[character.Character]
    game_screen: screen

    def __init__(self) -> None:
        init()
        self.game_screen = screen.Screen(self,SCREEN_WIDTH,SCREEN_HEIGHT)
        self.game_screen.display_message("Welcome to my game!")
        self.play()

    def play(self):
        clock = time.Clock()
        clock.tick(60)

        self.characters = [character.Pacman(PACMAN_POS)]
        self.characters += [character.Ghost(GHOST_POS,name) for name in ("red","orange","blue","pink")]
        
        for c in self.characters:
            self.draw(c)
        
        while True:  
            for event in event.get():
                if event.type == QUIT:
                    quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_UP or K_DOWN or K_LEFT or K_RIGHT:
                        self.characters[0].chooseDirection(event.key)

                
                # move characters
                for c in self.characters:
                    c.move()
                
                # update screen        
                self.game_screen.update()
                self.game_screen.draw(self.characters)

