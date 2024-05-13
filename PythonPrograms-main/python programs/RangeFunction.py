# # There are three ways to use range function
# for el in range(5):   #First to give stop condition only
#    print(el)           # range(stop)   output 0,1,2,3,4

# for el in range(1,5):  #  Second to give start and end condition
#    print(el)           #   range(start, stop)    output 1,2,3,4

# for el in range(1,5,2):  # Third way is to give start,end as well as step condition
#    print(el)             #   range(start, stop, step)        output 1  3

#  # Wap to print even numbers between 1 and 10 using range function

# for el in range(0,11,2):
#    print(el)

#  # Wap to print odd numbers between 1 and 10 using range function

# for el in range(1,10,2):
#    print(el)

# #  PRACTOICE QUESTIONS

# # print numbers from 1 to 100
# for el in range(1,101):
#    print(el)

# # print numbers from 100 to 1
# for el in range(100,0,-1):  #note : step size can also be bnegative
#    print(el)

#Print the multiplication table of number n
n=int(input("enter a  number :"))  #WAY 1
for el in range(n,11*n,n):
   print(el)

n=int(input("enter a  number :"))   #WAY 2
for el in range(1,11):
   print(n*el)