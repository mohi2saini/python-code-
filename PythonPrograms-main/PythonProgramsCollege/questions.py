# # WAP to read and print values of variable of different datatype
# a=int(input("Enter a number "))
# b=str(input("Enter your name"))
# print(a)
# print(b)

# #wap to swap two variable
# a=10
# b=20
# print("a before swapping",a)
# print("b before swapping",b)
# a,b=b,a
# print("a after swapping",a)
# print("b after swapping",b)

# #WAp to swap two variable using third variable
# a=10
# b=20
# print("a before swapping",a)
# print("b before swapping",b)
# c=a
# a=b
# b=c
# print("a after swapping",a)
# print("b after swapping",b)

# # WAp to calculate area of triangle using heron's formula
# import math
# a=int(input("enter first side of triangle : "))
# b=int(input("enter second side of triangle : "))
# c=int(input("enter third side of triangle : "))
# s=(a+b+c)/2 
# area= math.sqrt(s*(s-a)*(s-b)*(s-c))
# print("area of triangle is : ", area)

# #WAp to calculate the distance between two points
# import math
# x1=int(input("enter coordinate x1 :"))
# y1=int(input("enter coordinate y1 :"))
# x2=int(input("enter coordinate x2 :"))
# y2=int(input("enter coordinate y2 :"))
# distance=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
# print("distance between two points is : ",distance)

# #WAp to find Ascii value of character
# a=input("enter a character : ")
# ascii=ord(a)  #  ord() is function used to find ascii value it is function that takes character valuer only(1,2,3,w,e,d,f,g,@,#,$) it does not accept values like (23,krishna)
# print(ascii)

# #WAP to enter a number and display its binary ,hexa and octal equivalent 
# a=int(input(" enter a number : "))
# b=bin(a)

# c=oct(a)

# d=hex(a)
# print("binary of entered number is :", b)
# print("octal of entered number is : ",c)
# print("hexadecimal of entered number is :", d)

# #WAP by using for loop to calculate the average of first n natural numbner 
# n=int(input("enter value of n: "))
# sum=0
# avg=0.0
# for i in range(1,n+1):
#     sum=sum+i
# avg=sum/i
# print("sum of  n nautral no",sum) 
# print("average of first n natural number is:",avg)

# # #write a program to sum the series 1+1/2+.......+1/n

# n=int(input("enter value of n: "))
# sum=0
# for i in range(1,n+1):
#     sum=sum+(1/i)
# print("sum of series  is:",sum)

# #write a program to calculate pow(x,n)
# x=int(input("enter value of x: "))
# n=int(input("enter value of n: "))
# pow=x**n
# print(x,"raise to the power ",n,"= ",pow)




"""
#WAp to print pattern
# 1
# 1 2
# 1 2 3
# 1 2 3 4 
# 1 2 3 4 5

for i in range(1,6):
    count=1
    for j in range(0,i):
        
         print(count,end=" ")
         count+=1
    print()
"""


'''

# WAp to print pattern
# 1
# 3 2
# 6 5 4
# 10 9 8 7

start=1  #start value
stop=2
current_num=stop
for row in range(2,6):
    for col in range(start,stop):
        current_num-=1
        print(current_num,end=" ")
    print(" ")
    start=stop
    stop+=row
    current_num=stop
'''

# *****
# *****
# *****
# *****
# *****

for i in range (0,5):
    for j in range(0,5):
        print("*", end=" ")
    print(" ")


