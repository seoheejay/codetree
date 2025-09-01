n = int(input())

#2차원 
lst = [tuple(map(int, input().split()))for _ in range(n)]

#최대 뽑기 (x,y)
def choose(i,j,k):
    x1,y1 = lst[i]
    x2,y2 = lst[j]
    x3,y3 = lst[k]
    #단, x축과 평행, y축과 평행
    if (x1==x2 or x1==x3 or x2==x3) and (y1==y2 or y2==y3 or y1==y3):
        return(area(x1,y1,x2,y2,x3,y3))
    else:
        return 0
    
#삼각형 넓이에 2 곱한 값
def area(x1,y1,x2,y2,x3,y3):
    return abs((x1*y2 + x2*y3 + x3*y1)-(x2*y1+x3*y2+x1*y3)) #신발끈

#3개 골라 삼각형
max_area = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            max_area = max(max_area, choose(i,j,k))

print(max_area)
