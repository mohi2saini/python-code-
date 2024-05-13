"""
#Reading a File

f=open("demo.txt","r")
# data=f.read()  # used to read entire file
#data=f.read(10) #used to read first 10 characters of file
line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
print(type(line1))
f.close()
"""



#Writing a File using  write 'w' mode
f=open("demo.txt","w")
f.write("i want to learn all programming languages")
f.close()

#writing file in append "a" mode
f=open("demo.txt","a")
f.write("\n this will help me to get best placements")
f.close()

#open file in "r+" (read and write) mode ,hum jitne character denge purani file me se utne character overwrite ho jayenge from start.
f=open("demo.txt","r+")
f.write("abc")
print(f.read( ))
f.close() 

#open file in "w+"(read and write )mode ,isme phle file truncate hogi fir write hoga
f=open("demo.txt","w+")
print(f.read)  #isse kuch nhi print hoga kyoki file truncate hogayi
f.write("abc")
f.close()

#open file in "a+"(read and append )mode ,isse file read hogi aur hum jo bhi write karenge woh at the end add hoga
f=open("demo.txt","a+")
print(f.read) 
f.write("krishna")
f.close()

#using with keyword
with open("demo.txt","r") as f:
  data=f.read()
print(data)

#Deleting a file
import os
os.remove("demo.txt") 

