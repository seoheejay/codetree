n = int(input())

# Please write your code here.
class Person:
    def __init__(self, name,street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

people = []
for _ in range(n):
    name,street_address, region = input().split()
    people.append(Person(name,street_address, region))

lastper = sorted(people, key = lambda p : p.name)

print("name",lastper[n-1].name)
print("addr",lastper[n-1].street_address)
print("city",lastper[n-1].region)