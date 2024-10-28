#public -- anywhere
'''class Details:
    a=10
    def hi(self):
        print("hello world")
        return 0
    
b=Details()
print(b.a)
print(b.hi())
'''
# protected --only  for sub class
'''class Details:
    _a=10
    def hi(self):
        print("hello world")
        return 0
    
b=Details()
print(b._a)
print(b.hi())'''

#private --means only class
'''class Details:
    __a=10
    def hi(self):
        print("hello world")
        return 0
    
b=Details()
print(b.__a)
print(b.hi())'''

# to print variable in classs
'''class Actionanime:
    a='naruto'
    def charecters(self):
        print(" naruto\n sasukee\n itachi \n madhara")
        print("main charecter = ",self.a)
        return "keshimoto"
    
anime=Actionanime()
print(anime.a)
print(anime.charecters())'''

# Inheritance of the class

#---single inheritance
'''class Parent:
    def color(self):
        print("white")

class Child(Parent):
    pass

obj=Child()
obj.color()'''


#---multiple inheritance
class Father:
    def color(self):
        print("skin colour is white")
class Mother:
    def height(self):
        print("height is 6 Ft")
class Child(Father,Mother):
    pass

obj=Child()
obj.color()
obj.height()