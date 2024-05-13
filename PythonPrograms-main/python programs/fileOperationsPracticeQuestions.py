# """
# create a new file "practice.txt" using python.add the following data in it:
# Hi everyone
# we are learning file I/O
# using Java
# I like programming in Java.

# """
# f=open("practice.txt","w")
# f.write("Hi everyone \nwe are learning file I/O \nusing Java \nI like programming in Java.")
# f.close()

# #WAF that replace all occurrences of "Java" with "python" in above file
# def replace_occurrence():  
#   f=open("practice.txt","r")
#   data=f.read()
#   new_data= data.replace("Java","Python")
#   print(new_data)
#   f.close() 
  
#   f=open("practice.txt","w")
#   f.write(new_data)
#   f.close()
# replace_occurrence()

# #Search if the word  "learning" exists in the file or not
# f=open("practice.txt","r")
# data=f.read()

# if(data.find("learning")!=-1):
#     print("found")
# else:
#     print  ("not found")


# f.close()

# #WAF to find which line of the file does the word "learning" occur first.
# #Print -1 if word not found

# def check_for_line():
#    word="learning"
#    data=True
#    line_no=1
#    with open("practice.txt","r") as f:
#       while data:
#          data=f.readline()
#          if(word in data):
#             print(line_no)
#             return
#          line_no+=1
      
#       return -1
   

# check_for_line()

#from a file containing numbers seprated by comma, print the count of even numbers.
count=0
with open("practice.txt","r") as f:
    data=f.read()
    
    nums=data.split(",")
    for val in nums:
        if(int(val) %2 ==0):
            count+=1
print(count)
  

