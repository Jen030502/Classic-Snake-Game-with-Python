import turtle


#define program constant 
WIDTH = 500
HEIGHT = 500
DELAY = 20  #it's a millisecond between screen update 


def moveTurtle():
    mytutle.forward(1)
    mytutle.right(1)
    screen.update()
    screen.ontimer(moveTurtle,DELAY)




# create a window where we do our drawing 
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)# set up the dimention of the window
screen.title("Program title")
screen.bgcolor("cyan")
screen.tracer(0) #turn off the automatic animation 



mytutle = turtle.Turtle()
mytutle.shape("turtle")
mytutle.color("red")

#set animation in motion 
moveTurtle()

turtle.done()