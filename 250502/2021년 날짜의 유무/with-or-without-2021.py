M, D = map(int, input().split())

# Please write your code here.
def fun(M,D):
    result = False
    for i in range(1,13): #1월부터 12월
        if M==i:
            #D일 존재하는지 여부
            if M==2: 
                for j in range(1,29): #28일까지
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
        print("Yes")
    else:
        print("No")

fun(M,D)