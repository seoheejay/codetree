class Info:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name,height,weight

#변수 입력
people  = []
for i in range(5):
    name, height, weight = tuple(input().split())
    people.append(Info(name,int(height),float(weight)))


people.sort(key=lambda x: x.name)
print("name")
for person in people:
    print(person.name, person.height, person.weight)
print()

people.sort(key=lambda x: -x.height)
print("height")
for person in people:
    print(person.name, person.height, person.weight)