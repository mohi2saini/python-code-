# # program to calculate electricity bill

# def Calculate_bill(units):
#     if units <=50:
#         bill = units*0.5
#     elif units <=100:
#         bill = 50*0.5 + (units-50)*0.75
#     elif units <=150:
#         bill = 50*0.5 + 50 *0.75 + (units-100)* 1.0
#     elif units <=250:
#         bill = 50*0.5 + 50 *0.75 + 50*1.0 + (units-150)* 1.5
#     else :
#         bill = 50*0.5 + 50 *0.75 + 50*1.0 +100*1.5 + (units-250)* 1.5

#     return bill

# bill_units=int(input("enter your bill units :"))
# total_bill = Calculate_bill(bill_units)
# print("your total electricity bill is :  ",total_bill,"Rs" )

# # program to retail shop billing

# n=int(input("Enter number of items :"))
# total_bill=0
# for el in range(0,n,1):
#     item=input(F"enter {el+1} item name :")
#     price=int(input(f"enter price of {item}: " ))
#     total_bill=total_bill+price

# print("total bill is:" , total_bill ,"Rs")

# #Weight of a motorbike

# def calculate_bike_weight(frame_weight, engine_weight, wheels_weight, fuel_tank_weight, other_components_weight):
#     total_weight = frame_weight + engine_weight + wheels_weight + fuel_tank_weight + other_components_weight
#     return total_weight

# frame_weight = float(input("Enter the weight of the frame (in kg): "))
# engine_weight = float(input("Enter the weight of the engine (in kg): "))
# wheels_weight = float(input("Enter the weight of the wheels (in kg): "))
# fuel_tank_weight = float(input("Enter the weight of the fuel tank (in kg): "))
# other_components_weight = float(input("Enter the weight of other components (in kg): "))
# bike_weight = calculate_bike_weight(frame_weight, engine_weight, wheels_weight, fuel_tank_weight, other_components_weight)
# print("The total weight of the motorbike is:", bike_weight, "kg")

# #weight of a steel bar 
# def calculate_steel_bar_weight(length, width, height, density):
#     volume = length * width * height
#     weight = volume * density
#     return weight

# length = float(input("Enter the length of the steel bar (in meters): "))
# width = float(input("Enter the width of the steel bar (in meters): "))
# height = float(input("Enter the height of the steel bar (in meters): "))
# density = float(input("Enter the density of the steel (in kg/m^3): "))
# steel_weight = calculate_steel_bar_weight(length, width, height, density)
# print("The weight of the steel bar is:", steel_weight, "kg")


# #wAP By using for loop to calculate the average of first n natural numbers 
# num=int(input("enter value of num : "))
# sum=0
# for n in range (1,num+1):
#     sum=sum+n
# average= sum /num
# print("average of first n natural numbers is : ", average)

# #WAP to calculate factorial of a  number using for loop 
# num=int(input("enter value of n : "))
# fact=1
# for n in range (1,num+1):
#     fact=fact*n
# print("factorial of entered number is: ",fact )

# WAP to check wheather a given number is armstrong or not 

# num=int(input("enter a number : "))
# n=num
# m=num
# s=0
# count=0
# while(m>0):
#     m=m//10
#     count=count+1

# while(n>0):
#     r= n%10
#     s=s+(r**count)
#     n=n//10  #here we have to use intezer division ( //, floor value division) instead of floating division,/
# if(s==num):
#     print("get armstrong")
# else:
#     print("number is not armstrong")

# num=int(input("enter a number : "))
# no_of_digits=len(str(num)) 
# sum=0
# temp=num
# while temp>0:
#     digit=num%10
#     sum+=digit** no_of_digits
#     temp//=10
# if(sum==num):
#     print("get armstrong")
# else:
#     print("number is not armstrong")
 





#WAP to print sin series 
# import math
# print(sin(90))

import math
print(math.sin(math.radians(90))+math.sin(math.radians(30)))


# #Wap to demonstrate reverse and pallindrome
# num=input("enter a number :")
# num_rev=(num[::-1])
# print("reverse number is :", num_rev)

# #wap to demonstrate pallindrome 
# num=input("enter a number :")
# num_rev=(num[::-1])
# if(num==num_rev):
#     print("number is pallindrome")
# else:
#    print("number is not  pallindrome")
# import numpy as np

# # Creating a 1D array of integers using numpy
# int_array = np.array([1, 2, 3, 4, 5])
# print(int_array)  # Output: [1 2 3 4 5]

# # Accessing elements by index
# print(int_array[0])  # Output: 1



