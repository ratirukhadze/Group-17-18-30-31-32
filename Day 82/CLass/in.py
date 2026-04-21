class Myclass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f"Welcome{self.name} Name: {self.name}, Age: {self.age}"     
    
New_Myclass = Myclass("Rati", 13)
print(New_Myclass.info())

new_Person = Person({"fname": "Rati", "lname": "Rukhadze"})


class Zebra(Person):
    def __init__ (self, fname, lname):
        Person.__init__(self, fname, lname)
        

print(new_Person)        