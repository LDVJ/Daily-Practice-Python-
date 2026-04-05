def question(arr, n):
    for i in range(n-1, -1, -1):
        print(arr[i][0], end=" ")
    for i in range(1,n-1,1):
        print(arr[i][i], end=" ")
    for i in range(n-1,-1,-1):
        print(arr[i][n-1], end=" ")
        

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

question(arr, n=4)