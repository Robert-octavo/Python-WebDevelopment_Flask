from flask import Flask, render_template

app = Flask(__name__)

class GalileanMoons:
    def __init__(self, first, second, third, fourth) -> None:
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route('/')
def hello_world():
    return render_template("jinja_intro.html", name="Bob Smith", template_name="jinja2")

@app.route('/expressions/')
def expression():
    color = 'bronw'
    animal_one = "Dog"
    animal_two = "Cat"
    orange_amount = 20
    apple_amount = 40
    donate_amount = 15
    first_name = "Robert"
    last_name = "Ortega"
    
    kwargs = {
        "color" : color,
        "animal_one" : animal_one,
        "animal_two" : animal_two,
        "orange_amount" : orange_amount,
        "apple_amount" : apple_amount,
        "donate_amount" : donate_amount,
        "first_name" : first_name,
        "last_name" : last_name
    }
    return render_template('expressions.html', **kwargs)

@app.route('/dataStructure/')
def dataestructure():

    movies = [
        "Leon the Professional",
        "The Usual Suspects",
        "A Beutiful Mind"
    ]

    car = {
        "brand" : "Tesla",
        "model" : "Roadster",
        "year" : "2020"
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    
    kwargs = {
        "movies" : movies,
        "car" : car,
        "moons" : moons
    }

    return render_template('data_structures.html', **kwargs)

@app.route('/conditionals/')
def conditional():
    company = "Apple"
    return render_template('conditional_basic.html', company=company )

@app.route('/for-loop/')
def render_loop():
    planets = [
        "Mercury",
        "Venus",
        "Earth",
        "Mars",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune",
    ]

    user_os = {
        "Bob Smith": "Windows",
        "Anne Pum": "MacOS",
        "Adam lee": "Linux",
        "Jose Salva": "Windows"
    }
    return render_template('loops_and_conditionals.html', planets=planets, user_os=user_os )