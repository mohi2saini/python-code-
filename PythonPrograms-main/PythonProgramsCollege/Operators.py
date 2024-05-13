#Arithmetic Operator
a=20
b=10
c=-11
print("sum :",a+b)
print("difference :",a-b)
print("multiplication:",a*b)
print("division :",a/b)
print("remainder:",a%b)
print("power :",a**b)
print("floor division a//b :",a//b)
print("floor division a//c :",a//c)
print("floor division c//b :",c//b)




#Assignment Operator
str1="hello"
str2="python"

print(str1)
str1+=str2
print(str1)


a=20
b=10

a+=b
print(a)
a-=b
print(a)
a*=b
print(a)
a/=b
print(a)
a//=b
print(a)
a**=b
print(a)
a%=b
print(a)

#Relational Operator
a=2
b=5

print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
print(a==b)
print(a!=b)

#Identity Operators(is and is not)
# identity operator not check for the same content but it check wheather they are actually the same object 
# means if they are present on same memory location return true else return false

a=2
b=5
print(a is b)
print(a is not b)

a=2
b=2
print(a is b)
print(a is not b)

a='a'
b='b'
print(a is b)
print(a is not b)

a='a'
b='a'
print(a is b)
print(a is not b)

a=("krishna","Agarwal")
b=("krishna","Agarwal")
print(a is b)
print(a is not b)

a=["krishna","Agarwal"]
b=["krishna","Agarwal"]
print(a is b)
print(a is not b)

x=[1,2,3]
y=[1,2,3]
z=x
print(x is y)
print(x is z)
print(x is not y)

#Membership operator(in and not in)
# return true if variable is found in specified sequence,basically used for list string and tuple 

a=[1,2,3,4,5]
b=3
c=2,3,4
d=3,2,1
e=[2,3,4]
print(b in a)
print(c in a)
print(d in a)
print(e in a)
print( c not in e)

str1="python is easy"
str2="is"
str3="is easy"
str4="hard"
print(str2 in str1)
print(str3 in str1)
print(str4  in str1)
print(str4 not in str1)

# bitwise Operator

a=6
b=3

# And operator &
c=a&b
print(c,bin(c))


# OR operator |
c=a|b
print(c,bin(c))

# Not operator ~
c= ~b
print(c,bin(c))

# xor operator ^
c=a^b
print(c,bin(c))

# left shift operator <<
c=a<<2
print(c,bin(c))

d=b<<2
print(d,bin(d))

# right shift operator >>
c=a>>2
print(c,bin(c))
d=b>>2
print( d,bin(d))


#Logical operator

a=4
b=6

#Logical And
c=a>10 and b>10
d=a>5 and b>5
e=a<5 and b<5
f=a<10 and b<10
print(c)
print(d)
print(e)
print(f)

#Logical OR
c=a>10 or b>10
d=a>5 or b>5
e=a<5 or b<5
f=a<10 or b<10
print(c)
print(d)
print(e)
print(f)

#Logical Not
c= not(a>10 and b>10)
d= not(a>5 and b>5)
e= not(a<5 and b<5)
f= not(a<10 and b<10)
print(c)
print(d)
print(e)
print(f)


#Arithmetic Operatorion on  floating point number
a=20.0
b=10.0

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)





