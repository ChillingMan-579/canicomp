# Importing the turtle and random library
import turtle
from random import randint
# Creating the screen with name and size
screen = turtle.Screen()
screen.title("DataFlair Pinball game")
screen.setup(width=1000 , height=600)

# Creating the paddle
paddle = turtle.Turtle()
#Setting its speed as zero, it moves only when key is pressed
paddle.speed(0) 
#Setting shape, color, and size
paddle.shape("square")
paddle.color("blue")
paddle.shapesize(stretch_len=2, stretch_wid=6) 
paddle.penup()
#The paddle is left-centered initially 
paddle.goto(-350,-250)

paddle2 = turtle.Turtle()
#Setting its speed as zero, it moves only when key is pressed
paddle2.speed(0) 
#Setting shape, color, and size
paddle2.shape("square")
paddle2.color("blue")
paddle2.shapesize(stretch_len=2, stretch_wid=6) 
paddle2.penup()
#The paddle is left-centered initially 
paddle2.goto(350,-250)

# Creating the ball of circle shape
ball = turtle.Turtle()
#Setting the speed of ball to 0, it moves based on the dx and dy values
ball.speed(0)
#Setting shape, color, and size
ball.shape("circle")
ball.color("red")
ball.penup()
#Ball starts from the random position from the top of the screen
#y=randint(0,400)
ball.goto(0, 0)
#Setting dx and dy that decide the speed of the ball
ball.dx = -7
ball.dy = -7

score=0

# Displaying the score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.penup()
#Hiding the turtle to show text
scoreBoard.hideturtle()
#Locating the score board on top of the screen
scoreBoard.goto(0, 260)
#Showing the score
scoreBoard.write("Score : 0 ", align="center", font=("Courier", 20, "bold"))

# Functions to move the paddle left and right
def movePadUp():
    y = paddle.ycor() #Getting the current x-coordinated of the paddle
    y += 15 
    paddle.sety(y) #Updating the x-coordinated of the paddle

# Function to move the left paddle down
def movePadDown():
    y = paddle.ycor() #Getting the current x-coordinated of the paddle
    y -= 15 
    paddle.sety(y) #Updating the x-coordinated of the paddle

def movePadUp2():
  y = paddle2.ycor() #Getting the current x-coordinated of the paddle
  y += 15 
  paddle2.sety(y) #Updating the x-coordinated of the paddle

# Function to move the left paddle down
def movePadDown2():
  y = paddle2.ycor() #Getting the current x-coordinated of the paddle
  y -= 15 
  paddle2.sety(y) #Updating the x-coordinated of the paddle

#Mapping the functions to the keyboard buttons
screen.listen()
screen.onkeypress(movePadUp, "w")
screen.onkeypress(movePadDown, "s")
screen.onkeypress(movePadUp2, "Up")
screen.onkeypress(movePadDown2, "Down")

while True:
  #Updating the screen everytime with the new changes
  screen.update()

  ball.setx(ball.xcor()+ball.dx)
  ball.sety(ball.ycor()+ball.dy)

  # Checking if ball hits the bottom and top walls of the screen  
  if ball.ycor() >280:
      ball.sety(280)
      ball.dy *= -1#Bouncing the ball
  if ball.ycor() < -280:
      ball.sety(-280)
      ball.dy *= -1#Bouncing the ball

  #Checking if the ball hits bottom and ending the game
  if ball.xcor() < -460:
      scoreBoard.clear()
      scoreBoard1 = turtle.Turtle()
      scoreBoard1.speed(0)
      scoreBoard1.penup()
      #Hiding the turtle to show text
      scoreBoard1.hideturtle()
      #Locating the score board on top of the screen
      scoreBoard1.goto(0, 0)
      scoreBoard1.color('black')
      #Showing the score
      scoreBoard1.write("Score : {} ".format(score),    align="center", font=("Courier", 30, "bold"))
      break
  if ball.xcor() > 460:
    scoreBoard.clear()
    scoreBoard1 = turtle.Turtle()
    scoreBoard1.speed(0)
    scoreBoard1.penup()
    #Hiding the turtle to show text
    scoreBoard1.hideturtle()
    #Locating the score board on top of the screen
    scoreBoard1.goto(0, 0)
    scoreBoard1.color('black')
    #Showing the score
    scoreBoard1.write("Score : {} ".format(score),    align="center", font=("Courier", 30, "bold"))
    break

  #Checking if paddle hits the ball, updating score, increasing speed and bouncing the ball
  if (paddle.xcor() + 30 > ball.xcor() > paddle.xcor() - 30 and 
     paddle.ycor() + 50 > ball.ycor() > paddle.ycor() - 50 ):

      #Increasing score of left player and updating score board
      score += 1 
      scoreBoard.clear()
      scoreBoard.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))

      #Increasing speed of the ball with the limit 7
      if(ball.dy>0 and ball.dy<5): #If dy is positive increasing dy
          ball.dy+=0.5
      elif(ball.dy<0 and ball.dy>-5): #else if dy is negative decreasing dy
          ball.dy-=0.5

      if(ball.dx>0 and ball.dx<5):#If dx is positive increasing dx
          ball.dx+=0.5
      elif(ball.dx<0 and ball.dx>-5): #else if dx is negative decreasing dx
          ball.dx-=0.5

      #Changing the direction of ball towards the right player
      ball.dx *=-1
  if (paddle2.xcor() + 30 > ball.xcor() > paddle2.xcor() - 30 and 
     paddle2.ycor() + 50 > ball.ycor() > paddle2.ycor() - 50 ):
  
      #Increasing score of left player and updating score board
      score += 1 
      scoreBoard.clear()
      scoreBoard.write("Score: {}".format(score), align="center", font=("Courier", 20, "bold"))
  
      #Increasing speed of the ball with the limit 7
      if(ball.dy>0 and ball.dy<5): #If dy is positive increasing dy
          ball.dy+=0.5
      elif(ball.dy<0 and ball.dy>-5): #else if dy is negative decreasing dy
          ball.dy-=0.5
  
      if(ball.dx>0 and ball.dx<5):#If dx is positive increasing dx
          ball.dx+=0.5
      elif(ball.dx<0 and ball.dx>-5): #else if dx is negative decreasing dx
          ball.dx-=0.5
  
      #Changing the direction of ball towards the right player
      ball.dx *= -1
    
while (True):
  screen.update()