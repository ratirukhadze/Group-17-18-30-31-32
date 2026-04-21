

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")
        print(f"Price: {self.price}")


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I am {self.name} and I am {self.age} years old.")


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def work(self):
        print(f"I work as an employee and my salary is {self.salary}.")


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


if __name__ == "__main__":
    
    book = Book("1984", "George Orwell", 328, 9.99)
    book.display_info()
    print()

    
    calc = Calculator()
    a, b = 10, 5
    print("Add:", calc.add(a, b))
    print("Subtract:", calc.subtract(a, b))
    print("Multiply:", calc.multiply(a, b))
    print("Divide:", calc.divide(a, b))
    print()

    
    emp = Employee("Alice", 30, 5000)
    emp.greet()
    emp.work()
    print()

   
    rect = Rectangle(3, 4)
    print("Rectangle area:", rect.area())