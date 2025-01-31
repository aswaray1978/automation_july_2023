'''
# Primitive Data Types
a=10 # Python is a dynamically typed language and b/c of that we don't have to explicitly define the variable type.
#PVM --> Python virtual machine is running in the background and with the value, it automatically convert the variable type. 

b=10.5    #float data type
c="Gaurav"  # String data types can use single or double quotes
d = True # Boolean data type - capital T or F for True and False
e=10+20j  #complex data type --> used in mathimatical operations. Not going to use in Devops.

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

'''

#In-built functions

a=10

#print(dir(a))  #dir() will give a list of all the functions you can use with a data type.

# __sizeof__  --> double underscore<functionname>double underscore are known as magic methods. 

#String is a class and name is an object of that class. A class is a blueprint.

#print(dir(name))

#print(type(name))

#What is a class and what is an object?
#In python everything is an object. What is class  --> A class is a blueprint. String is a class 
# and name is an object of that class. Object is implementation of that class. name is an object.

#replace() function
#print(name.replace("O", "P")) #
name='Oti Edema' 

#split() function  --> split string into multiple parts. If not passing argument(s), it will take space as separator. No errors. 
#print(name.split("E"))
#print(dir(name))


#List, Tuple, Set, Dict

#List/Array: collection of heterogeneous data types or ordered elements

# l1=[1,"Ramon", False]
# l2=[1,2,3,4,5]
# l3=[]

#print(dir(list))

#'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

#l1.append("Rahul")
#print(l1)

# insert() function --> insert an element at a particular index 
#l1.insert(1,"Rahul")


#.Gaurav Pathak -->teacher

#length function len()
#print(len(l1))


# Note: What is difference between a function and a method?
# A function is something you define independently. A method is something you define inside a class.


# Define a function

def add(x,y):
    return x+y

#call a function
# sum=add(1,5)
# print(sum)

#Remove value  #pop() --> Removes the value feom the last index.

# l1=[1,10,20,30,40]
# l2=[1,2,3,4,5]
# l3=[]

# print(l1)
# l1.pop()

# print(l1)

#Remove function --remove a particular element --> i.e. remove(20)

# l1=[1,10,20,30,40]

# l1.remove(20)
# l1.remove(30)

# print(l1)

#Tuple --> A collection of elements, heterogeneous type, ordered. Immutable list

#Example of List
# l = [10,20,"abc", True]
# l[2] = "xyz"
# print(l)

# #Example of Tuple
# t=(10,20,"abc", True)
# t[2]="xyz"
# print(t)

#Immutability: All primitive data types are immutable in nature: int, float, string, bool

a=10
b=10

#Check memory address of a particular variable use id() function
# print(id(a))
# print(id(b))

# #List is mutable
# l1=[10,20,30,40]
# l2=[10,20,30,40]
# print(id(l1))
# print(id(l2))

# t1=(1,2,3)
# t2=(1,2,3)

# #This will compare the memory address for both and tell you if it's the same or not
# print(id(t1))
# print(id(t2))
# print(t1 is t2)

#Note: Tuple is nothing more than a immutable list.

t=(1,2,True, "Naveen", "Naveen")

#Findout what functions are available for tuple  --> count() and index()
#print(dir(tuple))


#print(t.count(1))  # --> returns 2

#Why is 1 returning 2 values of 1? B/c True equals 1 as well

#index() function --> will tell you when a value first occurred, index position.
#print(t.index("Naveen"))

#Set Data type --> a collection of elements but duplicates aren't allowed. It's unordered

# s1={10,20,"Rahul", "Chad", "Rahul",True, 20}
# print(s1)

# #Different functions for set()
# print(dir(set))

#add() function

# s1={10,20,"Rahul", "Chad", "Rahul",True, 20}
# s1.add("lwplabs")
#print(s1)


#discard() function
# s1={10,20,"Rahul", "Chad", "Rahul",True, 20}
# print(s1)
# s1.discard("Rahul")
# print(s1)


#pop() function  --> it randomly removes a value
# s1={10,20,"Rahul", "Chad", "Rahul",True, 20}
# s1.add("lwplabs")
# print(s1)
# s1.pop()
# print(s1)


