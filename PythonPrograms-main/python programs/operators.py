#arithmetic operators
a=5
b=2

sum=a+b
print(sum)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)

#relational/comparision operator

# note: in python redifination of variable is poddible
#         the most recent variable definatiopn get executed
a=20
b=10
print(a==b)  #false
print(a!=b)  #true    
print(a>b)    #true
print(a<b)   #false
print(a<=b)  #false
print(a>=b)  #true

#assignment operator
num1=10
num1+=10 # num=num+10 
print("num1:",num1)         #num1: 20

num2=10
num2/=10 # num=num/10
print("num2:",num2)         #num2: 1.0

num3=10
num3-=10 # num=num-10
print("num3:",num3)        # num3: 0
         

num4=10
num4*=10 # num=num*10
print("num4:",num4)         #num4: 100

num5=10
num5**=10 #num=num**10
print("num5:",num5)         #num5: 10000000000

num6=10
num6%=10 #num=num%10
print("num6:",num6)         #num6: 0

#Logical operator
#   NOT OPERATOR
print(not False)    #return true
print(not True)     #return false

x=40
y=50
print(not x>y)    #return  true 
print(not x<y)      # return false
 
#   AND OPERATOR
val1=True 
val2=True
val3=False
print("and operator",val1 and val2)   #return true as both condition are true
print("and operator",val1 and val3)   #return false as val3 is false
print("and operator",(x>y) and (y>x))   #false
print("and operator",(x<y) and (y>x))   #True

#  OR OPERATOR
print("or operator",val1 or val2)     #True
print("or operator",val1 or val2)      #True
print("or operator",(x>y) or (y>x))   #True
print("or operator",(x<y) or (y>x))     #True
print("or operator",(x>y) or (y<x))     #false




