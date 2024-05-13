#Using for loop to traverse a list
nums=[1,2,3,4,5]
for val in nums:
    print(val)

# Using for loop to traverse a TUPLE
veggies=("potato","onion","tomato","ladyfinger","cucumber")
for val in veggies:
    print(val)

#traverse string using for loop
str="krishna"
for char in str:
    print(char)

# example to show use of else with for loop
#else statement always execute once loop get completely executed

str="krishna"
for char in str:
    print(char)
else:
    print("end")


# use else with break
str="krishna"
for char in str:
    if(char=="s"):
        print("s found")
        break
    print(char)
else:                  #else statement use karne se if break encounter ho raha hai toh else statement execute nhi hoga   
    print("end")

# cannot use else with break
str="krishna"
for char in str:
    if(char=="s"):
        print("s found")
        break
    print(char)

print("end")   #if we cannot use else then break eencounter hone par  bhi yeah statement execute hoga

#Print the elements of the following list using for loop
#[1,4,9,16,25,36,49,64,81,100]
list=[1,4,9,16,25,36,49,64,81,100]
for elements in list:
    print(elements)

# search for a  number x  in this tuple using for loop
  #(1,4,9,16,25,36,49,64,81,100) 

tuple=(1,4,9,16,25,36,49,64,81,100)
x=49
index=0
for elements in tuple:
    if(elements==x):
        print("x found at index",index)
    index=index+1

    