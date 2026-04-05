def question(arr, n , m):
    for i in range(0,n,1):
        if i != n-1:
            print(arr[i][0])
        elif i == n-1:
            print(arr[i][0], end=" ")
    for j in range(1,m,1):
        print(arr[n-1][j], end=" ")
        

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

question(arr, n=3,m=4)