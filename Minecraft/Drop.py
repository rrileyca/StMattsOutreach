import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()

playerPos = mc.player.getPos()
mc.player.setPos(playerPos.x, playerPos.y + 50, playerPos.z)
mc.postToChat("Dont look down!")
time.sleep(8)