#remove() function  --> explicitly remove an element from a a set
# s1={10,20,"Rahul", "Chad", "Rahul",True, 20}
# s1.add("lwplabs")
# print(s1)
# s1.remove("Chad")
# print(s1)


#Dictionary  => dict, map, hash-map. key: value pairs. Will use {}

# What type of variable are these; dictionary or set? default --> dictionary
# d={}
# s={}
# print(type(d))
# print(type(s))

#So how can we define an empty set? Use set() function
# m=set()
# print(type(m))

#Define dictionary and print a certain value  --> provide the key
#d1={"Name":"Hajj","Branch":"IT", "Roll_No":30, [10,20,30]:"xyz"}
# print(d1["Name"])

# #Update a value in a key
# d1["Branch"]="CS"
# d1["Name"]="Lavar"
# print(d1)

#Note:Dictionary's keys can't be mutable, but values can be mutable

#Integer is hashable. It will just return the value set for the variable.
# a=10
# print(hash(a))

#For string, a hash is generated, so it can be the key for a dictionary.
#All immutable data types are hashable in nature

# c="Gaming"
# print(hash(c))

#float is a hashable data type

# f1={10.2:"test-float","Name":"Hajj","Branch":"IT", "Roll_No":30}
# print((f1))



#Tuple can be key for a dictionary

# d1={10.2:"Dave","Name":"Hajj","Branch":"IT", "Roll_No":30, (a,b):"abc"}
# print((d1))


#Set is mutable so it can't be used as dictionary keys
# s={10,20,30}
# print(hash(s))

#d1={10.2:"Dave","Name":"Hajj","Branch":"IT", "Roll_No":30,{10,20,30}:"xyz"}

#Dictionary is mutable so it can't be a key for a dictionary.

#d1={10.2:"Dave","Name":"Hajj","Branch":"IT", "Roll_No":30,{"a":"b"}:"xyz"}

#Note: Key will always be hashable type. All immutable data types are hashable. 
# Only immutable data types (integer, float, string, boolean and tuple Key) can be key of a dictionary.

# d1={"Names":["Dave","Hajj","Gaurav"],"Branch":{"IT", "CS", "Mech"}, "Roll_No":30,(1,2):"abc"}
# print(d1)

#Some functions to use with dictionary

# d1={"Names":["Dave","Hajj","Gaurav"],"Branch":{"IT", "CS", "Mech"}, "Roll_No":30,(1,2):"abc"}

#1. items() function  --> is used with dictionaries to return a view object that 
# # contains all the key-value pairs in the dictionary as tuples.
# print(d1.items())


#2. values() function-->  is used with dictionaries to retrieve all the values stored within the dictionary

# d1={"Names":["Dave","Hajj","Gaurav"],"Branch":{"IT", "CS", "Mech"}, "Roll_No":30,(1,2):"abc"}
# print(d1.values())


#3. keys() function --> is used to retrieve all the keys present in a dictionary.

# d1={"Names":["Dave","Hajj","Gaurav"],"Branch":{"IT", "CS", "Mech"}, "Roll_No":30,(1,2):"abc"}
# print(d1.keys())

#4.fromkeys() function --> is used to create a new dictionary with specified keys and an optional default
# value for all keys.

# k=("name", "roll_no")
# v=("gaurav")

# d=dict.fromkeys(k,v)
# print(d)

#5. get() function - prints the associated value (s) for a specific key.
#It's a safer alternative to using square brackets ([]) to access dictionary elements because it allows 
#you to specify a default value to be returned if the key doesn't exist, preventing KeyError exceptions.
# d1={"Names":["Dave","Hajj","Gaurav"],"Branch":{"IT", "CS", "Mech"}, "Roll_No":30,(1,2):"abc"}
# print(d1.get("Names"))


# Operators In Python
# 1.Arithmetic Operators  (Addition, Subtraction, multiplication, division)
# 2.Logical Operators
# 3.Membership Operators
# 4.Bitwise Operators   100 & 010 
# 5.Identity Operators


# a=20
# b=10

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)  #Floor Division (//): Divides the first operand by the second, producing an integer result (rounded down).

# 2. Logical Operators

