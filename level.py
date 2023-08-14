import json
import screen, block

class Level:
    high_score: int
    width: int
    height: int
    blocks: list[block.Block]
    game_screen: screen

    def __init__(self, width=4, height=8):
        self.width = width
        self.height = height
        self.blocks = [[block.Block() for _ in range(self.width)] for _ in range(self.height)] 

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
        
        self.blocks = [[block.Block() for _ in range(self.width)] for _ in range(self.height)]
        return self

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


