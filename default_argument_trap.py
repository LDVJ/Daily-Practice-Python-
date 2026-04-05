def func(a, lst=[]):
    lst.append(a)
    return lst

print(func(2))
print(func(4))
print(func(3, []))
print(func(5))
