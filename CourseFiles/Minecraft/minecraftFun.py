# Full Application Programming Interface (API) Documentation here:
# https://www.stuffaboutcode.com/p/minecraft-api-reference.html

# Import these packages that allow you to play with Minecraft
import mcpi.minecraft as minecraft
import mcpi.block as block

# Create a connection to the Minecraft game
mc = minecraft.Minecraft.create()

# Get the player position, and assign it to 3 variables: "x", "y", and "z"
x, y, z = mc.player.getPos()

# Create a new block at the coordinates given in the first 3 arguments (x,y,z)
# The 4th argument is the block type, which is an integer.
# There is a list of constants in the API document.
mc.setBlock(x+1, y, z, block.Block(1))  # Stone
mc.setBlock(x-1, y, z, block.Block(42)) # Iron
mc.setBlock(x, y, z+1, block.Block(57)) # Diamond
mc.setBlock(x, y, z-1, block.Block(41)) # Gold

# Use for loops!
for b in range(0,5):
	mc.setBlock(x+5, y+b, z, block.Block(b+1))
	
