from __future__ import annotations

from pygame import Surface,image,transform, K_UP, K_DOWN, K_LEFT, K_RIGHT

direction_to_string = {K_UP: "up", K_DOWN: "down", K_LEFT: "left", K_RIGHT: "right"}

class Character:
    x_pos: int
    y_pos: int
    speed : int
    direction: int
    width: int
    height: int
    name: str
    image: Surface

    def __init__(self,pos:tuple, width=30, height=30, speed=5):
        self.width = width
        self.height = height
        
        try:
            self.x_pos = pos[0]
            self.y_pos = pos[1]
        except ValueError:
            self.x_pos = width // 2
            self.y_pos = height // 2

        self.speed = speed

    def setImage(self):
        address = "assets/" + self.name + '/' + self.name + '_' + direction_to_string[self.direction] + ".png"
        target = image.load(address)
        target = transform.scale(target, (self.width, self.height))   
        return target

    def collision(self,enemy:Character):
        x_difference = abs(self.x_pos - enemy.x_pos)
        y_difference = abs(self.y_pos - enemy.y_pos)
        
        if x_difference < 20 and y_difference < 20:
            return True
        return False

    def move(self):
        if self.direction == K_UP:
            self.y_pos -= self.speed
        elif self.direction == K_DOWN:
            self.y_pos += self.speed
        elif self.direction == K_LEFT:
            self.x_pos -= self.speed
        elif self.direction == K_RIGHT:
            self.x_pos += self.speed
        return
    
    def chooseDirection(self,key_press) -> bool:
        if key_press in [K_UP, K_DOWN, K_LEFT, K_RIGHT] and key_press != self.direction:
            self.direction = key_press
            self.image = self.setImage()
            return True
        return False
    
    def getLocation(self):
        return self.x_pos, self.y_pos

class Pacman(Character):
    def __init__(self, pos):
        super().__init__(pos)
        self.direction = K_RIGHT
        self.name = "pacman"
        self.image = self.setImage()

class Ghost(Character):
    def __init__(self, pos,name,direction=K_UP):
        super().__init__(pos)
        self.direction = direction
        self.name = name
        self.image = self.setImage()