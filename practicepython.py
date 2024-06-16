# print('hello')
# a=1
# b=2
# print(a+b)
# typecasting(explicit(mai jo karunga))
# a='4'
# b='2'
# print(int(a)+int(b))
# string="15"
# number=7
# string_number=int(string)
# sum=number+string_number
# print('the sum of the both number is ',sum)

# implicit conversion(jo python khud karega)

# c=1.9
# d=8
# print(c+d)
# a=7
# print(type(a))
# b=3.0
# print(type(b))
# c=a+b;
# print(c)
# print(type(c))
# TAKING INPUT
# a=input()
# print(a)
# b=input('enter the name:')
# print('print the name:',b)

# STRING
# name="Satyam"
# friend="Madhav"
# print("hello,"+name)
# apple='''He said,\" I want to
# eat an apple"'''

# print(apple)
# print(name[0])
# for character in apple:
#     print(character)
# for charac in name:
#   print(charac)
# print(name.upper())

# STRING SLICING

# names="satyam kumar"
# print(names[0:6])
# print(len(names))
# fruit="mango"
# leng1=len(fruit)
# print('Mango is a',leng1,
#      'letter word')
# print(fruit[:5])
# print(fruit[1:5])
# print(fruit[:])
# print(fruit[-2:-1])
# # yanha -2 means (length -2) tak delete karo
# # yanha -1 means (length -1)  tak delete karo o/p-only g
# nm="harry"
# print(nm[-4:-2])

# STRING METHOD
# String are imutable
# name='satyam'
# print(len(name))
# print(name.upper())
# print(name.lower())
# a='!!!satyam!!!! !!!!!!!'
# print(a.rstrip('!'))
# print(a.replace('satyam', 'aryan'))
# print(a.split(" "))
# blogheading='introduction to python'
# print(blogheading.capitalize())
# str1='welcome to console andt console it!!'
# print(len(str1))
# print(len(str1.center(50)))
# print(str1)
# print(str1.count('console'))
# print(str1.count('t'))
# print(str1.count('o'))
# print(str1.endswith('!!'))
# print(str1.endswith('to',4,10))
# str="he's run but he is still standup"
# str="123456"
# print(str.find("4"))

# DECISION MAKING
# a=int(input('Enter your input:'))
# print('Your age is:')
# if(a>18):
#   print('you can drive')
# else:
#   print('you cannot drive')
# for i in range(12):
#   if(i==10):
#     break
#   print("5 X",i+1,"=",5*(i+1));
# for i in range(1,15):
#   if(i==10):
#     break
#   print("9 X",i,"=",9*(i));
# FUNCTION

# def calculateGmean(a,b):
#   mean=(a*b)/(a+b)
#   print(mean)

# a=4
# b=3
# calculateGmean(a,b)
# def islesser(a,b):
# pass means function ke andar baad me code likhenge
#   pass
# def isGreater(a,b):
#     if(a>b):
#       print(a,'is greater than',b)
#     else:
#       print(b,'is greater than',a)
# a=5
# b=6
# isGreater(a,b)

# LIST
# marks=[3,5,6,"satyam",True]
# print(marks)
#                      [:]-> se list ka sara element print karwa sakte hai
# print(marks[:])
# print(marks[0])
# print(marks[1])
# print(marks[2])

# if 6 in marks:
#   print("yes")
# else:
#   print("no")
# if 7 in marks:
#   print("yes")
# else:
#   print("no")
# if "tya" in "satyam":
#   print('yes')

# list=[i for i in range(12) if(i%2==0)]
# print(list)

#                                            FUNCTION ARGUMENT
# def average(a,b):
#   print("The average is:",(a+b)/2)
# average(2,4);
#                 Default argument
# def average(a,b=1):
#   print("The average is:",(a+b)/2)
#    average(b=3,a=2)
# def name(fname,mname="John",lname="Whatson"):
#   print("hello",fname,mname,lname)
# name("satyam","kumar","yadav")
# average(b=3,a=2)

# function argument:==============
# def average(*numbers):
#   sum=0
#   for i in numbers:

#     sum=sum+i
#     print(sum)
#   # print("average is:",sum/len(numbers))
#   return sum/len(numbers)

