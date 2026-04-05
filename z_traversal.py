def question(arr, n , m):
    for i in range(0,m,1):
        print(arr[0][i], end=" ")
    i = 1
    j = m - 2
    while i < n and j >= 0:
        print(arr[i][j], end=" ")
        i += 1
        j -= 1
    for j in range(1,m,1):
        print(arr[n-1][j], end=" ")
        

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

question(arr, n=4,m=4)