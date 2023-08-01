from block import Block
import json

class Level:
    high_score: int
    width: int
    height: int
    blocks: list

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = [[Block() for x in range(self.width)] for y in range(self.height)] 

    def createNewLevel(self):
        for i in self.blocks:
            for j in i:
                j.buildBlock()

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
            