# c=average(5,6,3,7,12)
# print(c)
# l=[11,23,44,52,1,3,5,1]
# print (l)
# l.sort()
# print(l)
# l.sort(reverse=True)
# print(l)
# l.append(7)

# print(l.index(23))
# print(l.count(1))
# m=l
# print(m)
# m[0]=0
# print(l)
# m=l.copy()
# m[0]=0
# print(l)
# print(m)
# l.insert(1,345)
# print(l)
# m=[100,200,300]
# l.extend(m)
# print(l)
# k=m+l
# print(k)
# TUPLES
# tup=(1,2,3,55,66,44,"satyam","red")
# # tup[0]=90
# # print(type(tup),tup)
# # print(tup[0])
# # print(tup[1])
# # print(tup[-1])
# # print(tup[3])
# # print(tup[4])
# # print(tup[5])
# # print(tup[6])
# # print(tup[7])
# # print(tup[8])
# print(len(tup))
# if 53 in tup:
#   print("it is present")
# else :
#   print("not present")

# tup2=tup[1:5]
# print(tup2)
# countries=("india","srilanka","japan","israil")
# cont=("vnj","favk","hfbahlbl")
# print(countries)
# temp=list(countries)
# print(temp)
# temp.append("russia")
# print(temp)
# temp.pop(2)
# print(temp)
# temp[2]="afganistan"
# print(temp)
# countries=tuple(temp)
# print(countries)
# new=countries+cont
# print(new)

#                              f-string

# letter ="MY name is {1} and from belong from {0}"
# country="India"
# name="satyam"
# letter.format(name,country)
# print(letter.format(name,country))
# print(f"MY name is {name} and from belong from {country}")
# price=49.89999999
# txt=f"For only {price:.2f} dollars!"
# print(txt)
# print(txt.format(price=49.89999999))
# date=12
# txt=f"their date birth is{date}"
# print(txt)
# print(f"{2*30}")
# print(f"{2+2*2}")

# docstring
# def square(n):
#   '''Takes in a number n, returns the square of  n'''
#   print(n**2)
# square(5)
# print(square.__doc__)

# Recursion
# def factorial(n):
#   if(n==0 or n==1):
#       return 1
#   else:
#      return n*factorial(n-1)

# print(factorial(5))
# print(factorial(3))
# def fab(n):
#   if(n==0 or n==1):
#     return n
#   fab(0)=0
#   fab(1)=1
#   return fab(n)=fab(n-1)+fab(n-2)
# print( fab(3))
# SETS

# a={2,4,2,6}
# print(a)
# for i in a:
#   print(i)
#                Emptyset
# harry={}
# ram=set()
# print(type(harry))
# print(type(ram))

# set method
# s1={1,2,5,6}
# s2={3,6,7}
# print(s1.union(s2))
# print(s1.intersection(s2))
# s1.update(s2)
# print(s1)
# s3={"ram","satyam","aryan"}
# s4={"ram","ankush","shayam"}
# s3.add("ganesh")
# s4.remove("ankush")
# s3.discard("ankush")
# item=s3.pop()
# print(item)
# print(s3.union(s4))
# print(s3.intersection(s4))

#    symmetric difference(jo common hai usko hatakar jo aata hai)

# s5=s3.symmetric_difference(s4)
# print(s5)

# DICTIONARY
# dic={
#   "Harry":"human being",
#   "spon":"Object"
# }
# # print(dic["Harry"])
# # dic={
# #    355:"Harry",
# #   346:"satyam",
# #   743:"aryan",
# #   23:"minsu"
# #  }
# # print(dic[346])
# # print(dic.get(347))
# # print(dic.keys())
# # print(dic.values())
# # for key in dic.keys():
# #   print(f"The value corresponding to the key:{key} is {dic[key]}")
# print(dic.items())
# for key,value in dic.items():
#    print(f"The value corresponding to the key:{key} is {value}")

# dictionary Method
# ep1={122:45,123:89,567:69,670:69}
# ep2={222:67,677:98}

