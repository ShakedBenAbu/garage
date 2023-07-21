class Car:
    def __init__(self, name:str="name", year:int=0, color:str="color", number:str="0", owner:str="owner", visit_date:str="", service_date:str=""):
        self.name=name
        self.year=year
        self.color=color
        self.number=number
        self.owner=owner
        self.visit_date=visit_date
        self.service_date=service_date

    def __str__(self):
        return f"{self.name}:{self.year}"        

    def __repr__(self):
        return f"{self.name}:{self.year}"        

    

