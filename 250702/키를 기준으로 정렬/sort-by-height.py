"""
n = int(input())
name = []
height = []
weight = []


for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.

class stu:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

students=[]
for i in range(n):
    students.append(stu(name[i],height[i],weight[i])) 

students.sort(key = lambda x : x.height)

for student in students:
    print(student.name, student.height, student.weight)
"""

#클래스 선언
class Student:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

#변수 선언 및 입력
n = int(input())
students = []
for _ in range(n):
    name, height, weight = tuple(input().split())
    students.append(Student(name, int(height), int(weight)))

#정렬
students.sort(key = lambda x: x.height)

#출력
for student in students:
    print(student.name, student.height, student.weight)