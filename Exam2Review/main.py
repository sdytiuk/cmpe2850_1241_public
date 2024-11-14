class vehicle:
    model = "X"
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"Brand: {self.brand}, Model: {self.model}"

    def __repr__(self):
        return 'I say I am a vehicle and my name is Ryan'

    def DivideWrong(self):
        return self.model / 0


class Car(vehicle):
    #variables declared here are class level
    #same as C# static...
    FavCar = "Tesla"
    def __init__(self,brand,model,year,num_doors=4):
        super().__init__(brand,model,year)
        Car.FavCar = model
        self.num_doors = num_doors

    def __str__(self):
        return super().__str__() + f", NumDoors: {self.num_doors}, FavCar: {Car.FavCar}"

class Motorcycle(vehicle):
    type = 'Motorcycle'
    def __init__(self,brand,model,year,engine_cc):
        super().__init__(brand,model,year)
        self.engine_cc = engine_cc
    def __str__(self):
        return super().__str__() + f", Engine CC: {self.engine_cc} Type: {Motorcycle.type}"


if __name__ == '__main__':
    vehicles=[Car("Toyota","Camry",2010),
              Car('Honda','Civic',2024),
              Motorcycle('Honda','250X',2009,
                         250)]
    for v in vehicles:
        print(v)

    print(vehicles[0].__repr__())
