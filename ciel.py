import math
def calculate_ceil_average(n, arr):
    sum = 0
    for i in arr:
        sum += i
    
    avg = sum/n
    print(math.ceil(avg))