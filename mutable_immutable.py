import copy

# x = "abc"
# y = x
# y += "d"
# print(x,y)

# a = [1,2,3]
# b = a
# b[0] = 100
# print(a)

# def fun():
#     print("hello")

# x = fun()
# print(x)

# a = [[0]*3]*3

# print(a)

# a[0][0] = 1

# print(a)


# a = [[1,2,3],[4,5,6]]
# # a = [1,2,3]
# b = a.copy()
# b[0][0] = 100

# print(a)

# s = "hello"
# s = list(s)
# s[0] = "H"
# print("".join(s))

a = "True"
b = {1:2,3:4,5:6}
for x, y  in zip(a, b):
    print(x,y)
    print(type(x))
    print(type(y))

print(zip(a))
# print(f"{a.upper():<10}",end="_")
