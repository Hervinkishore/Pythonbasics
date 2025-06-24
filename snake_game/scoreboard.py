from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscorefile.txt") as file:
            self.highscore=int(file.read())
        self.score=0
        self.color("green")
        self.hideturtle()
        self.up()
        self.goto(0,270)
        self.write(f"score:{self.score} highscor:{self.highscore}", align="center", font=("Arial", 16, "normal"))

    def updatedscore(self):
        self.score+=1
        self.clear()
        self.write(f"score:{self.score} highscor:{self.highscore}", align="center", font=("Arial", 16, "normal"))

    # def gameover(self):
    #     self.goto(0,0)
    #     self.color("red")
    #     self.write("-----------------Game over---------------", align="center", font=("Arial", 20, "normal"))
    def checkscore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            self.score=0
            self.clear()
            self.write(f"score:{self.score} highscor:{self.highscore}", align="center", font=("Arial", 16, "normal"))
            with open("highscorefile.txt", "w") as file:
                file.write(f"{self.highscore}")
