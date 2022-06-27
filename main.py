###############################################
# Date: Oct, 29, 2021
# Programmer: Feng Zhang
# Purpose: To create a tkinter animation with 
#          multiple moving objects using lists
###############################################

#Initialize Tkinter 
from tkinter import *
import random
import time 

myInterface = Tk()

screen = Canvas(myInterface, width=800, height=600, background='#2C3845')
screen.pack()


#Variables 
posX = 100
posY = 500
width = 50
height = 325
posx = 500
posy = 350
chainX = posx-30
chainY = posY-70
treeStart = posX+width+width*1.15
x = []
y = []
size = []
triangleDrawingsUp = []
triangleDrawingsDown = []
treeColors = ['#143306', '#42692f', '#375828', '#326718', '#3a791b']
xSpeed = []
ySpeed = []
treeChunks = []
chunkSize = []
chunkPosX = []
chunkPosY = []
leafColors = []
outOfScreenIndexes = []
quadraticMultiplier = []
barkColors = ['#143306', '#3a1c1c', '#8a7362', '#533118', '#754A41', '#5E372E']
barkColor = []
end = False
catPic = PhotoImage(file='cat.png')
rainX = []
rainY = []
rainDrawings = []
rainSpeed = []
rainSize = []
rainIndexes = []
startingText = ['This is bob.','Bob is a lumberjack.', 'Bob is cutting this tree down.', 'Bob will profit from this wood.']
firstTime = True

#################
# DRAWS THE BACKGROUND 
#################

#Ground 
screen.create_rectangle(0, 600, 800, 500, fill='#336633')

#Branch of the tree
screen.create_rectangle(posX, posY, posX+width, posY-height, fill='#3a1c1c', outline='')

#Leaves of the tree
screen.create_polygon(posX-width*3/2, posY-height/4, posX, posY-height/1.25, posX+width, posY-height/1.25, posX+width+width*3/2, posY-height/4, fill='#143306')

screen.create_polygon(posX-width*1.15, posY-height/1.5, posX+width/2, posY-height*1.25, posX+width+width*1.15, posY-height/1.5, fill='#143306')


