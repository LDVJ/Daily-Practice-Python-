#2, 10
# 2, 4, 8

def rangeOfTwo(left, right):
    if left < right:
        temp = left
        while True:
            if temp <= right:
                print(temp)
                temp = temp*2
            else:
                break


rangeOfTwo(4,10)