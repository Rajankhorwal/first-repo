
#encapsulations
# class new1:
#     def __init__(self,name,name1):
#         self.nam=name1
#         print(name,"  ",self.nam)
#     def set(self,val):
#          self.__spy=val
#     def get(self):
#         return self.__spy
#
# f1=new1('rajan','janesh')
#
# print(f1.nam)
# f1=new1('rajan','shaqib')
#
# f1.set(3)
#
# f1.spy=4

# inheritance:
# class new1:


#     def set_value(self,width,height):
#          self.__width=width
#          self.__height=height
#     def set_wid(self):

#         return self.__width

#     def get_hei(self):
#         return self.__height

# class rec(new1):
#       def area(self):
#           return self.set_wid()*self.get_hei()

# r1=rec()
# r1.set_value(5,6)
# print(r1.area())


# multiple inheritance:

# class new1:


#     def set_value(self,width,height):
#          self.__width=width
#          self.__height=height
#     def set_wid(self):

#         return self.__width

#     def get_hei(self):
#         return self.__height

# class shape:
#       def color(self,name):
#           self.nam=name
#           print(self.nam)



# class rec(new1,shape):
#       def area(self):
#           return self.set_wid()*self.get_hei()
#       def shapecall(self):
#               self.color('rectangle')



# r1=rec()
# r1.shapecall()
# r1.set_value(5,5)
# print(r1.area())

# class new:
#     def __init__(self):
#         print("super class")
# class new2:
#     def __init__(self):
#         print("new1 class")
#     def fact(self,s):
#         list=[]
#         for i in range()

# class child(new2,new):
#     def __init__(self):
#         print("subclass")
#         super().__init__()
#         new.__init__(self)

# s=child()



# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def fact(self):
#          None
#     @abstractmethod    
#     def fact2(self):
#         NameError
# class B(A):
#     def fact(self):
#         print("hello")
# class C(B):
#     def fact2(self):
#         print("world")


# s=C()
# s.fact2()

# class Person:
#     age = 25

#     def printAge(cls,value):
#         cls.value=value
#         print('The age is:', cls.age,cls.value)

# # create printAge class method
# Person.printAge = classmethod(Person.printAge)

# Person.printAge(5)

# class Person:
#     age = 25

#     def printAge(value):
        
#         print('The age is:', age,cls.value)

# # create printAge class method
# Person.printAge = staticmethod(Person.printAge)

# Person.printAge(5)

# class Person:
#     age = 25

#     def printAge(cls,value):
#         cls.value=value
#         print('The age is:', cls.age,cls.value)

# # create printAge class method
# Person.printAge = classmethod(Person.printAge)

# Person.printAge(5)




# class Person:
#     age = 25

#     def printAge(cls,value):
#         cls.value=value
#         print('The age is:', cls.age,cls.value)

# # create printAge class method
# Person.printAge = classmethod(Person.printAge)

# Person.printAge(5)


# function that filters vowels 
def fun(x,y):
    if x<y:
        return x+y
def fun1(n):
    lis = [1, 2, 3, 4, 5]
    if n not in lis:
        return n



seq=[1,2,3]
seq1=[3,3,4]
x=map(fun,seq,seq1)
print(list(x))
z=[4,5,7]
y=filter(fun1,z)
print(list(y))




