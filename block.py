from pygame import draw, K_UP, K_DOWN, K_LEFT, K_RIGHT
class Block:
    x_pos: int
    y_pos: int
    length: int
    left_wall: bool
    right_wall: bool
    up_wall: bool
    down_wall: bool
    visited: bool

    def __init__(self, x_pos=0,y_pos=0,length=250,left_wall=False,right_wall=False,up_wall=False,down_wall=False,visited=False):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.up_wall = up_wall
        self.down_wall = down_wall
        self.visited = visited

    def drawBlock(self,screen):
        if self.left_wall:
            draw.line(screen, (0,0,255), (self.x_pos,self.y_pos), (self.x_pos,self.y_pos + self.length))
        if self.right_wall:
            draw.line(screen, (0,0,255), (self.x_pos + self.length,self.y_pos), (self.x_pos,self.y_pos + self.length))
        if self.up_wall:
            draw.line(screen, (0,0,255), (self.x_pos,self.y_pos), (self.x_pos  + self.length, self.y_pos))
        if self.down_wall:
            draw.line(screen, (0,255,255), (self.x_pos,self.y_pos + self.length), (self.x_pos + self.length ,self.y_pos ))

    def exportBlock(self,output_file):
        with open(output_file, 'w') as writer:
            for var in vars(self):
                writer.write(str(int(var)))
                writer.write('\t')
        return

    def importBlock(self,input_file):
        with open(input_file, 'r') as reader:
            variables = reader.readline().split('\t')
            for count, value in enumerate(variables):
                setattr(self,value,variables[count])
        return

    def changeBlock(self,key_press):
        if key_press == K_UP:
            self.up_wall = not self.up_wall
        elif key_press == K_DOWN:
            self.down_wall = not self.down_wall
        elif key_press == K_LEFT:
            self.left_wall = not self.left_wall
        elif key_press == K_RIGHT:
            self.right_wall = not self.right_wall
        return
    
    def isLegalMove(self,key_press):
        if key_press == K_UP:
            return not self.up_wall
        elif key_press == K_DOWN:
            return not self.down_wall
        elif key_press == K_LEFT:
            return not self.left_wall
        elif key_press == K_RIGHT:
            return not self.right_wall
        return

    def toString(self):
        return str(self.x_pos) + ',' + str(self.y_pos) + ',' + str(self.length) + ',' + str(int(self.left_wall)) + ',' + str(int(self.right_wall)) + ',' + str(int(self.up_wall)) + ',' + str(int(self.down_wall)) + ',' + str(int(self.visited))