########################################
# SCENE 1: LUMBERJACK CUTS DOWN THE TREE
########################################
while True:
  
  ######################
  # DRAWS THE LUMBERJACK
  ######################

  #Head
  head = screen.create_oval(posx, posy, posx+50, posy+50, fill='#ffe0bd')

  #Eyes
  eye1 = screen.create_oval(posx+50/2-10, posy+15, posx+50/2-5, posy+10, fill='black')

  eye2 = screen.create_oval(posx+50/2+10, posy+15, posx+50/2+5, posy+10, fill='black')

  #Mouth
  mouth = screen.create_line(posx+17, posy+30, posx+25, posy+35, posx+33, posy+30, smooth=1, width=3)

  #Body
  body = screen.create_line(posx+25, posy+50, posx+25, posy+100, fill='red', width=2)

  #Legs
  leg1 = screen.create_line(posx+25, posy+100, posx+45, posy+150, fill='blue', width=2)

  leg2 = screen.create_line(posx+25, posy+100, posx+5, posy+150, fill='blue', width=2)

  #Arms
  arm1 = screen.create_line(posx+25, posy+55, posx-40, posy+65, fill='red', width=2)

  arm2 = screen.create_line(posx+25, posy+65, posx-40, posy+75, fill='red', width=2)

  #Chainsaw
  chainsaw1 = screen.create_oval(chainX-10, chainY-10, chainX-30, chainY-40, fill='black')

  chainsaw2 = screen.create_rectangle(chainX, chainY, chainX-40, chainY-25, fill='orange', outline='')

  #Chains 
  chain1 = screen.create_rectangle(chainX-40, chainY-10, chainX-80, chainY-20, fill='silver', outline='')

  chain2 = screen.create_arc(chainX-85, chainY-20, chainX-65, chainY-10, fill='silver', outline='', start = 90, extent = 180)

  #Chainsaw image 
  chainImg = screen.create_image(chainX-30, chainY-15, image=catPic)


  ###################
  # INTRODUCTORY TEXT
  ###################
  if firstTime == True:

    #Only repeats once 
    for text in startingText:

      #Loops through the messages
      message = screen.create_text(400,100, fill='red', text=text, font='Arial 35')

      screen.update()
      time.sleep(2)
      screen.delete(message)
    
    firstTime = False
    


  #Clear lists to update the position of the lumberjack jack and chainsaw
  if end == False:
    x.clear() 
    y.clear() 
    size.clear()
    triangleDrawingsDown.clear()
    triangleDrawingsUp.clear() 
  

  #Changes the speed of the lumberjack and chainsaw 

  #Walk towards the tree 
  if chainX - 85 > treeStart:
    posx ,chainX = posx - 1, chainX - 1

  #Stops after cutting down the tree 
  elif chainX - 85 < posX: 
    pass

  #Slowly cut the treedown 
  else:
    posx ,chainX = posx - 0.2, chainX - 0.2

  
  #Random moving spikes on the chainsaw 
  if end == False:
    for k in range(7):
      
      x.append(random.uniform(chainX-80, chainX-40))
      y.append(random.uniform(chainY-20, chainY - 18))
      size.append(random.uniform(5,7))


  #Draws the moving triangles on the chainsaw
  for l in range(7):
    #Triangles on the top of the chainsaw
    triangleDrawingsUp.append(screen.create_polygon(x[l], y[l], x[l]-size[l], y[l], x[l]-size[l]/2, y[l]-size[l],fill='red', outline=''))

    #Triangles on the bottom of the chainsaw
    triangleDrawingsDown.append(screen.create_polygon(x[l], y[l]-size[l]+15, x[l]-size[l], y[l]-size[l]+15, x[l]-size[l]/2, y[l]+15,fill='red', outline=''))


  #FALLING TREE PARTICLES
  if chainX -85 < treeStart:
    if end == False:

      #Creates a particle with a random attribute
      for t in range(1):

        #Random Size and Speeds 
        xSpeed.append(random.uniform(5,8))
        chunkSize.append(random.uniform(10, 20))
        ySpeed.append(random.uniform(2,3))
        quadraticMultiplier.append(random.uniform(5,12))


        #Random Colors
        leafColors.append(random.choice(treeColors))
        barkColor.append(random.choice(barkColors))
        

        #Random spawning position 
        chunkPosX.append(random.uniform(chainX-80,chainX - 90))
        chunkPosY.append(random.uniform(chainY-5, chainY-30))
        treeChunks.append(0)

        
    #CREATES THE FLYING PARTICLES 
    for r in range(len(treeChunks)):

      #Decides which color to use  
      if chainX -85 < posX + width:
        colorUsed = barkColor[r]
      
      else:
        colorUsed = leafColors[r]

      #Draws the flying particles
      treeChunks[r] = screen.create_oval(chunkPosX[r], chunkPosY[r], chunkPosX[r]+chunkSize[r], chunkPosY[r]+chunkSize[r], fill=colorUsed, outline='')
    

    #Moves the particles in a parabolic motion 
    for q in range(len(treeChunks)):
      chunkPosX[q] = xSpeed[q] + chunkPosX[q]
      chunkPosY[q] += 3*ySpeed[q]**2 - quadraticMultiplier[q]*ySpeed[q]
      ySpeed[q] += 0.05

      #Finds the particles outside of the screen 
      if chunkPosY[q] > 650:
        outOfScreenIndexes.append(q) 
    

  ######################
  # CREATES THE RAINFALL
  ######################
  
  for rain in range(2):
      #Random attirbutes for the rain fall particles 

      rainX.append(random.uniform(-100,800))
      rainY.append(random.uniform(0,-100))
      rainSize.append(random.uniform(60, 70))
      rainSpeed.append(random.uniform(20, 25))

      #Fills the array with empty values 
      rainDrawings.append(0)

  #Draws and moves the rain droplets
  for l in range(len(rainDrawings)):
    rainDrawings[l] = screen.create_line(rainX[l], rainY[l], rainX[l]+5, rainY[l]+rainSize[l], fill='blue', width=2)

    rainY[l] += rainSpeed[l] 
    rainX[l] += 1

    #Finds the rain droplets that have hit the ground
    if rainY[l] > 550:
      rainIndexes.append(l)
      
  
  ##DELETES AND REMOVES RAIN ON THE GROUND FROM LISTS AND SCREEN TO REDUCE LAG
  rainIndexes.sort(reverse=True)
  for bound in rainIndexes:
    screen.delete(rainDrawings[bound])

    rainDrawings.pop(bound)
    rainSpeed.pop(bound)
    rainSize.pop(bound)
    rainY.pop(bound)
    rainX.pop(bound)

  #Makes room for next rain particles that hit the ground
  rainIndexes.clear()
  
    
  #DELETES AND REMOVES OUT OF CANVAS PARTICLES FROM LISTS AND SCREEN TO REDUCE LAG
  outOfScreenIndexes.sort(reverse=True)
  for index in outOfScreenIndexes:
    screen.delete(treeChunks[index])

    treeChunks.pop(index)
    quadraticMultiplier.pop(index)
    chunkPosY.pop(index)
    chunkPosX.pop(index)
    leafColors.pop(index)
    chunkSize.pop(index) 
    ySpeed.pop(index)
    xSpeed.pop(index)
    barkColor.pop(index)
      
  #Makes room for the next out of screen particles 
  outOfScreenIndexes.clear()


  #UPDATES THE CANVAS 
  time.sleep(0.01)
  screen.update() 


  #The end of the scene
  if chainX - 85 < posX:
    end = True

    #ONCE THE LAST TREE TRUNK IS OFF THE SCREEN EXIT THE SCENE
    if len(treeChunks) == 0:

      screen.create_text(400, 100, text='A little while later...', font='Arial 35', fill='red')
      screen.update()

      time.sleep(5)
      
      screen.delete("all")
      break
    


  #Deletes all the moving objects on the screen
  for t in range(7):
    screen.delete(x[t] ,y[t] ,size[t] ,triangleDrawingsUp[t], triangleDrawingsDown[t], head, eye1, eye2, head, mouth, body, leg1, leg2, arm1, arm2, chainsaw1, chainsaw2, chain1, chain2, chainImg) 
  
  #DELETES THE TREE CHUNKS IN FLIGHT
  if chainX -85 < treeStart:
    for n in range(len(treeChunks)):
      screen.delete(treeChunks[n])
  
  #DELETES AND REMOVES THE ACTIVE RAINDROPS
  for rainDrops in range(len(rainDrawings)):
    screen.delete(rainDrawings[rainDrops])
      


