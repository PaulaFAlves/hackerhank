"""
Objective
In this challenge, we're going to learn about the difference between a class and an instance; because this is an Object Oriented concept, it's only enabled in certain languages. Check out the Tutorial tab for learning materials and an instructional video!

Task
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign initialAge to age after confirming the argument passed as initialAge is not negative; if a negative argument is passed as initialage, the constructor should set age to 0 and print Age is not valid, setting age to 0.. In addition, you must write the following instance methods:

yearPasses() should increase the  instance variable by .
amIOld() should perform the following conditional actions:
If age < 13, print You are young..
If age >= 13 and age < 18, print You are a teenager..
Otherwise, print You are old..
"""

class Person:
    def __init__(self,initialAge):
        self.age = initialAge
        if age <= 0:
            print('Age is not valid, setting age to 0.')
        else:
            self.age = initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        elif self.age >=18:
            print('You are old.')
        
    def yearPasses(self):
        self.age += 1

t = int(input()) # how many ages are gonna be given
for i in range(0, t): # loop lenght acoording to the number given before
    age = int(input())  # an age are asked     
    p = Person(age)  # p object is instanced
    p.amIOld() # call the amIOld method inside p object
    for j in range(0, 3): # for 3 times, call the method yearPasses, to increases the age by 3
        p.yearPasses()       
    p.amIOld() # call amIOld method again, with the new age
    print("")