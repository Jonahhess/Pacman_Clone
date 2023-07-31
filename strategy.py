from abc import abstractmethod
from character import Pacman, Ghost
class Strategy:
    
    @abstractmethod
    def move(pacman:Pacman,ghost:Ghost) -> str:
        pass

class Run(Strategy):
    def move(pacman:Pacman,ghost:Ghost) -> str:
        move = ""
        for i in ["UP", "DOWN", "LEFT", "RIGHT"]:
            pass
        return move