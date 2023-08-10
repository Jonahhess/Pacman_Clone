from pygame import Surface,display,font
from game import Game
import character

class Screen:
    screen: Surface
    width: int
    height: int
    font:font
    game: Game

    def __init__(self,game,width,height,font=font.Font(None,36),title="Pacman Clone") -> None:
        self.game = game
        self.screen = display.set_mode((width, height))
        self.font = font
        display.set_caption(title)

    def draw(self,characters:character.Character):
        for c in characters:
            self.screen.blit(c.image,c.getLocation())

    def display_message(self, message, color=(255, 255, 255)):
        # Render the message on the screen
        text_surface = font.render(message, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)
        self.update()
        
    def update():
        display.flip()
        display.update()