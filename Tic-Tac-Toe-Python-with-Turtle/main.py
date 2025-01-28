import turtle
import math

'''
We're going to make an almost unbeatable tic-tac-toe game! Anyone who plays this game will play against the computer, but it's going to be really hard to win! 
The user will play as x. Every round, they will pick where they want to place an x, then the computer will place an o
We will also have to add code to check if anyone has gotten 3 in a row, or if there has been a tie
We also need to make sure that no two x's or o's share a spot
'''

#Here are the step's we will go through to build this game
#  1. Create a turtle and function that draws the background. Number each square in it's top left corner
#  2. Create a function to draw an x and a function to draw an o
#  3. Create event listeners, so the user can try to fill a square by pressing it's corresponding number
#  4. Create a representation of the board in the code
#  5. Create a turtle to give announcements to the user, set it up to tell the user if they've picked an invalid spot
#  6. Create a function to check if someone has won, and use it in the correct place to check if x won
#  7. Create a function to pick a place for the computer to put an o
#  8. Check if o won 
#  9. Create a function to check for a tie


# This function draws the grid the game will be played on
def drawBoard():
  # Draw both of the horizontal lines, starting from different heights
  for i in range(2):
    drawer.penup()
    drawer.goto(-300, 100 - 200*i)
    drawer.pendown()
    drawer.forward(600)

  drawer.right(90)

  # Draw both of the veritcal lines, starting from the correct position
  for i in range(2):
    drawer.penup()
    drawer.goto(-100 + 200*i, 300)
    drawer.pendown()
    drawer.forward(600)

  # Add the numbers to the top corner of each square
  num = 1
  for i in range(3):
    for j in range(3):
      drawer.penup()
      drawer.goto(-290 + (j * 200), 280 - (i * 200))
      drawer.pendown()

      drawer.write(num, font = ("Arial", 12))
      num += 1

  # Update the screen with the new changes
  screen.update()

# This function draws an "X" centered at the inputted coordinates
def drawX(x, y):
  # Move to the correct spot
  drawer.penup()
  drawer.goto(x,y)
  drawer.pendown()

  # Draw the lines of the "X"
  drawer.setheading(60)
  for i in range(2):
    drawer.forward(75)
    drawer.backward(150)
    drawer.forward(75)
    drawer.left(60)

  # Update the screen with the new changes
  screen.update()

# This function draws an "O" centered at the inputted coordinates
def drawO(x, y):
  # Move to the correct spot
  drawer.penup()
  drawer.goto(x,y + 75)
  drawer.pendown()

  drawer.setheading(0)

  # Draw a circle with of the correct size
  for i in range(180):
    drawer.forward((150 * math.pi)/180)
    drawer.right(2)

  # Update the screen with the new changes
  screen.update()

# This function will check if either "X" or "O" has won on the inputted board
def checkWon(letter):
  # Check if there are three in a row horizontally
  for i in range(3):
    if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] == letter:
      return True

  # Check if there are three in a row vertically
  for i in range(3):
    if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] == letter:
      return True

  # Check if there are three in a row diagonally down
  if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] == letter:
    return True

  # Check if there are three in a row diagonally up
  if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] == letter:
    return True

  # If at this point, the given letter has not won
  return False

# This function checks if the game is a tie
def checkDraw():
  # Count the number of X's in the board
  count = 0
  for i in range(3):
    for j in range(3):
      if board[i][j] == "x":
        count += 1
  
  # If there are 4 X's, and no one has won at this point, that means theres a tie
  if count > 3:
    return True
  else:
  # If not, the game isn't over
    return False

# This function will add an "O" to the board in the best place
def add0():
  # Check if there is any place in the board that will result in a win for "O". Place an "O" there if so
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "o"
        if checkWon("o"):
          drawO(-200 + (200 * j), 200 - (200 * i))
          return
        board[i][j] = " "

  # Check if there is any place in the board that will result in a win for "X". Place an "O" there to block if so
  for i in range(3):
    for j in range(3):
      if board[i][j] == " ":
        board[i][j] = "x"
        if checkWon("x"):
          board[i][j] = "o"
          drawO(-200 + (200 * j), 200 - (200 * i))
          return
        board[i][j] = " "

  # Try to place an "O" in one of the corners
  for i in range(0, 3, 2):
    for j in range(0, 3, 2):
      if board[i][j] == " ":
        board[i][j] = "o"
        drawO(-200 + (200 * j), 200 - (200 * i))
        return

  # Try to place an "O" on one of the sides
  for i in range(3):
      for j in range(3):
        if board[i][j] == " ":
          board[i][j] = "o"
          drawO(-200 + (200 * j), 200 - (200 * i))
          return

# This function activates all the event listeners
def activate(functions):
  for i in range(9):
    screen.onkey(functions[i], str(i + 1))


# This function deactivates all the event listeners
def deactivate():
  for i in range(9):
    screen.onkey(None, str(i + 1))

# This function will try to add an X to the inputted location
def addX(row, column):
  # Clear any announcements on the screen
  announcer.clear()
  
  # Check if the space they want to add to is full
  if board[row][column] == "x" or board[row][column] == "o":
    # Tell them that they can't take that spot
    announcer.write("That spot is taken!", font = ("Arial", 36))
    screen.update()
  else:
    # If they can fill that spot, draw an "X" in the correct spot and add it to the list holding the board
    drawX(-200 + (200 * column), 200 - (200 * row))
    board[row][column] = "x"

    # Check if that new place made "X" win
    if checkWon("x"):
      # Tell them that they won
      announcer.goto(-97, 0)
      announcer.write("You won!", font = ("Arial", 36))

      # Update the screen and deactivate the event listeners
      screen.update()
      deactivate()
    else:
      # If they didn't win, then an "O" gets added to the board
      add0()

      # Check if that new place made "O" win
      if checkWon("o"):
        # Tell them that they lost
        announcer.goto(-90, 0)
        announcer.write("You lost!", font = ("Arial", 36))
        
        # Update the screen and deactivate the event listeners
        screen.update()
        deactivate()
      # Check if there is no way to win, meaning a tie
      elif checkDraw():
        # Tell them they tied
        announcer.goto(-90, 0)
        announcer.write("It's a tie!", font = ("Arial", 36))
        
        # Update the screen and deactivate the event listeners
        screen.update()
        deactivate()

# Define functions for the event listeners
def squareOne():
  addX(0,0)
def squareTwo():
  addX(0, 1)
def squareThree():
  addX(0, 2)
def squareFour():
  addX(1, 0)
def squareFive():
  addX(1, 1)
def squareSix():
  addX(1, 2)
def squareSeven():
  addX(2, 0)
def squareEight():
  addX(2, 1)
def squareNine():
  addX(2, 2)

# Create the screen and turn of animation
screen = turtle.Screen()
screen.tracer(0, 0)

# Create the two turtles necessary for the project
drawer = turtle.Turtle()
announcer = turtle.Turtle()

# Set up these turtles
announcer.penup()
announcer.ht()
announcer.goto(-200, 0)
announcer.color("red")
drawer.pensize(10)

# Create a list of the event listener functions
functions = [squareOne, squareTwo, squareThree, squareFour, squareFive, squareSix, squareSeven, squareEight, squareNine]
drawer.ht()

# Draw the board
drawBoard()

# Create the board, which will actually save the value
board = []
for i in range(3):
  row = []
  for j in range(3):
    row.append(" ")
  board.append(row)

# Activate the event listeners
activate(functions)
screen.listen()

