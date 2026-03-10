class Car():
    brand = "BMW"
    model = "X5"
    year = 2020
    color = "Black"
    price = 60000

    def printDetails(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Price: {self.price}")

car = Car()

print(car.brand)
