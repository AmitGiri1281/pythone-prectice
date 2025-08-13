# created using []


mylist = ["mango", "apple", "banana"]
print(mylist[0])
print(len(mylist))

testlist = [1 ,"amit", False]
print(testlist)
print(type(testlist)) 
newlist=(("amit", "giri"))
print(type(newlist))
"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""


# in pytthon negetive indexing means starting from the end of thie list

rangelist = ["amit","giri","sachin","rohan","rajesh"]
print(rangelist[2:4])

if "rohan" in rangelist:
    print("yes")


print(rangelist[-2:])



rangelist.insert(3, "balck")
rangelist[1]="red"
print(rangelist)