# # Example: Logical Operators (AND, OR, NOT) with generic variables
# a, b, c = True, False, True

# # AND: Both conditions must be True
# if a and c:
#     print("Both a and c are True (AND condition).")

# # OR: At least one condition must be True
# if b or c:
#     print("Either b or c is True (OR condition).")

# # NOT: Reverses the condition
# if not b:
#     print("b is False (NOT condition).")
# --------------------------------------------------------------------
# Both a and c are True (AND condition).
# Either b or c is True (OR condition).
# b is False (NOT condition).

#3.Membership Operators

# l=[10,20,30,"India",True,"USA"]

# print("India" in l)


#5.Identity Operators

# a=10
# b=20

# print(a is b)

# x = [1, 2, 3]
# y = x
# z = [1, 2, 3]

# print(x is y) 
# print(x is z) 
# print(x is not z) 

# 6. Comparison operators -->used to compare values and return a boolean result (True or False). 

# •	Equal to (==): Checks if two values are equal.
#                 x = 5
#                 y = 5
#                 print(x == y)  # Output: True
# •	Not equal to (!=): Checks if two values are not equal.
#                  x = 5
#                  y = 10
#                 print(x != y)  # Output: True
# •	Greater than (>): Checks if the left operand is greater than the right operand. 
#                x = 10
#                y = 5
#                print(x > y)  # Output: True
# •	Less than (<): Checks if the left operand is less than the right operand. 
#                 x = 5
#                 y = 10
#                print(x < y)  # Output: True
# •	Greater than or equal to (>=): Checks if the left operand is greater than or equal to the right operand. 
#                x = 10
#                y = 10
#                print(x >= y)  # Output: True
# •	Less than or equal to (<=): Checks if the left operand is less than or equal to the right operand.
#                x = 5
#                y = 10
#                print(x <= y)  # Output: True


#C. Indexing:  Accessing a single element.

# my_list = [10, 20, 30, 40, 50]
# print(my_list[0])
# print(my_list[2])
# print(my_list[-1]) #-1 will retrieve the value from the last index

#Slicing:  Extracting a portion of a sequence.

# my_string = "Hello, World!"
# print(my_string[0:5])  
# print(my_string[7:])
# print(my_string[:5])
# print(my_string[::2])




# print(l[1:6])  #l[beginning_index_#:end_index_#:increment by 1 by default]
# print(l[1:])  #from beginning index to the last index

#From 3rd index to including Happy(-->have to add 5th index to include 4th index)
#Increments by 1 by default
#print(l[2:5])

#Get 7th index value
#print(l[8])

l=[10,20,30,"India","Happy","USA",True]
#Get 3rd index to 7th index value even though 7th index doesn't exist
#print(l[2:8])

#Print Increment values by 2  Output -->[30,"Happy",True]
# print(l[2:7:2])

#Print Increment values by 3 7-->Output -->[20,"Happy"]
# print(l[1:7:3])   

#Negative Slicing
# print(l[-1:-7:1])

# ex 2

#l1=[10,20,30,40,50,60,70]

#print(l1[5:1:-1])

#print(l1[7:2:-1])
#--------------------------------------------------------------------------------------------------
#Day 29 Conditions  --> If you want a particular condition to be performed when a 
#a particular condition is matching

#1. If else -->Even number, odd or prime number (divisible by 1 or itself)
# a=33

# if a%2 == 0:
#     print("Provided number is an even number")

# elif a%2 != 0:
#     print("Provided number is an odd number")

# else:
#     print("Provided number is a prime number")

#Ex 2 Honeymoon Destinations

# honeymoon_destinations=input("Enter your honeymoon destination: ")

# if honeymoon_destinations == "Mombasa":
#     print("It is very common in Nairobi middle class to go on honeymoon")
# elif honeymoon_destinations == "Malvdives":
#     print("It's overrated due to high marketing")
# elif honeymoon_destinations == "Zanzabar":
#     print("It's the best place for a honeymoon....truly breath taking!")
# else:
#     print("These are good but not as famous.")


#B. Loops in Python are used to repeat actions efficiently. The main types are 
# For loops (counting through items) and While loops (based on conditions). 
# Additionally, Nested Loops allow looping within loops for more complex tasks. 
# While all the ways provide similar basic functionality, they differ in their
#  syntax and condition-checking time

