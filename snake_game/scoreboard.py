from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 16, "normal")
FONT_2 = ("Arial", 32, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.hideturtle()
        self.sety(270)
        self.color("white")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            file = open("data.txt", mode="w")
            file.write(f"{self.highscore}")
            file.close()
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.home()
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT_2)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()








