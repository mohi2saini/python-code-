# #   create DICTIONARY  and then print it
# # Note:we can use almost every data type as a value but cannot use mutable data type as key like list and dictionary
# #in key we generally use primitive data type and we may also muse tuple
# #most of the case we keep our key as String
# info={
#     "key":"value",
#     "name":"krishna",
#     "learning":"python",
#     "age":23,                                #use integer as a value
#     "is_adult":True,                         #use boolean as a value
#     "subjects":["python","java","android"],  #use list as a value
#     "topics":("dict","set"),                 #use tuple as a value
#     12.99:94.3,                              #use integer as a key

# } 
# print(info)
# print(type(info))
# print(info[12.99])          #accessing value using key name
# print(info["subjects"])
# print(info["age"])
# # changing value of key
# info["learning"]="java"          #assigningo or updating  new value to key it can override existing value
# info["surname"]="Agarwal"    #we can also add new key value pair just like assignment
# print(info)

# null_dict={}            #creating null dictionry
# print(null_dict)

# #creating nested dictionary
# student={
#     "name":"krishna",
#     "subjects":{
#         "math":90,
#         "chem":90,
#         "phy":88, 
#                }
#          }
# print(student)
# print(student["subjects"])
# print(student["subjects"]["chem"]) #nested dictionary me se relevant info ko nikalne ke liye multiple square bracets ka use kar sakte hai

# #  DICTIONARY METHODS
# print(student.keys())   #return  all keys in form of dictionary
# print(list(student.keys()))  # typecast in list return key in form of list
# print(len(student))    #find length of dictionary return number of keys in dictionary
# print(student.values()) #return all values
# print(student.items())#return all key value pair in form of tuple

# print(student["name"])         #  print(student["name2"])  give error 
# print(student.get("name"))      # print(student.get("name2"))   cannot gicve erroe ,return none hence we use get method

# # update new key value pair in dictionary
# #iske ander hum new dictionary banke usko bhi pass kar sakte hai old dictionary me
# student.update({"city":"delhi"})
# print(student)

# new_dict={"country":"India","age":23}
# student.update(new_dict)
# print(student)


#   SETS

collection={1,2,3,4,"hello"}
print(collection)
print(type(collection))

collection={1,2,3,4,4,3}
print(collection)          #list ignore duplicate values   DUPLICATE values are not allowed in set
print(len(collection))

# syntax to crerate empty set
collection=set()
print(collection)

# SET METHODS
collection.add(1)   #add method add an element
collection.add(2)
collection.add(1)
collection.add("krishna")
collection.add((1,2,3))  #add tuple in set
#   collection.add([1,2,3])    give an error unhashable type list
print(collection)
collection.remove(1)   
print(collection)# remove method remove an element
collection.clear()  #empty the set
print(collection)
print(len(collection))


collection1={"hello","world","python","apnacollege"}
collection2={"world",1,345,2002,"python"}
print(collection1.pop())    #pop any random value from set

print(collection1.union(collection2))     #combine and return both set values
print(collection1.intersection(collection2)) #combine and return common values

 



