class Car:
    # constructor
    def __init__(self, make, model, year, color):
        # attribute
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    # method
    def drive(self):
        print("This " + self.make + " is driving")

    def stop(self):
        print("This " + self.make + " is stopped")
