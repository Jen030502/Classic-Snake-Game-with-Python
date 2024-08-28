import turtle
import random


#define program constant 
WIDTH = 800
HEIGHT = 600
DELAY = 100 #millisecond
FOODSIZE = 32
SNAKESIZE = 20

offset = {
    "up" : (0,SNAKESIZE),
    "down": (0,-SNAKESIZE),
    "left": (-SNAKESIZE,0),
    "right":(SNAKESIZE,0)
}


#high score 
highScore = 0

#loads the high score if it exist 
try:
    with open("highscore.txt","r") as file:
        highScore = int(file.read())
        
except FileNotFoundError:
    pass


def updateHighScore():
    global highScore
    if score > highScore:
        highScore = score
        with open("highscore.txt","w") as file:
            file.write(str(highScore))






def bindDirectionKeys():
    screen.onkey(lambda: setSnakeDirection("up"),"Up")
    screen.onkey(lambda: setSnakeDirection("down"),"Down")
    screen.onkey(lambda: setSnakeDirection("left"),"Left")
    screen.onkey(lambda: setSnakeDirection("right"),"Right")



def setSnakeDirection(direction):
    global snakeDirection
    if direction =="up":
        if snakeDirection != "down": #No self-collision simply by pressiong wrong key 
            snakeDirection = "up"

    elif direction =="down":
        if snakeDirection != "up": #No self-collision simply by pressiong wrong key 
            snakeDirection = "down"
            
    elif direction =="left":
        if snakeDirection != "right": #No self-collision simply by pressiong wrong key 
            snakeDirection = "left"
            
    elif direction =="right":
        if snakeDirection != "left": #No self-collision simply by pressiong wrong key 
            snakeDirection = "right"



def gameloop():
    stamper.clearstamps()#remove exsiting stamps made by stamper 
    
    newHead = snake[-1].copy()
    newHead[0] += offset[snakeDirection][0]
    newHead[1] += offset[snakeDirection][1]
    
    
    #check collisions 
    if newHead in snake or newHead[0] < -WIDTH / 2 or  newHead[0] > WIDTH /2 or newHead[1] < - HEIGHT / 2 or newHead[1] > HEIGHT / 2:
        reset()
    else:
    
        #add new head to snake body
        snake.append(newHead)
        
        ## check the food collosion 
        if not foodColl():      
            # keep the snake the same length  
            snake.pop(0)
        
        
        #draw snake  
        stamper.shape("assest/snakehead.gif")
        stamper.goto(snake[-1][0],snake[-1][1])
        stamper.stamp()
        stamper.shape("circle")
        
        
        for segment in snake[:-1]:
            stamper.goto(segment[0],segment[1])
            stamper.stamp()

        #refresh the screen 
        screen.title(f"Snake Game. Score: {score}   High Score: {highScore}")
        screen.update()
        
        #rinse and repeat 
        turtle.ontimer(gameloop,DELAY)


def foodColl():
    global foodPos,score
    if getDistance(snake[-1],foodPos) < 20:
        score += 1 
        updateHighScore()
        foodPos = getRandomFoodPos()
        food.goto(foodPos)
        return True
    return False
        



def getRandomFoodPos():
    x =  random.randint(-WIDTH / 2 + FOODSIZE , WIDTH/2 - FOODSIZE)
    y =  random.randint(-HEIGHT / 2 + FOODSIZE , HEIGHT/2 - FOODSIZE)
    return(x,y)
    




def getDistance(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5 #pythagoras' theorem 
    return distance

def reset():
    global score,snake,snakeDirection,foodPos
    score = 0
    snake = [[0,0],[SNAKESIZE,0],[SNAKESIZE * 2,0],[SNAKESIZE * 3,0]]
    snakeDirection = "up"
    foodPos = getRandomFoodPos()
    food.goto(foodPos)
    gameloop()





# create a window where we do our drawing 
screen = turtle.Screen()
screen.setup(WIDTH,HEIGHT)# set up the dimention of the window
screen.title("Snake")
screen.bgpic("assest/bg.gif")
screen.register_shape("assest/snakefood.gif")
screen.register_shape("assest/snakehead.gif")
screen.tracer(0)

#Event handlers 

screen.listen()
bindDirectionKeys()





# create a turtle to do you bidding 

stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("#009ef1")
stamper.penup()

    
    
#food 
food = turtle.Turtle()
food.shape("assest/snakefood.gif")
food.shapesize(FOODSIZE/20)
food.penup()

    
    
# set the animtion to motion 
reset()






turtle.done()