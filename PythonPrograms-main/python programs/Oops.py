# # # class Student:
# # #     name="Krishna Agarwal"

# # # s1=Student()
# # # print(s1.name) 

# # # class Student:
# # #     def __init__(self):
# # #         print(self)
# # #         print("adding new student in Database...")

# # # s1=Student()
# # # print(s1) 

# # #Default constructor

# # class Student:
    
# #     def __init__(self):
# #         print("this is default constructor")
# # s1=Student()


# #     #parameterized Constructor
# # class Student:
# #     def __init__(self,name,marks ):
# #         self.name=name
# #         self.marks=marks
# #         print("adding new student in Database...")
# # s1=Student("karan",97)
# # print(s1.name,s1.marks)
# # s2=Student("Rahul",88)
# # print(s2.name,s2.marks)

# # #   class and instance attribute

# # class Student:
# #     college_name="ABC College"   # here college_name is class attribute
# #     def __init__(self,name,marks ):
# #         self.name=name   #here name is object attribute
# #         self.marks=marks   #here marks is object attribute
# #         print("adding new student in Database...")
# # s1=Student("karan",97)
# # print(s1.name,s1.marks)   #accessing object aatribute with object name
# # s2=Student("Rahul",88)
# # print(s2.name,s2.marks)
# # print(Student.college_name)  #acessing class attribute with class name
    
# # #methods in python
# # class Student:
# #     def __init__(self,name,marks):     #defining constructor
# #         self.name=name
# #         self.marks=marks
    
# #     def hello(self):             #Defining method
# #         print("hello",self.name)

# #     def get_marks(self):
# #         return self.marks
    
# # s1=Student("karan",97)                #creating object
# # s1.hello()
# # print(s1.get_marks())

# # # Question
# # # Create student class that takes name & marks of 3 subjects as arguments in constructor.
# # #themn create a method to print the average

# # class Student:
# #     def __init__(self,name,marks):
# #         self.name=name
# #         self.marks=marks
# #     def get_avg(self):
# #         sum=0
# #         for val in  self.marks:
# #             sum +=val
# #         print("hi",self.name,"Your Avg Score is:",sum/3)

# # s1=Student("tony stark",[99,98,97])
# # s1.get_avg()

# # s1.name="ironman"  #we can also directly change name of our object
# # s1.get_avg()


# # # class Student:
# # #     def __init__(self,name,marks1,marks2,marks3):
# # #         self.name=name
# # #         self.marks1=marks1
# # #         self.marks2=marks2
# # #         self.marks3=marks3
    
# # #     def average(self):
# # #        self.avg=[(marks1+marks2+marks3)/3]


# #static method
# class Student:
#     @staticmethod
#     def college():
#         print("ABC college")


# #abstraction
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.bck=False
#         self.clutch=False
    
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started....")

# car1= Car()
# car1.start()

# #Create Account class with 2 attributes- balance & account number
# # create method for debit ,credit, printing the balance 

# class Account:
#     def __init__(self,balance,acc_no):
#         self.balance=balance
#         self.acc_no=acc_no
#     # debit method
#     def debit(self ,amount):
#         self.balance -= amount
#         print("Rs" , amount, "was debited")
#         print("total  balance = " ,self.get_balance())

#         # credit method
#     def credit(self ,amount):
#         self.balance += amount
#         print("Rs" , amount, "was credited")
#         print("total  balance = " ,self.get_balance())

#     def get_balance(self):
#         return self.balance 


# acc1=Account(10000,12345) 
# acc1.debit(500)
# acc1.credit(1500)

dict={
    "brand":"Bata",
    "footwear":"shoes",
    "year":2020,
    1:"a"

}
print(dict)

print(dict.get("brand","not found "))
print(dict.get(1,"not found "))
print(dict.get(2,"not found "))

print(dict.keys())
print(dict.items())
print(dict.values(krish))