x, y = map(int, input().split())

cnt = 0

'''
def interest(num):
    #매개변수로 받은 i에 대해 정확히 한 자리만 다른지 볼거임
    #list -> str로 바꿔서 for문으로 한 자리씩 보자
    su_m=0 #sum이 1이어야 함
    lst = []
    s = str(num)
    for x in str(num): #"1118"
        lst.append(x) #["1","1","1","8"]
    for i in range(len(lst)-1):
        if lst[i]!=lst[i+1]:
            su_m+=1
    if su_m==1:
        return 1
    else:
        return 0
'''


def interest(num):
    s = str(num)
    lst = [ch for ch in s] 

    # 모든 자리 중 한 자리만 다른지 확인
    for i in range(len(lst)):
        temp = lst[:i] + lst[i+1:]  # i번째 제외
        # 나머지가 모두 같은지 확인
        if all(ch == temp[0] for ch in temp):
            # 제외한 자리가 다른 숫자인지 확인
            if lst[i] != temp[0]:
                return 1
    return 0
         

for i in range(x,y+1): #x이상 y이하 숫자 다 탐색
    cnt+=interest(i)

print(cnt)