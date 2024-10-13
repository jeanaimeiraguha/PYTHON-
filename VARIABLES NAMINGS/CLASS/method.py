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
            """
class Person:
  def __init__(self, name1, lname , age):
    self.name1 = name1
    self.age = age
    self.lname = lname
  #method definition
  def myfunc(self):
    print("Hello my name is " + self.name1 + self.lname)
#object of class
p1 = Person("John","kubwimana", 36)
#function calling
p1.myfunc()
