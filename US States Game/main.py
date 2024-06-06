from turtle import Turtle,Screen
import pandas
class TurtleStates:
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.hideturtle()
        self.turtle.penup()
        self.screen = Screen()
        self.screen.bgpic("blank_states.gif")
        self.screen.setup(width=726,height=498)
        self.screen.title("US States")
        self.game_works = True
        self.found = 0
        self.get_data()
        self.ask()

        
    def get_data(self):
        self.dictionary = {}
        data = pandas.read_csv("50_states.csv")
        df = pandas.DataFrame(data)
        for (index,row) in df.iterrows():
            state = row["state"]
            x = row["x"]
            y = row["y"]
            self.dictionary[state] = (x,y)

    def ask(self):
        while self.game_works:
            user_input = self.screen.textinput(title=f"States Found: {self.found}/50",prompt="Enter a state")
            if user_input.title() in self.dictionary:
                coordinates = self.dictionary[user_input.title()]
                self.turtle.goto(coordinates)
                self.turtle.write(user_input.title())
                self.dictionary.pop(user_input.title())
                self.found +=1
                if self.found == 50:
                    self.game_works = False
                    user_input = self.screen.textinput(title="Do you want to play again?",prompt="Yes or no?")
                    if user_input[0].lower() == 'y':
                        self.screen.clear()
                        new_object = TurtleStates()
                    else:
                        exit()




if __name__ == "__main__":
    ts = TurtleStates()