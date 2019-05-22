from mcpi import minecraft, block
import time
 
def createTower(numberOfBlocks):
    #Let's wait 1 second
    time.sleep(1)
    
    #Retrieve the X,Y,Z coordinates of the player
    pos=mc.player.getPos()
 
    #Create a tower 5 blocks away from the player
    for i in range (0, numberOfBlocks):
        mc.setBlock(pos.x + 5, pos.y + i, pos.z, block.STONE)
 
#Main Program Starts Here:
createTower(10)
