class Emplyoee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def give_raise(self, increase=5000):
        self.salary += increase
