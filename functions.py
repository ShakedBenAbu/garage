from classes import Car
import pickle

def load():
    try:
        with open("cars.pickle", "rb") as f:
            cars=pickle.load(f)
            return cars
    except:
        return [Car()]

def add(name:str="name", year:int=0, color:str="color", number:str="0", owner:str="owner", visit_date:str="", service_date:str=""):
    cars=load()
    cars.append(Car(name=name, year=year, color=color, number=number, owner=owner, visit_date=visit_date, service_date=service_date))
    with open("cars.pickle", "wb") as f:
        pickle.dump(cars, f)       

def save(contacts:list):
    with open("contacts.pickle", "wb") as f:
        pickle.dump(contacts, f)

def delete(name):
    contacts=load()
    for contact in contacts.copy():
        if contact.name==name:
            contacts.remove(contact)
    save(contacts)

def update(name, new_phone):
    add(name, new_phone)
    delete(name)

def search(query):
    cars=load()
    results=[]
    for car in cars:
        if query in car.name or query in car.number:
            results.append(car)
    return results                