#########################################
# SCENE 2: TREE IS THROWN INTO WOODCHIPPER
#########################################


#Variables
posx = 650
posy = 100
posY = posy + 150
posX = posx -40
chipperX = posX
chipperY = posY
fallSpeed = 0.1
broken = False
treeX = []
treeY = []
particleDrawings = []
treeSize = []
fallSpeeds = []
treeIndexes = []
barkColors = ['#3a1c1c', '#8a7362', '#533118', '#754A41', '#5E372E']
chipX = []
chipY = []
chipDrawing = []
chipSpeedX = []
chipSpeedY = []
chipColors = ['yellow',  '#8a7362', '#533118', 'yellow', 'yellow','yellow','yellow']
chipIndexes = []
chipSize = []
chipColor = []
direcX = ['up', 'down']
direcY = ['up', 'down']
directionX = []
directionY = []
First = True



#BACKGROUND
#Hill
screen.create_rectangle(posX+30, posY, posX+190, posY+350, fill='brown', outline='')

#Ground 
screen.create_rectangle(0, 600, 640, 500, fill='#336633', outline='')


######################
# DRAWS THE LUMBERJACK
######################

#Head
head = screen.create_oval(posx, posy, posx+50, posy+50, fill='#ffe0bd')

#Eyes
eye1 = screen.create_oval(posx+50/2-10, posy+15, posx+50/2-5, posy+10, fill='black')

eye2 = screen.create_oval(posx+50/2+10, posy+15, posx+50/2+5, posy+10, fill='black')

#Body
body = screen.create_line(posx+25, posy+50, posx+25, posy+100, fill='red', width=2)

#Legs
leg1 = screen.create_line(posx+25, posy+100, posx+45, posy+150, fill='blue', width=2)

leg2 = screen.create_line(posx+25, posy+100, posx+5, posy+150, fill='blue', width=2)

#Arms
arm1 = screen.create_line(posx+25, posy+55, posx-40, posy+65, fill='red', width=2)

arm2 = screen.create_line(posx+25, posy+65, posx-40, posy+75, fill='red', width=2)



#Opening text
opnTxt = screen.create_text(250, 100, text="I'm going to profit \nso much from this!", fill='red', font='Arial 20')

screen.update()



