product_name, product_code = input().split()
product_code = int(product_code)

# Please write your code here.
class Struc:
    def __init__(self, name="codetree", code=50):
        self.name = name
        self.code = code
struc = Struc()
print(f"product {struc.code} is {struc.name}")
struc = Struc(product_name, product_code)
print(f"product {struc.code} is {struc.name}")

