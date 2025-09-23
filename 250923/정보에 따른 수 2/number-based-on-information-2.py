#알파벳 S,N T개가 주어짐
#특정위치 x=k로부터 가장 가까이에 있는 알파벳 S 까지의 거리 d1
#                                    알파벳 N 까지의 거리 d2
# if d1 <= d2 이면 x=k가 특별한 위치가 됨
# a<=x<=b 까지의 위치 중 특별한 위치의 수를 구하기

cnt_special = 0

n, a, b = map(int, input().split())

'''
lst=[]
for i in range(n):
    d,x = input().split()
    lst.append((d,int(x))) #[(S,10),(N,4),(S,1)]
'''
#N이랑 S따로 저장하자
S_pos = []
N_pos =[]
for _ in range(n):
    d,x = input().split()
    x=int(x)
    if d =="S":
        S_pos.append(x)
    else:
        N_pos.append(x)

lst_cnt=[0]*(b+1) #0부터 b까지 인덱스 가능
#이제 여기다가 1기록해줘야함
for i in range(a,b+1):
    d1 = min(abs(i-s) for s in S_pos) #가장 가까운 S까지 거리
    d2 = min(abs(i-n) for n in N_pos) #가장 가까운 N까지 거리

    if d1<=d2:
       lst_cnt[i]=1 


'''
for i in range(a,b+1):
    if lst_cnt[i]==1:
        cnt_special+=1
        '''
cnt_special = sum(lst_cnt)
print(cnt_special)

'''
Q. 특정위치 x가 special이 되려면
S가 N보다 가까워야 함

S     N            S
1     4           10
---------------------
-> 아 그럼 중간위치를 잡아야겠다
(S+N)//2 몫까지 괜찮음 -> 1로 써주고, 이거 나중에 for문 돌면서 cnt
1. 몫 2 -> 1,2 괜찮은거고 
2. 몫 7 -> 7,8,9,10 괜찮은거임
'''