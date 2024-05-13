# """
# print grade of students
# marks >= 90, grade =“A”
# 90 > marks >= 80, grade =“B”
# 80 > marks >= 70, grade =“C”
# 70 > marks, grade =“D 
#  ”"""

# #way1
marks=int(input("enter your marks"))
if(marks>=90):
    print(" A grade")
elif(marks>=80 and marks<90):
    print(" B grade")
elif(80 > marks >= 70):
    print(" c grade")
else:
    print("d grade")

# #way2
marks=74
if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of the student:",grade)
     
 #NESTING

age=91
if(age>=18):
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")

#WAP to check if a number entered by user is odd or even
num=int(input("enter a number"))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")

#WAP to find the greatest of three number entered by user
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
if(a>=b and a>=c):
    print(" a is greatest",a)
elif( b>=c):
    print("b is greatest",b)
else:
    print("c is greatest",c)

#WAP to check if a number is a multiple of 7 or not

x=int(input("enter a number"))
if(x % 7==0):
    print("number is a multiple of 7")
else:
    print("number is not a multiple of 7")

#WAP to find the greatest of three number entered by user
a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
d=int(input("enter fourth number"))
if(a>=b and a>=c and a>d):
    print(" a is greatest",a)
elif( b>=c and b>d):
    print("b is greatest",b)
elif( c>d):
    print("c is greatest",b)
else:
    print("d is greatest",c)