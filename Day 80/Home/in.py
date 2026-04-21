
name = "GitHub Copilot"
print("1) name:", name)
print("   type:", type(name))


fruits = ["alma", "banani", "orenji"]  
print("\n2) fruits:", fruits)
print("   მეორე ელემენტი (index 1):", fruits[1])


student = {"name": "Niko", "age": 20, "grade": "A"}
print("\n3) student:", student)
print("   grade:", student["grade"])


colors = ("red", "green", "blue")
print("\n4) colors tuple:", colors)
try:
    colors[0] = "yellow"  
except TypeError as e:
    print("   შეცდომა:", e)


set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "kiwi", "cherry"}
print("\n5) set1:", set1)
print("   set2:", set2)
print("   გაერთიანება (union):", set1.union(set2))
print("   გადაკვეთა (intersection):", set1.intersection(set2))