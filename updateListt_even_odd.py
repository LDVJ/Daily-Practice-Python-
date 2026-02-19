def transform_array(n, arr):
    result = []
    if n == len(arr):
        for i in arr:
            if i % 2 == 0:
                result.append(-1)
            else:
                result.append(1)
        
    print(result)


