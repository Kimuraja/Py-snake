from turtle import Turtle
FONT = ('arial', 15, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as file:
            self.high_score = file.read()
        self.color("#2d3142")
        self.hideturtle()
        self.clear()
        self.pu()
        self.goto(0, 270)
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', move=False, align='center', font=FONT)

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                scr = str(self.high_score)
                file.write(scr)
        self.score = 0
        self.update_scoreboard()
