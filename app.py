import functions
from classes import Car
from flask import Flask, request, redirect, url_for, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", cars=functions.load(), car_props=Car().__dict__)

@app.route('/add')
def add():
    name=request.args["name"]
    year=request.args["year"]
    color=request.args["color"]
    number=request.args["number"]
    owner=request.args["owner"]
    visit_date=request.args["visit_date"]
    service_date=request.args["service_date"]
    functions.add(name=name, year=year, color=color, number=number, owner=owner, visit_date=visit_date, service_date=service_date)
    return redirect(url_for('home'))

@app.route('/delete')
def delete():
    number=request.args["number"]
    functions.delete(number)
    return redirect(url_for('home'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method=='POST':
        name=request.form["name"]
        phone=request.form["phone"]
        functions.update(name, phone)
        return redirect(url_for('home'))
    else:
        name=request.args["name"]
        phone=request.args["phone"]
        return render_template("update.html", name=name, phone=phone)

@app.route('/search')
def search():
    query=request.args["query"]
    results=functions.search(query=query)
    return render_template("index.html", cars=results, car_props=Car().__dict__)