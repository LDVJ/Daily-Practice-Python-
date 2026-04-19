x = [int(x) for x in input("Enter your list of number: ").split()]
target = int(input("Enter you target Value: "))

# def check_target(x : list, target: int) -> bool:
#     for i in range(len(x)):
#         for j in range(i+1,len(x)):
#             if x[i] + x[j] == target:
#                 print(f"{x[i]} + {x[j]} = {target}")
#                 return True
    
#     return False

#optimization
def check_target(x : list, target : int) -> bool:
    i = 0
    j = len(x) - 1
    while i < j:
        if x[i] + x[j] == target:
            print(f"{x[i]} + {x[j]} = {target}")
            return True
        elif x[i] + x[j] > target:
            j -= 1
        else:
            i += 1
    return False

x.sort()

print(check_target(x=x, target=target))