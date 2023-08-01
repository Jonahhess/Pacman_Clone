import game
import level
import block

def main():
    lev = level.Level(3,3)
    blo = block.Block()
    blo.buildBlock()
    print(blo.toString())

if __name__ == "__main__":
    main()


    #TODO: Create Level, implement Collision, AI, fix movement issues