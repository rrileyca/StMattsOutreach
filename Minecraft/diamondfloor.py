import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
playerTilePos = mc.player.getPos()
mc.setBlocks(playerTilePos.x - 25, playerTilePos.y - 1, playerTilePos.z - 25, playerTilePos.x + 25, playerTilePos.y -1, playerTilePos.z + 25, block.DIAMOND_BLOCK)
mc.postToChat("Now thats a big diamond floor!")
