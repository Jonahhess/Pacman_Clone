from pygame import init, time, event, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT
import character,level,screen,sys

# Constants for the game window size and colors
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
ELEMENT_WIDTH, ELEMENT_HEIGHT = 30,30
BACKGROUND_COLOR = (0, 0, 0)
PACMAN_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
GHOST_POS = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 4)

class Game:
    score: int
    characters: list[character.Character]
    game_screen: screen.Screen
    cur_level: level

    def __init__(self,mode=0) -> None:
        init()
        self.game_screen = screen.Screen(SCREEN_WIDTH,SCREEN_HEIGHT)
        self.game_screen.display_message("Welcome to my game!")
        if mode == 0:
            self.play()
        elif mode == 1:
            self.cur_level = self.build_level()
            self.play()

    def play(self):
        clock = time.Clock()
        clock.tick(60)

        self.characters = [character.Pacman(PACMAN_POS)]
        self.characters += [character.Ghost(GHOST_POS,name) for name in ("red","orange","blue","pink")]
        
        self.game_screen.draw(self.characters)
        
        while True:  
            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                    sys.exit()
                elif ev.type == KEYDOWN:
                    if ev.key == K_UP or K_DOWN or K_LEFT or K_RIGHT:
                        self.characters[0].chooseDirection(ev.key)

                # move characters
                for c in self.characters:
                    if self.checkMove(c,self.game_screen):
                        c.move()
                
                # update screen        
                self.game_screen.draw(self.characters)
                self.game_screen.update()

    def build_level(self):
        return level.Level(self.game_screen,new_level=True)
    
    def checkMove(self,c:character.Character,game_screen:screen.Screen) -> bool:
        c_dir = c.direction
        x_max = game_screen.width
        y_max = game_screen.height
        change = -1
        if c_dir == K_UP:
            change = c.y_pos - c.speed
            if change > 0 and change < y_max:
                return True
        elif c_dir == K_DOWN:
            change = c.y_pos + c.speed
            if change > 0 and change < y_max:
                return True
        elif c_dir == K_LEFT:
            change = c.x_pos - c.speed
            if change > 0 and change < x_max:
                return True
        elif c_dir == K_RIGHT:
            change = c.x_pos + c.speed
            if change > 0 and change < x_max:
                return True
        


