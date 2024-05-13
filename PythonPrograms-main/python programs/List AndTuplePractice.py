#WAP to ask the user to enter names of their 3 favourite movies and store them in a list

# IST WAY
movie1=input("enter first movie name ")
movie2=input("enter second movie name ")
movie3=input("enter third  movie name ")

list=[movie1,movie2,movie3]
print(list)

#2ND WAY
 
movies=[]      # first create an empty list
movie1=input("enter first movie name ")
movie2=input("enter second movie name ")
movie3=input("enter third  movie name ")

movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)

#WAp to checlk if a list contains a pallindrome of elements
# example [1,2,3,2,1]    [1,"abc","abc",1]

list=[1,2,1]
copylist=list.copy()
copylist.reverse()

if(copylist==list):
    print("list is pallindrome")
else:
    print("list is not pallindrome")

# 2ND WAY
first=input("enterr first element")
second=input("enter second element")
third=input("enter third element")
list=[first,second,third]
copylist=list.copy()
copylist.reverse()

if(copylist==list):
    print("list is pallindrome")
else:
    print("list is not pallindrome")


# WAP to count number students with "A" grsde in the following tuple
#   ["C","D","A","A","B","B","A"]

grade= ("C","D","A","A","B","B","A")
print(grade.count("A"))
    
 
#WAP to store the above values in a list and sort them from "A"to "D"
list=["C","D","A","A","B","B","A"]
list.sort()
print(list)