from mcpi import minecraft, block
import time
 
def createTower(numberOfBlocks):
    #Let's wait 1 second
    time.sleep(1)
    
    #Retrieve the X,Y,Z coordinates of the player
    pos=mc.player.getPos()
 
    #Create a tower 5 blocks away from the player
    mc.setBlocks(pos.x + 5, pos.y, pos.z, pos.x + 5, pos.y + numberOfBlocks, pos.z, block.STONE)
 
#Main Program Starts Here:
createTower(10)