# # ep1.update(ep2)
# # print(ep1)
# # ep1.clear()
# # ep1 khali
# # print(ep1)
# # empt={}
# # print(empt)
# # ep1.pop(122)
# # ep1.popitem()
# print(ep1)
# # del ep1
# del ep1[122]
# print(ep1)

#         for with else
#  yanha loop break  hone ke baad else print huwa

# for i in range(5):
#   print(i)

# else:
#   print("sorry no i")

# yanha break means kam khatm ho gya isliye else print nhi hoga

# for i in range(6):
#   print(i)
#   if i==4:
# i=0
# while i<7:
#   print(i)
#   if i==4:
#     break
#   i=i+1

# else:
#   print("sorry no i")

# a=input("Enter the number : ")
# print(f"Multiplication of{a} is:")
# for i in range(1,11):
#   print(f"{(int)(a)} X {i} ={(int)(a)*i}")

# TRY AND EXCEPT
# try:
#   for i in range(1,11):
#     print(f"{int(a)} X {i}= {int(a)*i}")
# except:
#   print("Invalid number")

# print("some important of cade")
# print("end of the code")

#             SHORTHAND IF ELSE

# a = 3308
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B")

# print(9) if a > b else ""

# c=9 if a>b else ""
# print(c)

#                      ENUMERATE FUNCTION
# marks = [12, 43, 54, 65, 24, 45, 23, 15]
# for index, mark in enumerate(marks):
# for index, mark in enumerate(marks, start=1): indexing 1 se start ke liye

# yanha enumerate function marks ko mark ke sath us element ka index bhi pass karta hai
# print(index, mark)
# if (index == 3):
#   print("satyam, awesome")

#IMPORT

# import math as m
# print(m.floor(4.567))
# from math import sqrt,pi
# result=sqrt(9)*pi
# print(result)

# from math import *
# # * means all function and variable
# result=sqrt(9)*pi
# print(result)

# from taking import welcome,satyam
# welcome()
# print(satyam)
# import taking
# taking.welcome()

#            GLOBAL AND LOCAL VARIABLES
# x=10;# global variable
# def my_function():
#   global x #means abb x ka value 4 hai jo ki global hai(global variable change kar rahe hai)
#   x=4
#   y=5 #local variable
#   print(y)

# my_function()
# print(x)

#            File Input/output
# READING A FILE

# f=open('myfile.txt','r') # it just only open the file

# text=f.read() # it read the file
# print(text)
# f.close()

# f=open('myfile2.txt','w') #here myfile2 automatically created

#  WRITING A FILE

# f=open('myfile.txt','w')
# f.write('hello,satyam')
# f.close()

# with open('myfile.txt','a') as f:
#   f.write("hey i am inside with")  # yanha with ke help se file humko close nahi karna padega

# f=open('myfile.txt','r')
# while True:
#   line=f.readline()
#   print(line)
#   if not line:
#     # print(line,type(line))
#     break

# f=open('myfile.txt','r')
# i=0
# while True:
#   i=i+1
#   line=f.readline()
#   if not line:
#     break
#   m1=line.split(",")[0]
#   m2=line.split(",")[1]
#   m3=line.split(",")[2]
#   print(f"Marks of student {i} is Maths is: {m1}")
#   print(f"Marks of student {i} is science is: {m2}")
#   print(f"Marks of student {i} is sst is: {m3}")
# print(line)

# f=open('myfile2.txt','w')
# lines=['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()

# with open("myfile.txt", 'r') as f:
#   print(type(f))
#   f.seek(10)# move to 10 bite of letter including space in the file

#   print(f.tell())# ye batlata hia khana tak seek function use huwa hai
#   data = f.read(5)#  after 10 byte print 5 letter
#   print(data)

# with open('sample.txt','w') as f:
#   f.write("hello world")
#   f.truncate(5)# ye batlata hai ki kitna letter likhna hai file mai

#LAMBDA functions

# def double(x):
#   return x*2

# double=lambda x:x*2
# avg=lambda x,y,z:(x+y+z)/2
# print(double(2))

# print(avg(3,5,10))

#  function ke andar function pass karna hai
# def app(fx,value):
#   return 6+fx(value)
# cube=lambda x:x*x*x

# print(app(cube,2))

