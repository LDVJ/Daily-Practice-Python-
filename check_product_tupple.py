def check_product(n, products, search_product):
    is_available = False
    for product in products:
        if product[0] == search_product:
            is_available = True
            break
    print("Available" if is_available else "Not Available")

products = (["apple",10],["banana",4],["guava",13])

check_product(n=len(products),products=products,search_product="guava")