class Info:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

n=int(input())
people = []
for _ in range(n):
    name,height,weight=tuple(input().split())
    people.append(Info(name,int(height),int(weight)))

people.sort(key = lambda x: (x.height,-x.weight))

for person in people:
    print(person.name,person.height, person.weight)

