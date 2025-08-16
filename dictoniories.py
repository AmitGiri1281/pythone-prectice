# crete as key : pointer 

mydictionaries ={
    "name": "Amit Giri",
    "age" : 50,
    "address" : "jaunpur uttarparedsh" ,
    "age": 32
    }
print(mydictionaries) 
 dictionary iteam or orderded , changeable and do not allow duplicates
 dictionry iteam can be refferd by key

print(mydictionaries["name"])

print(mydictionaries["age"])
print(len(mydictionaries))
print(type(mydictionaries))
x  = mydictionaries.values() # it give all values of dictionary 
print(x)
x = mydictionaries.keys() # it gives all keys of dictionary


# y = cast.keyS()
# print(y)
# cast["gosai"] = "goswami"

# print(x)

mydictionaries["name"] = "rahul "
print(mydictionaries)

newdict = {
    "name": "amit giri" , 
    "class" : "m tech (cse)"

}

mydict = newdict.copy()
print(mydict) # copy to the dictionoary 