#         MAP FILTER AND REDUCE
# cube=lambda x:x*x*x
# l=[1,2,3,4,5,6]
# newl=[]
# for item in l:
#   newl.append(cube(item))

# newl=list(map(cube,l))
# print(newl)

#FILTER(it is just like a condition )

# def filter_function(a):
#   return a>4     # here a>4 is condtion  if condtion is true then filter allow to enter the element in list

# newnewl=filter(filter_function,l)
# print(list(newnewl))

#REDUCE
# from functools import reduce

# def mysum(x,y):
#   return x+y

# sum=reduce(mysum,l)

# print(sum)

#                    'is' vs '=='
# a=4
# b="4"
# print(a is b)  #exact location of object in memory
# print(a==b)  # it check the value

# a=[1,2,3,4,5]
# b=[1,2,3,4,5]
# print(a is b)
# print(a==b)

#         OOPs

# class person:
#   name="satyam"
#   occupation="software developer"
#   networth=10000000
#   def info(self): #  self means woo object jiske liye self ko call kiya jaa raha hai
#     print(f"{self.name} is a {self.occupation}")
# b=person() # yanh b ko object banaye hai jo person ka blueprint use karta hai
# a=person() # yanha a ko object banaye hai

# a.name="satyam kumar"
# a.occupation="Accountant"
# a.info() #yanha self means 'a' object
# b.name="satya"
# b.info()
#CONSTRUCTOR

# class person:
#   def __init__(self , name, occ):
#     print("Hey I am a person")
#     self.name=name
#     self.occ=occ
#   def info(self):
#     print(f"{self.name} is a {self.occ}")

# a=person("satyam","software developer")
# a.info()

#Decorators
# this is basically decorator function means agar bar bar print karwana hai good morning
# def greet(fx):
#   def mfx(*args,**kwargs):
#     print("good morning")
#     fx(*args,**kwargs)
#     print("Thanks for using the function")
#   return mfx

# @greet
# def hello():
#   print("hello world")
# @greet
# def add(a,b):
#   print(a+b)

# # greet(add)(1,3) # agar hum log @greet use na kare add function ke aage
# add(1,3)

#                     GETTER AND SETTER

# class MyClass:
#   def __init__(self,value):
#     self._value=value
#   def show(self):
#     print(f"Value is {self._value}")

#   @property #getter
#   def ten_value(self):
#     return 10*self._value
#   @ten_value.setter  #setter
#   def ten_value(self,new_value):
#     self._value=new_value/10
# obj=MyClass(10)
# obj.ten_value=67;
# print(obj.ten_value) #getter
# obj.show()

#Inheritance

# class Employee:
#   def __init__(self,name,id):
#     self.name=name
#     self.id=id

#   def showDetails(self):
#     print(f"The name of Employee:{self.id} is {self.name}")

# class programmer(Employee):
#    def showLanguage(self):
#     print("The default language is python")
# e1=Employee("satyam",123)
# e1.showDetails()

# Access modifier
# 1.public it can easily acess from outside
# 2.private

# class Employee:
#   def __init__(self):
#     self.__name="satyam"  # __indicate the private
# a=Employee()
# # print(a.__name) it is not accessble
# # to access the private by indirctly (it is name mangling concept)(obj._classname__value)
# print(a._Employee__name)

# static method:- it help to write a functionin class without use  of self

# class Math:
#   def __init__(self,num):
#     self.num=num
#   def addtonum(self,n):
#     self.num=self.num+n

#   @staticmethod #here we can define the function without self in class
#   def add(a,b):
#     return a+b

# m=Math(5)
# print(m.num)
# m.addtonum(6)
# print(m.num)

# print(Math.add(7,2))
# print(m.add(7,3))

# Instance and class variable

# class method

# class Employee:
#   company="Apple"
#   def show(self):
#     print(f"The name is {self.name} and company is {self.company}")
#   @classmethod
#   def changecompany(cls,newcompany):
#     cls.company=newcompany

# e1=Employee()
# e1.name="satyam"
# e1.show()
# e1.changecompany("Tesla")
# e1.show()

# class Methods as Alternative Constructors

#

# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

#   @classmethod
#   def from_string(cls, string):
#     name,age=string.split(',')
#     return cls(name,int(age))

