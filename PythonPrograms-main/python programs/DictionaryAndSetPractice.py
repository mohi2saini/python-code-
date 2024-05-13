"""
Store following word meanings in a python dictionary :
table : “a piece of furniture”,“list of facts & figures”
cat : “a small animal”

"""
dictionary= {
    "table" : ["a piece of furniture","list of fact and figures"],
    "cat": "a small animal"       
}
print(dictionary)

#  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”

#here we use concept of sets as there is no concept of duplicacy in sets then find length of set
classroom={ "python","java","c++","python","javascript","java","python","java","c++","c"}
print("classroom needed by students",len(classroom))


#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
marks={}
phy=int(input("enter phy marks "))
marks.update({"phy":phy})
chem=int(input("enter chem marks "))
marks.update({"chem":chem})
maths=int(input("enter maths marks "))
marks.update({"maths":maths})
print(marks)


#Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
values={9,9.0} #when we print value it only give one element that is 9 in output as hash value of both 9 and 9.0 is same 
print(values)

values={9,"9.0"}  # so to store them seprately we may use concept of string data type
print(values)

values={
    ("float",9.0) ,    # another way is to use tuples
    ("int",9)
}
print(values)