n = int(input())
arr = []
cmd = []
for i in range(n):
    # str, num = input().split()
    # num = int(num)  -> size같은 경우 num value가 없음
    cmd = input().split()
    str = cmd[0]
    num = int(cmd[1]) if len(cmd) > 1 else None

    if str == "push_back":
        arr.append(num)
        # print(num)
    elif str == "pop_back":
        arr.pop()
        # print(num)
    elif str == "size":
        print(len(arr))
    elif str == "get":
        print(arr[num-1])

