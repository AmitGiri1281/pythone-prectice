variable = ("amit", "giri",25, "jaunpur", "india") # tuple can contain diffrent data types

# when tuple cretae then it cannot be changed
# tuples are store duplicate values and elemnt is accessed by variable[0]

print(variable[0])
print(len(variable)) # print lengthe of tupele
print(type(variable))

createtupele =tuple(("rahuul", "giri")) #create tupes use (())
"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# wee can not add, remove or change item in tupple


# to add or remove item from tuple we need to convert it into a list
variable_list = list(variable)  # convert tuples to list after that use we can again covert it into tuple
variable_list = list(variable)  # convert tuple to list

#Aditio in tuple 
tuple1 = (1,2,3,4,5)
tuple2 =(6,7,8,9,10)
tuple3 = tuple1 + tuple2
print(tuple3)

t