# loops: executing for each element from a collection of elements/sequential data. 
# lops: collection list, set, range, dict. You can't iterate over a single element.


# #1. for loop
# l1=[10,20,30,50,40]
# # #list, dict,set, tuple, range

# # a=10 #Trying to Iterate over a single element which is not possilble

# for each_element in l1:
#     print(each_element)

#ex 2

#l1=[10,20,30,40]

# s1={20,"name",True} # In set order is not important

# for x in s1:  #x will store the value of iteration from s1
#     print(x)


#ex 3 dictionary iteration

# d1={"Name":"Hajj","Work":"Trainer"}

# for x in d1.items():
#     print(x)



#ex 4 range

# for x in range(6):
#     print(x)

# print(range(6))

#While loop

# i=0
# while i<=10:
#     print(i)
#     i=i+1

# [10,20,30,40]

#Day 30 Functions In Python


#Define a function

# def add(x,y):
#     print(x+y)

# #Call the function
# add(10,20)
# add(20,30)


#example 2 Arithmetic Operations
# def arth(x,y):
#     if ops=="add":
#         print(x+y)
#     elif ops=="sub":
#         print(x-y)
#     elif ops=="mul":
#         print(x*y)
#     else:
#         print(x//y)

# ops="sub"
# arth(20,10)

#eval() function in allows you to dynamically evaluate a string 
# as a Python expression and return the result.   

# a=eval(input("enter first number: "))  #eval() --> returns integer
# b=eval(input("Enter second number: " ))

#ex 3 Positional argument

# def add(x,y):  #Positional argument --. Order is important
#     print(x+y)

# x=10
# y=20
# add(x,y)


#ex 4 Key word based argument --> Order is not important

# def add(x,y):
#     print(x+y)

# add(y=3,x=10)

#ex 5 Need to Add 3 numbers or 4 numbers

# def add(*args):
#    sum=0
#    for x in args:
#        sum=sum+x

#    print(sum)

#Method Overloading --> #You can call the same function but with different data types as arguments
#N/A in Python b/c it's not static type language
#in Python you can achieve method overloading with (*args)


# add(10,20)
# add(10,20,30)
# add(10,20,30,40,50,40)

# Interview ?: How can you achieve method overloading in Python ?
# Answer: By default, it is n/a in Python b/c it's not a statically typed language like Java. 
# In Python, you can achieve the method overloading functionality by using variable length of (*args).


#Ex 6. Key Ward based argument

# def add(**kwargs):
#     sum=0
#     for x in kwargs.values():
#         sum=sum+x
#     print(sum)


# add(a=10,b=20)
# add(a=10,b=20,c=30)
# add(a=10,b=20,c=30,d=40,e=50,f=40)

#Day 31 Exception Handling
#A. handles errors that occur during the execution of a program. Exception handling allows 
# to respond to the error, instead of crashing the running program. It enables you to catch 
# and manage errors, making your code more robust and user-friendly.

# a=10
# b=2
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("Please provide non-zero number as denominator")
# except TypeError as err:
#     print(f"Only integer value is allowed: {err}")
# except Exception as err:
#     print(f"Error is: {err}")
# finally:
#     print("program execution stopped")


#B Packages  --> collection of modules
#1. A module is pre-written code that you can directly use in your code 

#import os  #os comes by default.To install some packages use pip (python install packages) manager.

#If you want to run some system level functions you can import 

#print(os.system("ls -ltr"))

#How to run shell command in python?

#NumPy - use for arithmetic operations

#C. OOPS --> Object Oriented Programming. Python is a scripting, procedural, and object oriented language.
#1. #Instance of a class is an object. The blueprint is the class. You can create any # of objects.
#self is a reference to the object

class Employees:
    def __init__(self, EmpID, branch, Designation):
        #print(id(self))
        self.emp_id=EmpID
        self.branch=branch
        self.designation=Designation
    def display_info(self):
        print(f"{self.emp_id}..{self.branch}")

Hajj=Employees(1,"IT","Solutions Architect")

Kiran=Employees(2, "Admin","Controller")

Hajj.display_info()  
#Kiran.display_info()