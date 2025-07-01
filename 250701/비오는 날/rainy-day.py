n = int(input())
# Please write your code here.
class Da:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

da = []
for _ in range(n):
    date, day, weather = input().split()
    da.append(Da(date, day, weather))


da = sorted(da, key = lambda d:d.date) 

for i in range(n):
    if da[i].weather == "Rain":
        print(da[i].date, da[i].day, da[i].weather)
        break
