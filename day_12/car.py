class Car:
    def __init__(self, make, model, year):
        self.car_make = make
        self.car_model = model
        self.car_year = year

    def print_car(self):
        print("{} {} {}".format(self.car_make, self.car_model, self.car_year))

    def honk(self):
        print("honk")
