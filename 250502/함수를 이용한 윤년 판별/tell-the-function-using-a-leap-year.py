y = int(input())

# Please write your code here.
def fun(y):
    if y%4==0:
        print("true")
    else:
        if y%100==0 and y%400!=0:
            print("true")
        else:
            print("false")
fun(y)