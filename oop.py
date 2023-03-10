class Person:

    amount = 0  # Class variable

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1
        print("...object deleted!")

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name, self.age, self.height)

    def get_older(self, yrs):
        self.age = self.age + yrs


person1 = Person("Akshaya", 36, 178)
print(person1)
person1.get_older(5)
print(person1)

print(Person.amount)
person2 = Person("Olgamama", 23, 173)
print(Person.amount)
