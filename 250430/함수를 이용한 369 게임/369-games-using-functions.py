a, b = map(int, input().split())

# Please write your code here.
def fun(a,b):
    cnt=0
    for i in range(a,b+1):
        if i%3==0:
            cnt+=1
        else:
            i=str(i) 
            for x in i: #2랑9
                if x=="3" or x=="6" or x=="9":
                    cnt+=1
                    break
    return cnt

print(fun(a,b))