# person=Person.from_string("John Doe,38")
# print(person.name,person.age)

#          kisi class ke bare me jankari nikalna hai toooo

# x=[1,2,3]
# print(dir(x))# return all the method of class
# print(x.__add__)
# class Person:
#   def __init__(self,name,age):
#     self.name=name
#     self.age=age

# p=Person("John",30)
# print(p.__dict__) #dict means self ke sath jitna property include hai
# print(help(Person))

                            # OOPS
# class Person:
#   def __init__(self):
#     self.name="satyam"
#     self.gender="male"

# p=Person()
# print(p.name)
# q=p
# print(q.name)

# class Person:
#   def __init__(self,name,gender):
#     self.name=name
#     self.gender=gender

# def greet(person):
#   print("my name is :",person.name, "and I am a",person.gender)
# p=Person("satyam","male")
# greet(p.__doc__)
# 1.collection of object
# class Person:

#   def __init__(self, name, gender):
#     self.name = name
#     self.gender = gender

# p1 = Person('Rakesh', 'male')
# p2 = Person('Vikash', 'male')
# p3 = Person('satyam', 'male')

# # l=[p1,p2,p3]
# d = {'p1': p1, 'p2': p2, 'p3': p3}

# for x in d:
#   print(d[x].name)
#   print(d[x].gender)


#                                 AGGREGATION== when two class have a has relationship
# class Customer:
#   def __init__(self,name,gender,address):
#     self.name=name
#     self.gender=gender
#     self.address=address
#   def print_address(self):
#     print(self.address.get_city(),self.address.pin,self.address.state)

#   def edit_profile(self,new_name,new_city,new_pin,new_state):
#     self.name=new_name
#     self.address.edit_address(new_city,new_pin,new_state)

# class Address:
#   def __init__(self,city,pin,state):
#     self.__city=city
#     self.pin=pin
#     self.state=state

#   def get_city(self):
#     return self.__city

#   def edit_address(self,new_city,new_pin,new_state):
#     self.__city=new_city
#     self.pin=new_pin
#     self.state=new_state

# add=Address('Hazaribag',825411,'jharkhand')
# cus1=Customer('satyam','male',add)

# cus1.print_address()

# cus1.edit_profile('amit','mumbai',111111,'Maharastra')
# cus1.print_address()


#                      INHERITANCE
#  parent class
# class User:
#   def __init__(self):
#     self.name='satyam'

#   def login(self):
#     print('login')
# #  child class

# class Student(User):
#   # def __init__(self):
#   #   self.rollno=100

#   def enroll(self):
#     print('enroll into the course')

# u=User()
# s=Student()

# print(s .name)
# # print(s.rollno)
# s.login()
# s.enroll()


# class Parent:
#   def __init__(self,num):
#     self.__num=num

#   def get_num(self):
#     return self.__num

# class Child(Parent):
#   def show(self):
#     print("This is in child class")

# son =Child(100)
# print(son.get_num())
# son.show()



#  Method overrinding
# agar parent class has methodand child class has a method and both has same method or agar hum call karte hai child ko menas child ka object create karte hai tab child ka mehtod ko output dega na ki parent wala method ka

# super keyword class ke andar hot ahai or woo class child calss hoga and class ke bhahar super keyword ko use nahi kar sakte hai

#  super keyword se hum attribute/variable ko access nahi kar sakte onl

# class Phone:
#   def __init__(self,price,brand,camera):
#     print("Inside phone constructor")
#     self.__price=price
#     self.brand=brand
#     self.camera=camera

#   def buy(self): 
#     print("Buying a Phone")

# class SmartPhone(Phone):
#   def buy(self):
#     print("buying a Smartphone")
#     # syntax to call parent ka buy method
#     super().buy()



# # @methodoverriding

# s=SmartPhone(2000,'Apple',12)
# s.buy()

# multilevel inheritance
# class Product:
#   def review(self):
#     print("Product customer review")

# class Phone(Product):
#   def __init__(self,price,brand,camera):
#     print("Inside phone constructor")
#     self.__price=price
#     self.brand=brand
#     self.camera=camera

#   def buy(self):
#     print("buying a phone") 
  
