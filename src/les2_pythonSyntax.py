import math

# number to string
print("string" + str(4))

#if
a = 30
if(a < 20):
    print(1)
elif (a == 20):
    print(2)
else:
    print(3)

#list - different types
list = [1,123,"test", [2,4]]
print(list)
print(list[3][0])
list.append("addEl")
print(list)
list.insert(2,"insert")
print(list)
list.remove(123)
print(list)

#set-only unique values
set = {12,12,17,"test"}
print(set)

#dictionary
dic = { "name" : "Rita", "address" : {"city": "Kharkiv"} }
print(dic["name"])
print(dic["address"]["city"])

#function
def sum (a, b, c):
    print (a+b+c)

sum(1,2,3)


#import math
print(math.cos(60))
print(math.pi)