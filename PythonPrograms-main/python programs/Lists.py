marks=[94.4,98.3,66.5,66.5,92.5]
print(marks) # print list
print(type(marks))  # print type of list
print(marks[2])    #accessing any element of list using index
print(marks[1])
print(len(marks))   #print length of list
student=["karan",34,"delhi"]  #shows we can store multitype data in single list
print(student)
student[0]="arjun"   #show that we can change any value in list using index as list are mutable in nature 
print(student)

#list slicing
print(marks[ :4])  #  marks[0:4]
print(marks[1:4])
print(marks[1:])    #  marks[1:len(marks)]
print(marks[-3:-1])

# LIST METHODS  [list methods return none it make changes in original list ,to see changes we have to print original list]
# changes made is permanent
list=[2,1,3]
print(list.append(4))  #add one element at end
print(list)
print(list.sort())  # sort list in ascending order 
print(list)
print(list.sort(reverse=True))  #sort list in descending order
print(list)
print(list.reverse)  #reverse elements of list
print(list)
print(list.insert(2,6))  #list.insert(index,value)  insert value at given index
print(list)
list.remove(1)   # remove first occurence of element, here remove first time 1 occur
print(list)
list.pop(2)   # remove elemet at given index
print(list)

list=["banana","litchi","apple","guvava"]
list.sort()
print(list)
list.reverse()
print(list)