# class SmartPhone(Phone):
#    pass
# s=SmartPhone(2000,'Apple',12)

# s.buy()
# s.review()






# import numpy as np

# a=np.arange(10000000)
# b=np.arange(10000000,20000000)
# start=time.time()

# c=a+b
# print(time.time()-start)












# NUMPY
# import numpy as np
# # arr=np.array((1,2,3,4,5))
# arr=np.array(42)
# print(arr.ndim)
# print(arr)

# import numpy as np
# arr=np.array([1,2,3,4,5])
# # print(arr[1])

# print(arr[2]+arr[3])

# import numpy as np

# arr=np.array([[1,2,3,4,5], [6,7,8,9,58]])
# print(arr[0,2])
# print(arr[1,3])
# print(arr[1,4])
# import numpy as np

# arr=np.array([[1,2,3,4,5] ,[6,7,8,9,25]])
# print(arr[ -1])
# print(arr.dtype)

# arr=np.array([1,2,3,4,5], dtype='S')
# print(arr)

# arr=np.array([1,2,3,4,5], dtype='i4')

# print(arr)
# print(arr.dtype)

# arr=np.array([1.1,2.1,3.1])
# newarr=arr.astype('i')

# print(arr.dtype)
# print(newarr.dtype)

# arr=np.array([1,2,3,4,5])
# x=arr.copy()
# arr[0]=23
# print(x)

# arr=np.array([1,2,3,4,5])
# x=arr.view()
# arr[0]=42
# print(arr)
# print(x)

# arr = np.array([[1, 2, 3, 4,6],[5,6,7,8,4]])

# x = arr.copy()
# y = arr.view()

# print(x.base)
# print(y.base)
# arr=np.array([1,2,3,4,5,6,7,8] )
# newarr=arr.reshape(3,3)
# # print(newarr.ndim)

# print(newarr)
# arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# print(arr.reshape(2, 4).base)

# arr=np.array([[1,2,3,4],[5,6,7,8]])
# for x in arr:
#   for y in x:
#     print(y)

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# for x in arr:
#  for y in x:
#    for z in y:
#      print(z)

# arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# for x in np.nditer(arr):
#   print(x)

# import numpy as np

# np.array([1,2,3])

# b=np.array([[1,2,3],[4,5,6]])
# print(b)
# a=np.array([1,2,3],dtype=float)
# print(a)

# a=np.arange(1, 11)
# print(a)
# b=np.arange(1,11,2)
# print(b)

# x=np.arange(1,11).reshape(2,5)
# print(x)
# a=np.ones((3,4)) #use to initialize the array
# print(a)

# a=np.zeros((2,3))
# print(a)
# e=np.random.random((3,4))
# print(e*10)
# x=np.linspace(-23,10,10)
# print(x)
# y=np.identity(4)
# print(y)
                      #IMPORTANT IN NUMPY
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(3,4)
# # print(a1*2)
# # print(a1**2)
# # print(a1>5)
# print(np.min(a1))
# print(np.max(a1))
# print(np.sum(a1))
# print(np.prod(a1))
# print(np.max(a1,axis=1)) #yanha row or col me max number ko find out karn a hai or axis me 0-> column and 1-> row . is trah hum min , sum , prod ka bhi karsakete hai 

      #  MEAN, MEDIAN, STANDARD DEVIATION , VARIANCE, TRIGO
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(3,4)
# x=np.mean(a1)
# print(x)
# yanha par bhi flexibilty hai ki row wise or column wise hum nikal sakte hai by the jhlp of axis for example
# print(np.mean(a1,axis=1)) # row
# print(np.mean(a1,axis=0)) #col

# print(np.median(a1,axis=1))
# print(np.median(a1,axis=0))

# print(np.std(a1,axis=1))

# print(np.var(a1,axis=0))

# print(np.sin(a1))  # yanha har element ka sin functon nikala hai but kabhi use nahi karna hai 


          #DOT PRODUCT use for dot product of two materices
# import numpy as np
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(4,3)
# x=np.dot(a1,a2)
# print(x)

                     #LOG AND EXP FUNCTion
# import numpy as np
# a1=np.arange(12).reshape(3,4)
# a2=np.arange(12,24).reshape(4,3)
# print(np.log(a1))

