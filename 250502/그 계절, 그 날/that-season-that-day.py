Y, M, D = map(int, input().split())

# 어떤 계절인지 출력 3~5 봄, 6~8 여름, 12~2 겨울
def fun(Year,M,D):
    result = False 
    for i in range(1,13): #1월부터 12월
        if M==i:
            #D일 존재하는지 여부
            if M==2 and Year==False: #평년 
                for j in range(1,29): #28일까지
                    if D==j:
                        result=True
                        break
            elif M==2 and Year==True: #윤년
                for j in range(1,30): #29일까지
                    if D==j:
                        result=True
                        break
            elif M in [1,3,5,7,8,10,12]:
                for j in range(1,32): #31일까지
                    if D==j:
                        result=True
                        break
            elif M in [4,6,9,10,11]:
                for j in range(1,31): #30일까지
                    if D==j:
                        result=True
                        break
            break


    if result == True:
        sea(M)
    else:
        print("-1")

def sea(M):
    if M in [3,4,5]:
        print("Spring")
    elif M in [6,7,8]:
        print("Summer")
    elif M in [9,10,11]:
        print("Fall")
    elif M in [12,1,2]:
        print("Winter")


def Year(Y,M,D):
    result = False
    if Y%4==0:
        if Y%100==0:
            if Y%400==0: #4,100,400의 배수
                result = True
            else: #4의배수, 100의 배수이지만 400배수는 아님 > 윤년 아님
                result = False
        else:
            result = True

    else:
        result =False
    
    fun(result,M,D)
    
Year(Y,M,D)