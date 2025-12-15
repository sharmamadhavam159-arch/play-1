import turtle
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Square Drawer")
tina = turtle.Turtle()
tina.shape("turtle")
tina.color("blue")
tina.speed(1) 
side_length = 100
for _ in range(4):
    tina.forward(side_length) 
    tina.right(90)            
turtle.done()
