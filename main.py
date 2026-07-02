import turtle
from random import randint

screen = turtle.Screen()
screen.title("Catch The Turtle")
screen.bgcolor("white")
screen.setup(width=800, height=600)

score = 0
game_over = False

score_turtle = turtle.Turtle()
timer_turtle = turtle.Turtle()
turtle_instance = turtle.Turtle()

def setup_score():
    score_turtle.hideturtle()
    score_turtle.penup()
    score_turtle.goto(0,260)
    score_turtle.write(f"Score = {score}",align="center",font=("Arial",20,"bold"))

def move_turtle():
    if not game_over:
        x = randint(-250,250)
        y = randint(-250,250)
        turtle_instance.penup()
        turtle_instance.shape("turtle")
        turtle_instance.goto(x,y)
        screen.ontimer(move_turtle,700)

def on_click(x,y):
    global score
    if not game_over:
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Score = {score}", align="center",font=("Arial",20,"bold"))

def count_down(time):
    global game_over
    timer_turtle.hideturtle()
    timer_turtle.penup()
    timer_turtle.goto(0,230)

    if time > 0:
        timer_turtle.clear()
        timer_turtle.write(f"Süre: {time}",align="center",font=("Arial",20,"bold"))
        screen.ontimer(fun=lambda : count_down(time-1),t=1000)
    else:
        game_over = True
        timer_turtle.clear()
        timer_turtle.write(f"Game Over",align="center",font=("Arial",20,"bold"))
        turtle_instance.hideturtle()

turtle_instance.onclick(on_click)
setup_score()
move_turtle()
count_down(15)

screen.mainloop()