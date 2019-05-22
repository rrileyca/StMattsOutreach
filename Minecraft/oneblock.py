import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, 1)

#mc.setBlock(x+1, y, z, block.GOLD_ORE.id)
