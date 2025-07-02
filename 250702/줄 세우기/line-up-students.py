# Please write your code here.
class info:
    def __init__(self, height, weight):
        self.height, self.weight = height, weight

students = []
n = int(input())

for i in range(n):
    height, weight = map(int, input().split())
    students.append((i+1,info(height, weight)))

students.sort(key = lambda x: (-x[1].height, -x[1].weight))

for idx, student in students:
    print(student.height, student.weight, idx)