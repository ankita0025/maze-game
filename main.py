import turtle
import math
import random

#register shapes
turtle.register_shape("loot-1.gif")
turtle.register_shape("wall-1.gif")
turtle.register_shape("wizzl-1.gif")
turtle.register_shape("wizzr-1.gif")
turtle.register_shape("enemy.gif")




#setting up screen of game
wn = turtle.Screen()
wn.bgcolor("white")
wn.title("Maze Game")
wn.setup(700,700)
wn.tracer(0)

#configuring the turtle
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("wizzr-1.gif")
        self.color("pink")
        self.penup()
        self.speed(0)
        self.gold=0

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor()+24
        self.shape("wizzr-1.gif")
        if (move_to_x,move_to_y) not in walls:

            self.goto(move_to_x,move_to_y)

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)


    def go_left(self):
        move_to_x = player.xcor() -24
        move_to_y = player.ycor()
        self.shape("wizzl-1.gif")
        if (move_to_x, move_to_y) not in walls:

            self.goto(move_to_x, move_to_y)


    def go_right(self):
        move_to_x = player.xcor() +24
        move_to_y = player.ycor()
        self.shape("wizzr-1.gif")
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)

    def is_collision(self, other):
        a= self.xcor() - other.xcor()
        b = self.ycor() - other.ycor()
        distance = math.sqrt((a**2)+(b**2))

        if distance <5:
            return True
        else:
            return False

    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()
        print("restart game")

        turtle.bye()


class Treasure(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("loot-1.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 100
        self.goto(x,y)

    def destroy(self):
        self.goto(2000,2000)
        self.hideturtle()





class Enemy(turtle.Turtle):
    def __init__(self,x,y):
        turtle.Turtle.__init__(self)
        self.shape("enemy.gif")
        self.color("blue")
        self.penup()
        self.speed(0)
        self.gold = 50
        self.goto(x,y)
        self.direction = random.choice(["up", "down", "left", "right"])

    def move(self):
        if self.direction == "up":
            dx=0
            dy = 24
        elif self.direction=="down":
            dx= 0
            dy = -24
        elif self.direction=="left":
            dx= -24
            dy= 0
        elif self.direction=="right":
            dx= 24
            dy = 0
        else:
            dx=0
            dy=0

        move_to_x = self.xcor() +dx
        move_to_y = self.ycor() +dy

        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x,move_to_y)
        else:
            self.direction = random.choice(["up", "down", "left", "right"])
        turtle.ontimer(self.move , t=random.randint(100,300))
    def destroy(self):
        self.goto(2000, 2000)
        self.hideturtle()


#a list of list containing all levels of maze
levels = [""]

#level 1 maze
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"X  XX XXXXXTP        XXXX",
"X XX  T      XXXX      XX",
"X  E   XX       XXX T   X",
"X  XXXXXXX   XXXXX  XXXXX",
"XX    XXXXXXXX          X",
"XXXXXXX    E T   XXXXXXXX",
"XXXXX        XXXXXX     X",
"XXXXXXXXT             XXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
""
]

treasures = []
enemys = []

levels.append(level_1)

def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            char = level[y][x]

            screen_x = -288 + (x*24)
            screen_y = 288 - (y*24)

            if char == "X":
                pen.goto(screen_x,screen_y)
                pen.shape("wall-1.gif")
                pen.stamp()

                walls.append((screen_x,screen_y))

            if char == "P":
                player.goto(screen_x,screen_y)


            if char == "T":
                treasures.append(Treasure(screen_x,screen_y))

            if char== "E":
                enemys.append(Enemy(screen_x,screen_y))
pen= Pen() #for using turtle module
player = Player()

walls=[]

setup_maze(levels[1])# seting up level 1

#keyboard binding
turtle.listen()
turtle.onkey(player.go_left, "Left")
turtle.onkey(player.go_right, "Right")
turtle.onkey(player.go_up, "Up")
turtle.onkey(player.go_down, "Down")
for enemy in enemys:
    turtle.ontimer(enemy.move,t=250)
#turn off screen updates



while True:

     for treasure in treasures:
         if player.is_collision(treasure):
             player.gold += treasure.gold
             print("player gold : {}".format(player.gold))

             treasure.destroy()
             treasures.remove(treasure)
             if len(treasures)==0:
                 turtle.write("gold: {} \n GAME OVER".format(player.gold), font=("ariel", 20, "bold"))


     for enemy in enemys:
         if player.is_collision(enemy):
             player.destroy()


     wn.update()