while True:

  #TREE BRANCH 
  if broken == False:
    branch = screen.create_rectangle(posX, posY, posX-width, posY-height, fill='#3a1c1c', outline='')


  #Mouth of lumberjack
  mouth = screen.create_line(posx+17, posy+30, posx+25, posy+35, posx+33, posy+30, smooth=1, width=3)


  #CREATES THE WOODCHIPPER 
  if broken == False:
    woodchipper = screen.create_rectangle(chipperX+30, chipperY+100, chipperX-width-30, chipperY+200, fill='yellow', outline='')

    chipperText = screen.create_text(chipperX-width/2, chipperY+150, fill='black', font='Arial 10', text='Woodchipper\n3000')


  ######################
  # CREATES THE RAINFALL
  ######################
  
  for rain in range(2):
      #Random attirbutes for the rain fall particles 

      rainX.append(random.uniform(-100,800))
      rainY.append(random.uniform(0,-100))
      rainSize.append(random.uniform(60, 70))
      rainSpeed.append(random.uniform(20, 25))

      #Fills the array with empty values 
      rainDrawings.append(0)


  #Draws and moves the rain droplets
  for l in range(len(rainDrawings)):
    rainDrawings[l] = screen.create_line(rainX[l], rainY[l], rainX[l]+5, rainY[l]+rainSize[l], fill='blue', width=2)

    rainY[l] += rainSpeed[l] 
    rainX[l] += 1


    #Finds the rain droplets that have hit the ground
    if rainY[l] > 550:
      rainIndexes.append(l)
      
  
  ##DELETES AND REMOVES RAIN ON THE GROUND FROM LISTS AND SCREEN TO REDUCE LAG
  rainIndexes.sort(reverse=True)
  for bound in rainIndexes:
    screen.delete(rainDrawings[bound])

    rainDrawings.pop(bound)
    rainSpeed.pop(bound)
    rainSize.pop(bound)
    rainY.pop(bound)
    rainX.pop(bound)

  #Makes room for next rain particles that hit the ground
  rainIndexes.clear()


  #ACCELERATES THE TREE BRANCH DOWNWARDS
  
  if posY < chipperY + 150 and broken == False:
    posY += fallSpeed*1**2
    fallSpeed += 0.1
  

  ####################################
  # WHEN THE BRANCH IS IN THE SHREDDER 
  ####################################


  else:
    #THE TREE PARTICLES FALLING FROM THE SHREDDER
    if broken == False:
      for r in range(1):
        #random positions
        treeX.append(random.uniform(chipperX+15,chipperX-width-20))
        
        treeY.append(random.uniform(chipperY+200, chipperY+201))
        
        #Initial values for particledrawings
        particleDrawings.append(0)

        #Random particle size 
        treeSize.append(random.uniform(7,15))

        #Random Colors
        barkColor.append(random.choice(barkColors))

        #Fallspeed initial value 0
        fallSpeeds.append(0)
    
      #Draws and moves the particles
      for g in range(len(particleDrawings)):
        particleDrawings[g] = screen.create_oval(treeX[g], treeY[g], treeX[g]+treeSize[g], treeY[g]+treeSize[g], fill=barkColor[g], outline='')

        #Moves the particles
        treeY[g] += fallSpeeds[g]*1**2
        fallSpeeds[g] += 0.1

        #Finds the wood pieces that have hit the ground
        if treeY[g] > 550:
          treeIndexes.append(g)
    

      #Remove the particles on the ground from all the lists
      treeIndexes.sort(reverse=True)

      for part in treeIndexes:
        treeX.pop(part)
        particleDrawings.pop(part)
        fallSpeeds.pop(part)
        treeSize.pop(part)
        treeY.pop(part)
        barkColor.pop(part)


      #Clears the list for next particles that hit the ground
      treeIndexes.clear()


      #MOVES THE BRANCH SLOWLY DOWN
      posY += 0.2

      #MOVES THE WOOD and CHIPPER AROUND TO CREATE THE SENSE OF BEING SHREDDED
      move = random.uniform(0,2)

      #Boundaries
      if chipperX+15 < 610-30-50 or posX-width < chipperX -width-30:
        posX -= move
        chipperX-=0.2

      #Boundaries
      elif chipperX-width-15 > 600:
        posX += move
        chipperX+=0.2

      #MOVES THE LOG AND WOODCHIPPER AROUND RANDOMLY
      else:
        choice = random.uniform(0,1)

        if choice < 0.5:
          posX+=move 
          chipperX+=0.2
        
        else:
          posX-=move
          chipperX-=0.2
    
  
  #When the chipper breaks
  if posY >= chipperY + 200 or broken == True: 
    broken = True
    screen.delete(opnTxt)

    #Broken text
    breakTxt = screen.create_text(250, 100, text="The rain has made\nthe chipper break!", fill='red', font='Arial 20')

    screen.update()
    
    screen.delete(woodchipper, chipperText, branch)


    ##################
    # CHIPPER BLOWS UP
    ##################

    #Create the explosion particles ONCE
    if First == True:
      for w in range(400): 

        #Random location for debris
        chipX.append(random.uniform(chipperX+30,chipperX-width-30))
        chipY.append(random.uniform(chipperY+100, chipperY+200))

        #Random size
        chipSize.append(random.uniform(15,25))

        #Random Speeds
        chipSpeedX.append(random.uniform(3,15))
        chipSpeedY.append(random.uniform(3,15))

        #Random Color
        chipColor.append(random.choice(chipColors))

        #Default values for drawings
        chipDrawing.append(0)

        #Random direction 
        directionX.append(random.choice(direcX))
        directionY.append(random.choice(direcY))


    #DRAWS THE DEBRIS
    for q in range(len(chipDrawing)):
      chipDrawing[q] = screen.create_oval(chipX[q], chipY[q], chipX[q]-chipSize[q], chipY[q]-chipSize[q], fill=chipColor[q], outline='')


      #IF THE DEBRIS HITS THE HILL REVERSE THE DIRECTION
      if chipX[q] >= 640 and chipY[q] >= 250:
        chipSpeedX[q] = -chipSpeedX[q]


      #MOVES THE DEBRIS IN RANDOM DIRECTIONS 
      
      chipX[q] -= chipSpeedX[q]
      if directionX[q] == 'up':
        chipX[q] += chipSpeedX[q]*2
      
      chipY[q] -= chipSpeedY[q]
      if directionY[q] == 'up':
        chipY[q] += chipSpeedY[q]*2
      

      #FINDS THE PARTICLES THAT HAVE HIT THE GROUND or HAVE GONE OFF CANVAS
      if chipY[q] >= 550 or chipY[q] <= -50 or chipX[q] <= -50:
        chipIndexes.append(q)
        

    #REMOVES PARTICLES THAT HAVE HIT THE GROUND FROM THE LISTS
    chipIndexes.sort(reverse=True)

    for b in chipIndexes:
      chipDrawing.pop(b)
      directionY.pop(b)
      directionX.pop(b)
      chipSize.pop(b)
      chipColor.pop(b)
      chipX.pop(b)
      chipY.pop(b)
      chipSpeedX.pop(b)
      chipSpeedY.pop(b)

    
    chipIndexes.clear()
    First = False

    #ONCE ALL THE EXPLOSION BITS ARE OFF THE SCREEN 
    if len(chipX) == 0:
      time.sleep(1)
      screen.delete("all")
      break


  #UPDATES THE CANVAS
  screen.update()
  time.sleep(0.01)

  #Deletes all moving items from the screen 
  screen.delete(mouth, branch, woodchipper, chipperText) 


  #DELETES AND REMOVES THE ACTIVE RAINDROPS
  for rainDrops in range(len(rainDrawings)):
    screen.delete(rainDrawings[rainDrops])

  #DELETES THE FALLING ACTIVE TREE BRANCHES
  for particles in range(len(particleDrawings)):
    screen.delete(particleDrawings[particles])

  #DELETES THE ACTIVE EXPLODING SHREDDER BITS 
  for explosion in range(len(chipDrawing)):
    screen.delete(chipDrawing[explosion])

        

###########################
# SCENE 3: CONCLUSION SCENE
###########################



#Background 
screen.create_rectangle(0,0, 800, 600, fill='black')


#Variables
conclusion = ['To conclude...', 'Only use shredders\nin suitable weather', 'Make sure to wear\nprotective equipment', "Save the trees", "Thank you for watching\nthis infographic"]

#conclusion
for dialogue in range(len(conclusion)):
  txt = screen.create_text(400,300, fill='red', text=conclusion[dialogue], font='Arial 30')

  #UPDATES TO CANVAS
  screen.update()
  time.sleep(2)
  screen.delete(txt)
  

screen.update()
