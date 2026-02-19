# a = 10
# b = 20

# temp = a
# a = b
# b = temp

# print("a = ",a)
# print("b = ",b)
import secrets

SECRET_KEY = secrets.token_hex(16)  # 16 bytes → 32 hex chars
print(SECRET_KEY)