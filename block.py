class Block:
    x_pos: int
    y_pos: int
    length: int
    left_wall: bool
    right_wall: bool
    up_wall: bool
    down_wall: bool
    visited: bool

    def __init__(self, x_pos=0,y_pos=0,length=50,left_wall=0,right_wall=0,up_wall=0,down_wall=0,visited=0):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.length = length
        self.left_wall = left_wall
        self.right_wall = right_wall
        self.up_wall = up_wall
        self.down_wall = down_wall
        self.visited = visited


    def buildBlock(self):
        finished = False
        print("begin\n")
        while not finished:
            user_input = input()
            self.changeBlock(user_input)
            if user_input == 'q':
                finished = True
        
        return self

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
        if key_press == 1:
            self.up_wall = not self.up_wall
        elif key_press == 2:
            self.down_wall = not self.down_wall
        elif key_press == 3:
            self.left_wall = not self.left_wall
        elif key_press == 4:
            self.right_wall = not self.right_wall
        return
    
    def isLegalMove(self,key_press):
        if key_press == "UP":
            return not self.up_wall
        elif key_press == "DOWN":
            return not self.down_wall
        elif key_press == "LEFT":
            return not self.left_wall
        elif key_press == "RIGHT":
            return not self.right_wall
        return

    def visit(self):
        self.visited = False

    def toString(self):
        return str(self.x_pos) + ',' + str(self.y_pos) + ',' + str(self.length) + ',' + str(int(self.left_wall)) + ',' + str(int(self.right_wall)) + ',' + str(int(self.up_wall)) + ',' + str(int(self.down_wall)) + ',' + str(int(self.visited))