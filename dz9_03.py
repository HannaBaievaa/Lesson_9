class Parallelogram():
    def __init__(self,width, legth):
        self.width = width
        self.legth = legth

    def get_area(self):
        s = self.width * self.legth
        return f"Площа паралелограма : {s}"

parallelogram1 = Parallelogram(4, 8)
print(parallelogram1.get_area())

class Square(Parallelogram):
    def __init__(self, width):
        self.width = width

    def get_area(self):
        s = self.width ** 2
        return f"Площа квадрату : {s}"

kvadrat1 = Square (5)
print(kvadrat1.get_area())
