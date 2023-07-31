from __future__ import annotations
from pygame import Surface

class Character:
    x_pos: int
    y_pos: int
    speed : int
    direction: str
    width: int
    height: int
    current_sprite: Surface

    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def collision(self,enemy:Character):
        x_difference = abs(self.x_pos - enemy.x_pos)
        y_difference = abs(self.y_pos - enemy.y_pos)
        
        if x_difference < 20 and y_difference < 20:
            return True
        return False

    def move(self, key_press=None):
        self.changeDirection(key_press)

        if self.direction == "UP":
            pacman_y -= self.speed
        elif self.direction == "DOWN":
            pacman_y += self.speed
        elif self.direction == "LEFT":
            pacman_x -= self.speed
        elif self.direction == "RIGHT":
            pacman_x += self.speed

        return
    
    def chooseDirection(self,key_press):
        if key_press in ["UP", "DOWN", "LEFT", "RIGHT"] and key_press != self.direction:
            self.direction = key_press
            return True
        return False
    
    def getLocation(self):
        return self.x_pos, self.y_pos

class Pacman(Character):
    pass

class Ghost(Character):
    pass