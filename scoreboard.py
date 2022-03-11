from turtle  import Turtle

FONT=("Walter",16,"bold")
ALGIN="center"

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,280)
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"El puntaje es: {self.score}", font=FONT, align=ALGIN)

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Over, Final Score: {self.score}", font=FONT, align=ALGIN)
    
    def game_win(self):
        self.clear()
        self.goto(0,0)
        self.write(f"Game Perfect, Final Score: {self.score}", font=FONT, align=ALGIN)