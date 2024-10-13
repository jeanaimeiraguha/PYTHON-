"""

class Person:
    def __init__(self, firstName ,lastName, age,address):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.address=address
        # method 
        def mfunc(self):
            print("Welcome ") , self.firstName, self.age
            #object class
            p1=Person("Iraguha","Jean Aime" ,39)
            #function call
            p1.myfunc()
        """    """
class Person:
  def __init__(self, name1, lname , age):
    self.name1 = name1
    self.age = age
    self.lname = lname
  #method definition
  def myfunc(self):
    print("Hello my name is " + self.name1 + self.lname)
#object of class
p1 = Person("Iraguha","Jean AIme", 19)
#function calling
p1.myfunc()
"""
"""
class Animals:
   def __init__(self, an):
      self.an=an
      def myfunc(self):
      
         p1=Animals("cow")
         print("Welcome" + an)
         p1.myfunc()

"""
class Animal:  
    def speak(self):  
        print("Animal Speaking")  
#child class Dog inherits the base class Animal  
class Dog(Animal):  
    def bark(self):  
        print("dog barking")
#object definition  
obj = Dog()  
obj.bark()  
obj.speak() 
