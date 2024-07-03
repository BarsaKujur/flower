import turtle as tur

import colorsys as cs

tur.setup(800,800)

tur.speed(0)

tur.tracer(10)

tur.width(2)

tur.bgcolor("black")


for j in range(25):
    for i in range(15):
        tur.color(cs.hsv_to_rgb(i/15,j/25,1))
        tur.right(90)
        tur.circle(200-j*4,90)
        tur.left(90)
        tur.circle(200-j*4,90)
        tur.right(180)
        tur.circle(50,24)
        
        
        
# Create a turtle for drawing text
text_turtle = tur.Turtle()
text_turtle.speed("fastest")  # Set the drawing speed

# Define the text and colors
text = "Here's the flower for you.Thanks for your purchase. Have a nice day!"
colors = ["red", "green", "blue", "purple", "orange"]

# Calculate the starting position for centered text at the bottom
text_width = len(text) * 10  # Assuming each character has a width of 10 units
start_x = -text_width 
start_y = -300  # Adjust the vertical position as needed

# Position the text
text_turtle.penup()
text_turtle.goto(start_x, start_y)
text_turtle.pendown()

# Write the text in multicolor
for char in text:
    color = colors[text.index(char) % len(colors)]
    text_turtle.color(color)
    text_turtle.write(char, font=("Arial", 16, "bold"))
    text_turtle.forward(20)  # Adjust spacing between characters

# Draw a smiling emoji at the bottom-middle
emoji_turtle = tur.Turtle()
emoji_turtle.penup()
emoji_turtle.goto(0, start_y - 40)  # Position the emoji just below the text
emoji_turtle.pendown()
emoji_turtle.color("yellow")
emoji_turtle.write("😊", font=("Arial", 24, "bold"))



# Hide the turtles
text_turtle.hideturtle()
emoji_turtle.hideturtle()

# Keep the window open
tur.done()
        
tur.hideturtle()
tur.done()