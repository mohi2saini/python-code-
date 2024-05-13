tup=(12,34,56)
print(type(tup))
print(tup[2])

tuple=()   # we can also create an empty tuple
print(tuple)
print(type(tuple))

tuple=(1,)   # this is the right way to create a tuple with single element  we must have to use , after element
print(tuple)
print(type(tuple))

tuple=(1)   # if we write like this then python will consider it as integer
print(tuple)
print(type(tuple))

#  TUPLE METHODS 
tup=(1,2,3,1)
print(tup.index(3))
print(tup.count(1))
