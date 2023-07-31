class Block:
    left_wall: bool
    right_wall: bool
    up_wall: bool
    down_wall: bool
    visited: bool

    def buildBlock(self):
        finished = False
        user_input = input("To finish press q")
        if user_input == "q":
            finished = True

        user_input = input("Build block: use I,J,K,L keys to add/remove walls")
        while not finished:
            self.changeBlock(user_input)
            user_input = input()
        
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
        if key_press == "UP":
            up_wall = not up_wall
        elif key_press == "DOWN":
            down_wall = not down_wall
        elif key_press == "LEFT":
            left_wall = not left_wall
        elif key_press == "RIGHT":
            right_wall = not right_wall
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