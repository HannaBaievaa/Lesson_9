class Avto :
    def __init__(self, brand, color, volume):
        self.brand = brand
        self.color = color
        self.volume = volume

    def go_straight(self):
        return f"Avto {self.brand} goes straight"

    def go_back(self):
        return f"Avto {self.brand} goes back"

class New_Avto(Avto) :

    def go_right(self) :
        return f"Avto {self.brand} goes right"

    def go_left(self) :
        return f"Avto {self.brand} goes left"

my_car = Avto("Mazda6", "white", 1.8)
print("My avto is", my_car.brand)
print(my_car.go_straight())


family_car = New_Avto("BMW", "grey", 2.0)
print("Our family car color is", family_car.color)
print(family_car.go_left())


