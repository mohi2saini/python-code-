str="python is very very easy"


#find length of string using len() function
print("length of string is:",len(str))

#use str.count(substring) function to count occurence of substring
print(str.count("y"))
print(str.count("very"))

#program to show use of string index()function
print(str.index("is"))
print(str.index("n"))
# print(str.index("z"))  #return error

#program to show use of string uppercase() function
print(str.upper())

#program to show use of string lowercase() function
print(str.lower())

#using capitalize() make first letter of string in upper case
print(str.capitalize())

#program to check wheather function start with given substring or  not (it will return true or false)
print(str.startswith("object"))
print(str.startswith("python"))
print(str.startswith("Python"))  # output is false,this shows that python is case sensitive


#program to check wheather function ends with given substring or  not (it will return true or false)
print(str.endswith("easy"))
print(str.endswith("very"))

#using string split function to  break down string into smaller parts, it will return output in form of list
print(str.split())

#using string join() funstion ,oit will join two string 
#it will join such that second string between each letter of first string
temp1="!"
temp2="-"

print(temp1.join(str))
print(temp2.join(str))

#using string find() function to find the index position of first occurence of specified substring
#diffference between index() and find() is that when substring not found 
#index() function will return exception whereas find() function return -1

print(str.find("is"))
print(str.find("n"))
print(str.find("z")) #return -1 as z is not present in given string
print(str.find("is,30")) #return -1 as size of given string is less than 30

#using strip function it will remove extra space  if present from both side of given string 
print(str.strip())

#using lstrip function it will remove extra space  if present from left side of given string 
print(str.lstrip())

#using rstrip function it will remove extra space  if present from right side of given string 
print(str.rstrip())

# using string replace function to replace all occurences of old with new
print(str.replace("easy","hard"))
