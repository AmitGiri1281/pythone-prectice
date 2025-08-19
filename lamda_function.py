# x = lambda a: a + 5
# print(x(5))


# x = lambda a, b, c, : a+ b + c
# print(x(5,6,2))


# def myfun(n):
#     return lambda a : a*n


# mydoubler = myfun(2)

# print(mydoubler(11))



def myfunc(n):
    return lambda a : a*n
mydoubler = myfunc(2)
mytripler = myfunc(3)


print(mydoubler(11))
print(mytripler(11))