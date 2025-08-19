cars = ["ford" , "Volvo", "bmw"]
cars[0] = "toyta"

print(cars)
print(len(cars))

for x in cars:
    print(x)

cars.append("honada") # add elemnt 
print(cars)

cars.pop(1) # remove cars[1]
print(cars)