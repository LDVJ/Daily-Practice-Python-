def calculate_total_sales(n: int, sales_data: list) -> int:
    temp = 0
    for key, value in sales_data:
      temp += value
    print(temp)

hello = [("apple",10),("banana",5),("guava",8)]

# calculate_total_sales(3, sales_data={
#    "apple":10,
#    "banana":5,
#    "guava":8
# })

calculate_total_sales(3, sales_data=hello)

