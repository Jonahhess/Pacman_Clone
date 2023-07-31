from __future__ import annotations

import pygame

class Character:
    x_pos: int
    y_pos: int
    speed : int
    direction: str
    width: int
    height: int
    name: str
    image: pygame.Surface

    def __init__(self,x_pos,y_pos, width=30, height=30):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.speed = 5

    def setImage(self):
        address = "assets/" + self.name + '/' + self.name + '_' + self.direction.lower() + ".png"
        target = pygame.image.load(address)
        target = pygame.transform.scale(target, (self.width, self.height))   
        return target

    def collision(self,enemy:Character):
        x_difference = abs(self.x_pos - enemy.x_pos)
        y_difference = abs(self.y_pos - enemy.y_pos)
        
        if x_difference < 20 and y_difference < 20:
            return True
        return False

    def move(self):
        if self.direction == "UP":
            self.y_pos -= self.speed
        elif self.direction == "DOWN":
            self.y_pos += self.speed
        elif self.direction == "LEFT":
            self.x_pos -= self.speed
        elif self.direction == "RIGHT":
            self.x_pos += self.speed

        return
    
    def chooseDirection(self,key_press):
        if key_press in ["UP", "DOWN", "LEFT", "RIGHT"] and key_press != self.direction:
            self.direction = key_press
            return True
        return False
    
    def getLocation(self):
        return self.x_pos, self.y_pos

class Pacman(Character):
    def __init__(self, x_pos, y_pos):
        super().__init__(x_pos, y_pos)
        self.direction = "RIGHT"
        self.name = "pacman"
        self.image = self.setImage()

class Ghost(Character):
    def __init__(self, x_pos, y_pos,name):
        super().__init__(x_pos, y_pos)
        self.direction = "UP"
        self.name = name
        self.image = self.setImage()