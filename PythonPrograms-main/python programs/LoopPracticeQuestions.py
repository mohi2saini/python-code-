#WAP to find the sum of first n natural numbers (using while)

n=int(input("enter n "))
sum=0
i=1
while(i<=n):
  sum=sum+i
  i=i+1
print("the sum of first",n,"natural numbers is :",sum)


#WAP to find the sum of first n natural numbers (using for loop)

n=int(input("enter n"))
sum=0
for i in range(1,n+1):  #yeah line bata rahi hai ki loop kha se  kha tak chalega
   sum=sum+i
print("total sum =",sum)

# WAP to find the factorial of first n numbers (using for loop)
n=int(input("enter a number to find factorial"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print("factorial of number is :",fact)

#WAP to find the factorial of first n numbers (using while loop)
n=int(input("enter a number to find factorial"))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i=i+1
print("factorial of number is :",fact)
