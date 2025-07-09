from  turtle import Turtle
file = open("data.txt")
contents =file.read()
file.close()
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(contents)
        self.penup()
        self.color("white")
        self.goto(0,270 )
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}     High Score : {self.high_score}", move=False, align='center', font=('Arial', 18, 'normal'))

    def reset(self):

        if self.score > self.high_score:
            file1 = open("data.txt" ,mode ="w")
            self.high_score = self.score
            file1.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score +=  1
        self.update_score()

    def game_over(self):
        self.goto(0,0 ,)
        self.write("GAME OVER", align='center' , font=('Arial', 18, 'normal'))