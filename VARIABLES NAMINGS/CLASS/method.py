class Person:
    def __init__(self, firstName ,lastName, age,address):
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        self.address=address
        # method 
        def mfunc(self):
            print("Welcome ") , self.firstName, self.age