A = input()
cnt = 0 #가짓수 세기위한 변수

for i in range(len(A)-1):
    if A[i]=="(":
        for j in range(i+1,len(A)): 
            if A[j]==")":
                cnt+=1
print(cnt)
