"""

This program aims to exercise some OOP concepts in Python programming 
"""

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        
    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        
    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
            
            return value / len(self.students)
    

#Main program
s1 = Student("Bill", 19, 95)
s2 = Student("Jill", 19, 65)

course1 = Course("Python programming", 5)
course1.add_student(s1)

print(course1.add_student(s1))





#Inheritance exercises

"""
 Inheritance is when a class receives characteristics from an upper class also called superclass
        
"""

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am a {self.name} and I am {self.age} years old")
        
class Cat(Pet):
    def speak(self):
        print("Meow")
        
class Dog(Pet):
    def speak(self):
        print("Bark")
        
p = Pet("Tim", 19)
p.show()
#The output is "Im Tim and Im 19 years old" taken from the pet class

c = Cat("Bill", 34)
c.show()
#The output will also be "Im Bill and Im 34 years old" but this time is taken from the cat class that heritages from the pet class

d = Dog("Bill", 34)
d.speak()
#Here the output will be "Bark" because is working in the same way as the above line but is using the method speak in the Dog class

