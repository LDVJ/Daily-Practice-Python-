# lst = [1,2,3,4]

# for i in lst:
#     if i % 2 == 0:
#         lst.remove(i)

# print(lst)


# # def greet(name = "Guest", msg): # original 
# def greet(msg, name = "Guest"): # fix
#     print(msg, name)

# print(greet(msg="hello"))

# a = [1,2,3] # original 
# a = [1,2,3,4,5,6] # fix
# print(a[5])

# d  =  {
#     "a":1
# } # orignal
# d  =  {
#     "a":1,
#     "b":1
# } # fix
# print(d["b"])

def func(lst : list) -> int | float:
    lst.append(10)

x = [1,2]
func(x)
print(x)