# print(np.exp(a1))

#                   rOUND, FLOOR, CEIL
# x=np.random.random((2,3))   random number ko inter me convert karna ke keliye
# x=np.round(np.random.random((2,3))*100)
# print(x)

#                    INDEXING AND SLICING
# a1=np.arange(12)
# a2=np.arange(12).reshape(3,4)
# a3=np.arange(8).reshape(2,2,2)
# print(a1)
# print(a1[-1])# last element
# print(a1)
# print(a2)
# print(a2[2,3])
# print(a3)
# print(a3[1,0,1])
# print(a3[1,1,1])

# print(a1[2:5:2])
# print(a2)
# print(a2[2,:])  #dushra row ka sara element
# print(a2[:,1])  #1 index ka sara element
# print(a2[1:,1:3])
# print(a2[::2,::3])  #::2 means row me alternates ko print karega and ::3 me col me pahla element ke baad fir thisra element
# print(a2[::2,1::2])
# print(a2[1,::3])
# print(a2[0:2,1:4])
# a3=np.arange(27).reshape(3,3,3)
# print(a3)
# print(a3[2,1:,1:])
# print(a3[0])
# numpy vs python list
# numpy faster isiliye hai kyunki ye c type language ka array jo ki static hota hai
# a=[i for i in range(10000000)]
# b=[i for i in range(10000000,20000000)]

# c=[]
# import time
# start=time.time()
# for i in range(len(a)):
#   c.append(a[i]+b[i])
# print(time.time()-start)




# in comparision to size
# a=[i for i in range(10000000)]
# to find the memory occupies in system we use module sys
# import sys

# x=sys.getsizeof(a)

# print(x)
# import numpy as np
# b=np.arange(10000000,dtype=np.int32)
# y=sys.getsizeof(b)
# print(y)


# Advanced Indexing


# Fancy indexing
# import numpy as np
# a=np.arange(24).reshape(6,4)
# print(a)

# print(a[[0,2,3,5]])
# print(a[:,[1,3]])

# boolean indexing

# import numpy as np

# a=np.random.randint(1,100,24).reshape(6,4)
# print(a)


# # find all number greater than 50
# # print(a>30)
# # print(a[a>30])

# # find the even number
# print(a%2==0)
# print(a[a%2==0])

# # find all number greater then 50 and divisible by 2
# print((a>50) & (a%2==0))
# print(a[(a>50) & (a%2==0)])


          # BROADCASTING :- ye batlata hai ki numpy kaise do different shape wale array ko kaise treate karta hai while using arithmetic operation

# import numpy as np
# a=np.arange(6).reshape(2,3)
# b=np.arange(3).reshape(1,3)
# print(a)
# print(b)
# print(a+b)

import numpy as np
# a=np.arange(12).reshape(4,3)
# b=np.arange(3)

# print(a)
# print(b)
# print(a+b)

# b=np.arange()

# a=np.arange(3).reshape(1,3)
# b=np.arange(8).reshape(4,1)

# print(a+b)



#           Working with mathematical formulas

# a=np.arange(10)
# print(np.sum(a))
# print(np.sin(a))

      # 1.Sigmoid function  S(x)=1/(1+e ka power -x)
# def sigmoid(array):
#   return 1/(1+np.exp(-(array)))

# a=np.arange(100)
# x=sigmoid(a)
# print(x)

#                         2.mean square error
# actual=np.random.randint(1,50,25)
# predicted=np.random.randint(1,50,25)

# print(actual)
# print(predicted)

# def mse(actual,predicted):
#   return np.mean((actual-predicted)**2)

# print(mse(actual,predicted))

# 3.                     missing value

# a=np.array([1,2,3,np.nan,4])
# print(a)

# # how to remove missing value

# y=np.isnan(a)
# print(y)
# print(a[~np.isnan(a)])


                # PLOTTING GRAPH
# plotting a 2D plot
# import matplotlib.pyplot as plt
# x=np.linspace(-10,10,100)
# y=x
# plt.plot(x,y)

# import numpy as np
# import matplotlib.pyplot as plt
# x=np.linspace(-10,10,100)

