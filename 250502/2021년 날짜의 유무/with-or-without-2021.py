M, D = map(int, input().split())

# Please write your code here.
def fun(M,D):
    result = False
    for i in range(1,13): #1월부터 12월
        if M==i:
            #D일 존재하는지 여부
            if M==2: 
                if D<=28:
                    result=True
                    break
            elif M in [1,3,5,7,8,10,12]:
                    if D<=31:
                        result=True
                        break
            elif M in [4,6,9,10,11]:
                    if D<=30:
                        result=True
                        break
            break


    if result == True:
        print("Yes")
    else:
        print("No")

fun(M,D)