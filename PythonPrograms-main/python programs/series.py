# # WAP to sum the series 
# # 1+1/2+1/3........1/n

# num=int(input("enter number of terms: "))
# sum=0
# for i in range(1,(num+1)):
#     sum=sum+(1/i)
# print("sum= ",sum)  


# WAP to sum the series 
# 1+1/4+1/9........1/n^n

num=int(input("enter number of terms: "))
sum=0
for i in range(1,(num+1)):
    sum=sum+(1/i**i)
print("sum= ",sum)  
