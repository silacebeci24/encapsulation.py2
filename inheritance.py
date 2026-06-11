class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} is working.")


class Programmer(Employee):
    def code(self):
        print(f"{self.name} is writing code.")


worker = Programmer("Ali")

worker.work()
worker.code()
