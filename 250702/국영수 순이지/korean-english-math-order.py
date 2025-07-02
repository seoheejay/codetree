# Please write your code here.
class Score:
    def __init__(self, name, kor,eng, mat):
        self.name,self.kor, self.eng, self.mat = name,kor,eng,mat

students =[]
n = int(input())
for i in range(n):
    name, kor, eng, mat = tuple(input().split())
    students.append(Score(name, int(kor), int(eng), int(mat)))


students.sort(key = lambda x: (-x.kor, -x.eng, -x.mat))


for student in students:
    print(student.name, student.kor, student.eng, student.mat)