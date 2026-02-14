def solve(num, K):
    for i in range(1,num+1):
        if i % K == 0:
            print(i)


num = int(input())
k = int(input())

solve(num=num,K=k)
