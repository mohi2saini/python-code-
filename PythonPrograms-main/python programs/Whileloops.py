#  WHILE LooP

# #print a string
# count=1
# while count<5:   #stopping condition
#     print("hello")
#     count=count+1
# print(count)

# #print numbers from 1 to 100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1

# #print numbers from 100 to 1
# i=100
# while(i>=1):
#     print(i)
#     i=i-1

# #prinmt the multioplication table of a number n
# num=int(input("enter a number to print multiplication table "))
# i=1
# while(i<=10):
#     mul=num*i
#     print(num,"*" ,i,"=" ,mul)
#     i=i+1

# # Print the elements of following list using a loop
#     # [1,4,9,16,25,36,49,64,81,100]

# nums=[1,4,9,16,25,36,49,64,81,100]
# index=0
# while(index<len(nums)):
#     print(nums[index])
#     index=index+1
#  Search a number x in this tuple using loop:
   # (1,4,9,16,25,36,49,64,81,100)
#this loop will run till full tuple length

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("item found at index",i)
        
#     else:
#         print("finding.......")
#     i=i+1


    #  BREAK 

# i=1
# while(i<=5):
#  print(i)
#  if(i==3):
#     break
#  i=i+1

#  #  Search a number x in this tuple using loop:
#    # (1,4,9,16,25,36,49,64,81,100)
# #this loop will run till first time x found

# nums=(1,4,9,16,25,36,49,64,81,100)
# x=36
# i=0
# while i<len(nums):
#     if(nums[i]==x):
#         print("item found at index",i)
#         break
        
#     else:
#         print("finding.......")
#     i=i+1

# CONTINUE

# i=1
# while(i<=5):
#   if(i==3):
#         i=i+1
#         continue  # used to skip any iteration
#   print(i)

#   i=i+1

  # WAP to print odd nu8mbers between 1 to 10
i=1
while(i<=10):
    if(i%2==0):
        i=i+1
        continue
    print(i)
    i=i+1