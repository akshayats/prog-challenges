# Inheritance
# Operator Overloading
class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, yrs):
        self.age += yrs


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary

    def __str__(self):
        text = super(Worker, self).__str__()
        text += " Salary: {}".format(self.salary)
        return text

    def calc_yearly_salary(self):
        return self.salary * 12


worker1 = Worker("Harisha", 37, 176, 2576)
print(worker1)
print(worker1.calc_yearly_salary())

# >>>>>>>>>>>>>>>>>>>


class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return "x: {}, y:{}".format(self.x, self.y)


v1 = Vector(3, 4)
v2 = Vector(4, -9)

print(v1 + v2)
print(v1 - v2)


