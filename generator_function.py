def odd_traversal(n, arr):
    print(*(arr[i] for i in range(n) if i % 2 != 0)) # generator function