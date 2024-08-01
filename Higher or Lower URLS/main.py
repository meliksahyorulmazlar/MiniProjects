import random
from flask import Flask

app = Flask(__name__)


chosen_number = random.randint(0,9)
@app.route("/")
def main_page():
    return "<h1>Guess a number between 0 and 9<h1>" \
            "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>" \
            "<br>" \
            "<a href ='/0'>0</a>" \
            "<br>"\
            "<a href ='/1'>1</a>" \
            "<br>" \
            "<a href ='/2'>2</a>" \
            "<br>" \
            "<a href ='/3'>3</a>" \
            "<br>" \
            "<a href ='/4'>4</a>" \
            "<br>" \
            "<a href ='/5'>5</a>" \
            "<br>" \
            "<a href ='/6'>6</a>" \
            "<br>" \
            "<a href ='/7'>7</a>" \
            "<br>" \
            "<a href ='/8'>8</a>" \
            "<br>" \
            "<a href ='/9'>9</a>" \


@app.route("/<int:number>")
def guess(number):
    if number == chosen_number:
        return "<h1 style='color:green'>You found me<h1>"\
                "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number <chosen_number:
        return "<h1 style='color:red'>Too low,try again!<h1>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return "<h1 style='color:purple'>Too high,try again!<h1>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"



if __name__ == "__main__":
    app.run()


