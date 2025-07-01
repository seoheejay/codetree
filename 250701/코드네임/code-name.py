MAX_N = 5
"""
codenames = []
scores = []
for _ in range(MAX_N):
    codename, score = input().split()
    codenames.append(codename)
    scores.append(int(score))
"""
# Please write your code here.
class Person:
    def __init__(self, codename="", score=0):
        self.codename = codename
        self.score = score


people = []
for _ in range(5):
    codename, score =  input().split()
    people.append(Person(codename, int(score)))

minperson = min(people, key=lambda p: p.score)
print(minperson.codename, minperson.score)
