from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        with open("venv\data.txt") as data:
            self.high_score = int(data.read())
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("venv\data.txt", "w") as data:
                data.write(str(self.high_score))
        self.goto(0, 0)
        self.write(f"Game Over!", align="center", font=("Arial", 24, "normal"))
