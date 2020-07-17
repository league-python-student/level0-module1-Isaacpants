import turtle
from tkinter import messagebox, simpledialog, Tk
import math



# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    # simpledialog.askinteger()
    radi = simpledialog.askstring(title = 'Greeter', prompt="What do you want the radius to be")
    # Make a new turtle
    isaac = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    # my_turtle.circle()
    isaac.circle(radius = int(radi), extent= 360, steps=100)
    # Call the turtle .penup() method
    isaac.penup()
    # Move your turtle to a new x,y position using .goto()
    isaac.goto(10, 10)
    # Calculate the area of your circle and store it in a variable, you can use math.pi
    radii = int(radi) 
    area = math.pi * radii * radii
    # Write the area of your circle using the turtle .write() method
    # myTurtle.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))
    isaac.write(arg = "area = " + str(area), move = True, align= 'left', font = ('Arial',8, 'normal'))
    # Hide your turtle
    isaac.hideturtle()
    # Call turtle.done()
    turtle.done()
    window.mainloop()