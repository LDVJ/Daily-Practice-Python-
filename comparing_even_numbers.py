def check_nice_array(n, array, k):
    count = 0
    for i in array:
        if i % 2 == 0:
            count += 1  
    print("Nice Array" if count > k else "Bad Array")