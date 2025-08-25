mytuple = ("apple", "banan", "chery")
myit = iter(mytuple)


print(next(myit))

print(next(myit))
print(next(myit))


by applying for loop 

mytuple = ("ampple" , "banana", "mango")

for x in mytuple:
    print(x)




class MyNumber:
    def __iter__(self):
        self.a =1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a
            return x
        else:
            raise StopIteration
        
myclass = MyNumber()
myiter = iter(myclass)


for x in myiter:
    print(x)