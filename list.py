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


newlist = ["amit", "giti"]
newlist.append("mata")
print(newlist)

oldlist = ["rahul" "giri"]
newlist.extend(oldlist)
print(newlist)
newlist.append(oldlist)
print(newlist)


newlist.insert(1, "balck")
print(newlist)


newlist.remove("giti")
print(newlist)

newlist.pop(1)
print(newlist)


list = ["amit", "giri" , "sacchin"]

for w in list:
    print(w)

for i in range(len(list)):
    print(list[i])

i=0
while i<len(list):
    print(list[i])
    i =i+1


newlist = ["amit", "giri", "mataji",  "papaji"]

checklist =[]

for i in newlist:
    if "a" in newlist:
        checklist.append(i)
        print(checklist)

newlist.sort()
print(newlist)
numberlist = [45, 12, 32, 2 ,34,44]

numberlist.sort(reverse=False)
print(numberlist)
numberlist.sort()



print(numberlist)
numberlist.reverse()
print(numberlist)


list coppy method

list = ["amit", "giri", "sachin", "rohan"]
newlist = ["rohan" ,"rajesh"]
newlist = list.copy()
print(newlist)

mylist = list[:]
print(mylist)

list =[1,2,3,4,5,6]
list2 =["amit", "giri", "sachin"]

# list3 =list +list2
# print(list3)

list2 =list.append()
print(list2)
