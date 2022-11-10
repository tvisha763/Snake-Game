import turtle
import random
import time
screen = turtle.Screen()
screen.tracer(0,0)
timmy = turtle.Turtle()
timmy.pu()
pressed_last=["right"]
length=1
timmy.shape("turtle")
timmy.color("dark green")
timmy.speed(0)
gridturtle = turtle.Turtle()
gridturtle.speed(0)
foodpos=[0,0]
def drawgrid():
 gridturtle.pu()
 gridturtle.goto(-300,300)
 gridturtle.pd()
 gridturtle.goto(300,300)
 gridturtle.goto(300,-300)
 gridturtle.goto(-300,-300)
 gridturtle.goto(-300,300)
 for line in range(-300,300,20):
   gridturtle.pu()
   gridturtle.goto(300,line)
   gridturtle.pd()
   gridturtle.goto(-300,line)
 for line in range(-300,300,20):
   gridturtle.pu()
   gridturtle.goto(line,300)
   gridturtle.pd()
   gridturtle.goto(line,-300)
drawgrid()

def foodplacement():
  global foodpos
  x=random.randint(-15,14)*20+10
  y=random.randint(-15,14)*20+10
  foodpos[0]=x
  foodpos[1]=y
  timmy.goto(x,y)
  timmy.stamp()
for something in range(1):
 foodplacement()
snake=turtle.Turtle()
snake.pu()
snake.shape("square")
snake.color("red")
snake.goto(10,10)
snake.speed(0)
gridturtle.ht()
snakepositions=[(10,10)]
gameover=False
hsadvfsd=turtle.Turtle()
hsadvfsd.ht()
hsadvfsd.pu()
hsadvfsd.color("blue")
def message():
  hsadvfsd.write("U DIED! SCORE:"+str(length-1),align="center", font=("arial",20,"bold"))
  print("gameover")
  screen.update()
def checkgameover():
  global snakepositions,gameover
  first= True
  for something in snakepositions:
    if something[0]>300:
      gameover = True
      message()
    if something[0]<-300:
      gameover = True
      message()
    if something[1]>300:
      gameover = True
      message()
    if something[1]<-300:
      gameover = True
      message()
    if not first:
      if snakepositions[0]==something:
        gameover = True
        message()
    first = False
def grow():
  global snakepositions
  global pressed_last
  global length
  x = snakepositions[-1][0]
  y = snakepositions[-1][1]
  if pressed_last[0]=='right':
    snakepositions.append([x-20,y])
  if pressed_last[0]=='left':
    snakepositions.append([x+20,y])
  if pressed_last[0]=='up':
    snakepositions.append([x,y-20])
  if pressed_last[0]=='down':
    snakepositions.append([x,y+20])
  length+=1
def checkfood():
  global snakepositions, foodpos
  if foodpos[0]==snakepositions[0][0] and foodpos[1]==snakepositions[0][1]:
    timmy.clear()
    grow()
    foodplacement()
def moveUp():
  global pressed_last
  pressed_last.insert(0,"up")
  del pressed_last[length:]
def moveDown():
  global pressed_last
  pressed_last.insert(0,"down")
  del pressed_last[length:]
def moveLeft():
  global pressed_last
  pressed_last.insert(0,"left")
  del pressed_last[length:]
def moveRight():
  global pressed_last
  pressed_last.insert(0,"right")
  del pressed_last[length:]
def drawsnake():
  global snake, snakepositions
  snake.clear()
  for anything in snakepositions:
    snake.goto(anything[0], anything[1])
    snake.stamp()
  screen.update()
def move():
  global pressed_last, snakepositions
  pressed_last.insert(0,pressed_last[0])
  del pressed_last[length:]
  temp1=snakepositions[0][0]
  temp2=snakepositions[0][1]
  if pressed_last[0]=="right":
    temp1+=20
  if pressed_last[0]=="left":
    temp1-=20
  if pressed_last[0]=="up":
    temp2+=20
  if pressed_last[0]=="down":
    temp2-=20
  snakepositions.insert(0,(temp1,temp2))
  del snakepositions[length:]
  time.sleep(.1)
def loop():
  global gameover
  if not gameover:
    checkfood()
    move()
    drawsnake()
    checkgameover()
    screen.ontimer(loop,1)
loop()
screen.onkey(moveUp,"Up")
screen.onkey(moveDown,"Down")
screen.onkey(moveLeft,"Left")
screen.onkey(moveRight,"Right")
screen.listen()