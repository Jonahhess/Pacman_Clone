from pygame import Surface,display,font
import character

class Screen:
    screen: Surface
    width: int
    height: int
    my_font:font

    def __init__(self,width:int,height:int,cur_font=None,title="Pacman Clone") -> None:
        self.screen = display.set_mode((width, height))
        self.width = width
        self.height = height

        if cur_font == None:
            self.my_font = font.Font(None,36)
        else:
            self.my_font = cur_font
        display.set_caption(title)

    def draw(self,characters:list[character.Character]):
        for c in characters:
            self.screen.blit(c.image,c.getLocation())
            self.update()

    def display_message(self, message, color=(255, 255, 255)):
        # Render the message on the screen
        text_surface = self.my_font.render(message, True, color)
        text_rect = text_surface.get_rect()
        text_rect.center = (self.width // 2, self.height // 2)
        # Blit the text surface onto the screen
        self.screen.blit(text_surface, text_rect)
        self.update()
        
    def update(self):
        display.flip()
        display.update()