from flask import Flask
import random

app = Flask(__name__)

url = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
random_number = random.randint(0,9)
@app.route('/')
def home():
    print("Le chiffre est", random_number)
    return "<h1>Guess a number beetween 0 and 9</h1>\n"\
            f"<img src={url}>"
            

@app.route("/<numb>")
def guess_number(numb):
    if int(numb) < random_number:
        return "<h1 style='color:red'>Too low, try again</h1>"
    elif int(numb) > random_number:
        return "<h1 style='color:purple'>Too high, try again</h1>"
    if int(numb) == random_number:
        return "<h1 style='color:green'>You found it</h1>"
    
if __name__ == '__main__':
    app.run(debug=True)