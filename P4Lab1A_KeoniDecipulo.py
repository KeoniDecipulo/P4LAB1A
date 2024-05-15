#Keoni Decipulo
#P4AB1B
#4/29/24
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Square and Triangle")

# Create a turtle object
pen = turtle.Turtle()

# Draw a square
side_length = 100
angle = 90
num_sides = 4
count = 0
while count < num_sides:
    pen.forward(side_length)
    pen.right(angle)
    count += 1

# Move the turtle to a new position for the triangle
pen.penup()
pen.goto(150, 0)
pen.pendown()

# Draw a triangle
side_length = 100
angle = 120
num_sides = 3
count = 0
while count < num_sides:
    pen.forward(side_length)
    pen.right(angle)
    count += 1

# Hide the turtle and display the result
pen.hideturtle()
screen.mainloop()
