#A Class is like an object design, or a "blueprint" for creating objects.
class Person:
  def __init__(self, name, age):
    
    self.name = name
    self.age = age

  def GetAge(self):
    return self.age

  def GetName(self):
    return self.name

  def GetTypingSpeed(self):
    return self.typingSpeed
		
name = input("Enter Name")
age = int(input("Enter Age"))
p1 = Person(name, age)

if p1.GetAge() < 18:
  print(p1.GetName(), "is too young to vote")
else:
  print(p1.GetName(), "is old enough to vote")