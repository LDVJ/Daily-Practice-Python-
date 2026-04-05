def question(arr, n, m):
    for i in range(0,m,1):
        print(arr[0][i], end=" ")
    for i in range(1,n,1):
        print(arr[i][m-1], end=" ")
    for i in range(m-2,-1,-1):
        print(arr[n-1][i], end=" ")
    for i in range(n-2,0,-1):
        print(arr[i][0], end=" ")
        

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12],
       [13,14,15,16]]

question(arr, n=4, m=4)