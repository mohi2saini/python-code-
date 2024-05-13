# #function to calculate sum of two numbers
# def calc_sum(a,b):    # Defining function  a,b are the parameters
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(2,3)          #calling function   2,3 are the arguments
# calc_sum(78,45)

# #Function to create average of 3 numbers
# def calc_avg(a,b,c):
#     sum=a+b+c
#     avg=sum/3
#     print(avg)
#     return avg
# calc_avg(2,4,6)

# # example of default  parameter
# def calc_prod(a=2,b=3):# a and b are default parameters
#     print(a*b)
#     return a*b
# calc_prod()


# def calc_prod(a,b=3): #  b is a default parameter 
#     print(a*b)          #when we make one parameter default it is must to be last one
#     return a*b
# calc_prod(5)

# #Write a function to print the length of a list(List is a parameter)
# cities=["delhi","jaipur","chennai","mumbai","jodhpur"]
# heroes=["Bhagat Singh","Sukhdev","Rajguru","Chandrashekhar Azad"]
# def print_length(list):
#     print(len(list))

# print_length(cities)
# print_length(heroes)

# #Write a function to print the elements of a list in a single line(list is the patrameter)
# cities=["delhi","jaipur","chennai","mumbai","jodhpur"]
# heroes=["BhagatSingh","Sukhdev","Rajguru","ChandrashekharAzad"]

# def print_element(list):
#     for item in list:
#         print(item , end=" ")

# print_element(cities)
# print_element(heroes) 

# #Write ba bfunction to find the factorial of n (n ois in the parameter)

# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i
        
#         print(fact)

# calc_fact(5)
# calc_fact(7)

# #WAF to convert USD into INR
# def convert(USD):
#     INR=83*USD
#     print(USD ,"USD =",INR,"INR")
# convert(5)
# convert(81)

# #WAF that take a number as a input and return odd if input number is odd and return even if input number is 
# def number(n):
#     if(n%2==0):
#         print("even")
#     else:
#         print("odd")
#     return n
# number(9)
# number(4)
# number(0)

# #        RECURSION
# # when a function call itself repeatedly

# def show(n):    #function defination
#     if(n==0):  #Base condition-function kab tak call hoga (most imp)
#         return
#     print(n)  
#     show(n-1)    #recursive call
# show(5)         #function call

# # Calculate factorial using recurssion   
# def fact(n):
#     if(n==1 or fact==0):
#         return 1
#     else:
#         return fact(n-1) * n
    
# print(fact(5))
# print(fact(10))

# # Write  a recursive function to calculate the sum of first n natural numbers

# def sum(n):
#     if(n==0):
#         return 0
#     return n+sum(n-1)
# print(sum(5))

# # Write a recursive function to print all elements in a list.
# # Hint: use list and index as parameters.


# def print_list(list,idx=0):
#     if(idx==len(list)):
#         return 
#     print(list[idx])
#     print_list(list,idx+1)
# fruits=["apple","mango","banana","pineapple"]
# print_list(fruits)

    
def  check(a,b=4):
    x=a*b
    print(x)
check(3)     # here we observe that as we already provide the value of b in function defination hence we not need to give value of b at the time of calling
check(2,5)   # here we observe that when we define  that  function we already fix the value of b but later on calling we are able to change the value of b OUTPUT =10
check(5,10)