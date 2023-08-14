import json
from block import Block
from pygame import event, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN, QUIT, time
import screen

class Level:
    high_score: int
    width: int
    height: int
    blocks: list
    game_screen: screen

    def __init__(self, width=4, height=8,new_level = False):
        if new_level == False:
            self.width = width
            self.height = height
            self.blocks = [[Block() for _ in range(self.width)] for _ in range(self.height)] 
        else:
            self.createNewLevel()

    def createNewLevel(self):
        self.high_score = 0
        while True:
            try:
                width = int(input("Enter width: "))       
            except ValueError:
                print("Not an integer!")
                continue
            else:
                self.width = width
                break 
        
        while True:
            try:
                height = int(input("Enter height: "))       
            except ValueError:
                print("Not an integer!")
                continue
            else:
                self.height = height
                break
        
        self.blocks = [[Block() for _ in range(self.width)] for _ in range(self.height)]

        #start_building
        clock = time.Clock()
        clock.tick(60)
        i = 0
        cur_block = self.blocks[0]
        
        while i < len(self.blocks): 
            for ev in event.get():
                if ev.type == QUIT:
                    quit()
                elif ev.type == KEYDOWN:
                    if ev.key == K_UP or K_DOWN or K_LEFT or K_RIGHT:
                        cur_block.changeBlock(ev.key)
                    elif ev.key == "n":
                        cur_block.drawBlock(self.game_screen)
                        self.game_screen.update()
                        i = i + 1
                        cur_block = self.blocks[i]


    def importLevel(self,fname):
        with fname as import_level:
           line = import_level.readline()
           pieces = '\t'.split(line)
           self.high_score = pieces[0]
           self.width = pieces[1]
           self.height = pieces[2]
           blocks = '-'.split(pieces[3])

           for block in blocks:
               self.blocks.append()
            
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
        sort_keys=True, indent=4)
            



