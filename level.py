from block import Block

class Level:
    width: int
    height: int
    blocks: list
    high_score: int

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.blocks = [[Block() for x in range(self.width)] for y in range(self.height)] 

    def createNewLevel(self):
        for block in self.blocks:
            block.buildBlock()