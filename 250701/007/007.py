secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class Structprint:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time

sp = Structprint(secret_code,meeting_point,time)
print("secret code :",sp.s)
print("meeting point :",sp.m)
print("time :",sp.t)