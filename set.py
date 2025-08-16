# createset = {"amit" , "giri" , "jaunpur", "india"}
# print(type(createset))
# print(createset)

# newset = {"amit", "amit"}
# print(newset)  # not allosw duplicte


newset ={"amit", 'giri' , 1, 3, False , True, 0}
print(newset) # it is unorderd 1, true , 0 false bothe are treatd as same in set 


# can not acces to set index or set iteam
# but set iteam can be printed by applying to the loop
for x in newset:
    print(x)

# add elememnt  in set  but can not be update the elmetn in the set 
print("amit" in newset) # give boolean value in answer 
print("rahul" in newset)

newset.add("rahul") # add elemnt in the set 
print(newset)

# adding to set 

oldset = {"mataji", "papaji"}

newset.update(oldset)

print(newset)
"""Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates.
"""