str1='This is our first string\n'          #Three Ways To Store String
str2="This is our second string\n"
str3="""This is our third string\n"""
str4="this is our 4th string.\n we create it in python."
print(str1,str2,str3,str4)
str5="krishna"
str6="Agarwal"
concatstr=str5+str6
print(concatstr)            #print length of string
print(len(str5))
print(len(concatstr))

#print character of string with the help of indexing 
ch=str5[0]
print(ch)
print(str5[4])

#str5[3]="k"     not possible as string object does not allow/support item assignment

#  SLICING in python 
#used to break the string or to find any part of string

str7="apnaCollege"
print(str7[1:4])       #isme jo ending index hota hai nwoh count nhi hota 
print(str7[:5])    #    is same as print(str[0:5])   starting index miss hai toh compiler vby default o le leta hai
print(str7[1:])    #     is same as print(str[1:len(str)])  ending index miss hone ka matlb hum last index tak jana chate hai

#  SLICING SPECIAL CASE negative index negative index means indexing start fron backside
str8="apple"
print(str8[-5:])  
print(str8[-4:-1])  
print(str8[-1])  

 
# STRING FUNCTIONS (changes occur are temprory not permanent ) 

str9="I am studying python from Apna College"
print(str9.endswith("ege"))   #return true or false
print(str9.endswith("on"))
print(str9.capitalize())   #capitalize the first letter of string 
                           #isse sirf change ek bar ke lkiye hoga not permanently
                          #for permanent change str=str.capitalize()

print(str9.replace("o","a"))            #replaces all occurences of old with new
print(str9.replace("python","javascript"))


print(str9.find("o"))          #given word ko string me find karta hai if exist toh                          
print(str9.find("python"))      # first occurence ka starting index print ho jayega
print(str9.find("read"))        #return -1 means read is n ot exist in given string
                                   
print(str9.count("o"))      #count occurence of given string