# y=1/(1+np.exp(-x))
# plt.plot(x,y)

#                               np.sort(ye sort karne ke baad numpy array return karta hai)
# import numpy as np
# a=np.random.randint(1,100,15)

# print(a)
# b=np.random.randint(1,100,24).reshape(6,4)
# print(b)

# print(np.sort(a)) accending order
# print(np.sort(a)[::-1]) decending order

# print(np.sort(b,axis=0)) column wise sorting
# print(np.sort(b,axis=1)) row wise sorting


# print(np.append(a,200))
# print(np.append(b,np.ones((b.shape[0],1)),axis=1))

# np.concatenation(yahan do ye usse jayda multiple 2d array ko concat karna hai )

# import numpy as np
# a=np.arange(6).reshape(2,3)
# b=np.arange(6,12).reshape(2,3)

# print(np.concatenate((a,b),axis=0))

# np.unique
# e=np.array([1,1,2,2,3,3,4,4,5,5,6,6])
# print(e)
# print(np.unique(e))

# np.expand_dims(iske madad se 1 dimensional array se two dimensional me convert karta hai)

# import numpy as np
# a=np.arange(15)
# print(a)
# print(a.shape)
# print(np.expand_dims(a,axis=1))

#                         np.where(iske madad se findout karte hai indices after satisfying the condition)-> index deta hai

# import numpy as np
# a=np.random.randint(1,100,20)
# print(a)
# print(np.where(a>50))

# replace all value >50 with 0 (np.where(condition,true,false))

# print(np.where(a>50,0,a))
# print(np.where(a%2==0,0,a))

#                   np.argmax(ise array ka maximum element ka postion ka index deta hai)
# import numpy as np
# a=np.arange(6)
# b=np.arange(6,12).reshape(3,2)
# print(a)
# print(b)
# # print(np.argmin(a))
# print(np.argmax(b))

                         # np.cumsum (issme pahle wala number add hote jata hai)
# import numpy as np
# a=np.arange(12).reshape(4,3)
# print(a)
# print(np.cumsum(a,axis=0))
# print(a)
# print(np.cumsum(a))
              # np.cumprod
# import numpy as np
# a=np.arange(1,12)
# print(np.cumprod(a))

                      # np.percentile
# import numpy as np
# a=np.arange(12)
# print(a)
# print(np.percentile(a,50))

                      # np.median
# import numpy as np
# a=np.arange(20)
# print(a)
# print(np.median(a))

                    # np.histogram( count frequncy)
# import numpy as np
# a=np.random.randint(1,100,50)
# print(a)
# print(np.histogram(a,bins=[0,10,20,30,40,50,60,70,80,90]))
                     
                    # np.corrcoef(correlation cofficient)

 # np.isin()

# np.flip()- just reverse the array

# import numpy as np
# a=np.arange(12)
# print(a)
# print(np.flip(a))

# np.put()- array me diye gaye elemnt ko update karna ho to

# import numpy as np
# a=np.random.randint(1,200,10)
# print(a)
# print(np.put(a,[1,3],[110,130]))


# np.delete-jisko delete karna hai uska index do

# import numpy as np

# a=np.arange(12)
# print(a)
# print(np.delete(a,1))

#                                 Set functions







                  #  PANDAS(library of javascript)


# there are two object in pandas 1.series2.datarames
# series-like a column in table. it gives the index and value

import numpy as np
import pandas as pd


# list ke madad se
# names=["satyam","Aryan","samjeet","madhav"]
# print(pd.Series(names))

# nums=[12,23,34,45]
# print(pd.Series(nums))
# print(pd.Series(nums,index=names,name="friend ka number"))

# Dictionary ke madad se

# marks={
#   "math":67,
#   "English":89,
#   "hindi":90,
#   "Science":99
# }
# print(pd.Series(marks,name="Rishu ka marks"))
# print(pd.Series(marks).size)
# print(pd.Series(marks).dtype)
# print(pd.Series(marks).name)
# print(pd.Series(marks).is_unique)# is_unique -key key-value unique hona chahiye

# print(pd.Series(np.arange(8)).is_unique)
# print(pd.Series(marks).index)
# print(pd.Series().values)




