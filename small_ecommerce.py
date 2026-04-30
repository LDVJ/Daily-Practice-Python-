class Product:
  def __init__(self,name : str, price : float,category:str) -> None:
    self.product_name = name
    self.product_price = price
    self.product_category = category
  
  def get_info(self):
    print(f"Name: {self.product_name}")
    print(f"Price: ₹{self.product_price}")
    print(f"Category: {self.product_category}")
  
  def apply_discount(self, percentage : float) -> int:
    self.percentage = percentage
    self.product_price -= (self.percentage/100 * self.product_price)
    print(f"New price after {self.percentage}% discount: ₹{self.payable_price}")
  
class PhysicalProduct(Product):
  def __init__(self, name : str, price : float, category : str, weight_kg : float) ->None:
    super().__init__(name, price, category)
    self.product_weight_kg = weight_kg
  
  def get_info(self):
    super().get_info()
    print(f"Shipping Weight: {self.product_weight_kg} kg")
  
  def shipping_cost(self):
    return self.product_weight_kg * 50
    
class DigitalProduct(Product):
  def __init__(self, name: str, price : float, category : str, file_size_mb : float) -> None:
    super().__init__(name,price,category)
    self.product_file_size_mb = file_size_mb
  
  def get_info(self):
    super().get_info()
    print(f"File Size: {self.product_file_size_mb} MB")
    print("Delivery: Instant Download")
    
  def shipping_cost(self):
    return 0
  
def checkout(product : PhysicalProduct | DigitalProduct):
  print("--- Checkout ---")
  product.get_info()
  print(f"Shipping Cost: ₹{product.shipping_cost()}" + "\n")

p1 = PhysicalProduct("Python Programming Book",450, "Books", 0.8)
print("--- Product Info ---")
p1.get_info()
p1.apply_discount(percentage=10)
checkout(p1)

p2 = DigitalProduct("Data Science Masterclass", 999, "Online Course", 1200)
print("--- Product Info ---")
p2.get_info()
checkout(p2)
