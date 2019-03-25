#############################################
################ Challenge 1 ################
#############################################
unicorn.set_pixel(0,0,255,255,255)
unicorn.show() 


#############################################
################ Challenge 2 ################
#############################################
unicorn.set_pixel(0,0,255,255,255)
unicorn.set_pixel(1,0,255,255,255)
unicorn.set_pixel(2,0,255,255,255)
unicorn.set_pixel(3,0,255,255,255)
unicorn.set_pixel(4,0,255,255,255)
unicorn.set_pixel(5,0,255,255,255)
unicorn.set_pixel(6,0,255,255,255)
unicorn.set_pixel(7,0,255,255,255)
unicorn.show() 

#############################################
################ Challenge 3 ################
#############################################
unicorn.set_pixel(0,0,255,255,255)
unicorn.set_pixel(0,1,255,255,255)
unicorn.set_pixel(0,2,255,255,255)
unicorn.set_pixel(0,3,255,255,255)
unicorn.set_pixel(0,4,255,255,255)
unicorn.set_pixel(0,5,255,255,255)
unicorn.set_pixel(0,6,255,255,255)
unicorn.set_pixel(0,7,255,255,255)
unicorn.show() 

#############################################
################ Challenge 4 ################
#############################################
unicorn.set_pixel(0,0,255,255,255)
unicorn.set_pixel(1,1,255,255,255)
unicorn.set_pixel(2,2,255,255,255)
unicorn.set_pixel(3,3,255,255,255)
unicorn.set_pixel(4,4,255,255,255)
unicorn.set_pixel(5,5,255,255,255)
unicorn.set_pixel(6,6,255,255,255)
unicorn.set_pixel(7,7,255,255,255)
unicorn.show() 

#############################################
################ Challenge 5 ################
#############################################
xCoords = [0,1,2,3,4,5,6,7]
yCoords = [0,1,2,3,4,5,6,7]

for x in xCoords:
  for y in yCoords:
    unicorn.set_pixel(x,y,255,255,255)

unicorn.show()

#############################################
################ Challenge 6 ################
#############################################
coords = [0,1,2,3,4,5,6,7]

for n in coords:
  unicorn.set_pixel(n,n,255,255,255)

unicorn.show()

#############################################
################ Challenge 7 ################
#############################################
coords = [0,1,2,3,4,5,6,7]

for n in coords:
  unicorn.set_pixel(n,n,255,255,255)
  unicorn.set_pixel((7 - n),n,255,255,255)

unicorn.show()

#############################################
################ Challenge 8 ################
#############################################
counter = 0
interval = 2
maxTime = 30

while(counter < maxTime):
  print('Time currently at: ' + str(counter)) # A print just to show where we're at
  x = randint(0,7)
  y = randint(0,7)
  unicorn.off()
  unicorn.set_pixel(x,y,255,255,255)
  unicorn.show()
  time.sleep(interval)
  counter += interval

unicorn.off()