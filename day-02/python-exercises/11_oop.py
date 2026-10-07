# Classes, Objects, Inheritance and Encapsulation

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary

    def show_details(self):
        print("Name:", self.name)
        print("Salary:", self.__salary)

class Developer(Employee):
    def show_language(self):
        print("Language: Python")

employee = Employee("Priya", 45000)
developer = Developer("Aarav", 60000)

print("Employee:")
employee.show_details()

print("\nDeveloper:")
developer.show_details()
developer.show_language()