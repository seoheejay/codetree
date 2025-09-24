#야바위/ 3개의 종이컵, 하나에 조약돌
#N번에 걸쳐, a번과 b번 종이컵 교환 -> c번 open -> 조약돌 있으면 점수 얻음 cnt
max_cnt = 0
n = int(input())

#1,2,3 다 돌려보고 기록할 변수
f_score  = 0
s_score = 0
t_score = 0

#리스트 이용하자 (index 1 start)
f_list=[0,1,0,0]
s_list=[0,0,1,0]
t_list=[0,0,0,1]
#처음 조약돌 어디다가 둬야하는지 내가 설정해야 함
for _ in range(n):
    a, b, c = map(int, input().split()) #a,b교환 c오픈
    #교환작업
    f_list[a],f_list[b]=f_list[b],f_list[a]
    s_list[a],s_list[b]=s_list[b],s_list[a]
    t_list[a],t_list[b]=t_list[b],t_list[a]
    #c오픈
    if f_list[c] == 1: f_score+=1
    elif s_list[c] ==1 : s_score+=1
    elif t_list[c] ==1: t_score+=1
max_cnt = max(f_score,s_score,t_score)

print(max_cnt)