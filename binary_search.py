"""Write a Python program that:

Takes a list of integers as input
Converts the list into a set to remove duplicates
Sorts the unique elements
Searches for a target element using Binary Search
Prints whether the element is found or not
Instructions:

Use set for uniqueness
Use sorting before binary search
Implement binary search manually (not using built-in)
Write clean and readable code
Explain time complexity"""


def binary_search(lst : list[int], target: int) -> str:
    left  = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2

        if lst[mid] == target:
            return f"Found at index {mid}"
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return f"Not Found"


lst_int = [int(x) for x in input("Enter your Value with Spaces: ").split()]

target = int(input("Enter your target Value: "))

unique_value_sorted = sorted(set(lst_int))

print(binary_search(lst=unique_value_sorted, target=target))