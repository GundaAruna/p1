#Creating a dictionary 
#1.by using key:value pair syntax
d={"name":"Dhanusha","age":15,"phone":8978655490}
print(d)
print(type(d))
#Accessing keys followed by its respective value by using loop
for i in d:
    print(i,d[i])
#Modification done on values of a dictionary by using the syntax dictionary[key]=value
d["name"]="HAriTeja"
print(d)
#adding key:value pairs from one dictionary into the dictionary
d1={"Address":"Anantapur","pincode":515455}
d.update(d1)
print(d)
