import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))


# 제거된 원소의 위치를 removed_idx라 가정헀을 때,
# 인접한 원소간의 차의 합을 계산해 반환합니다.
def score(removed_idx):
    # 합을 계산합니다
    sum_val = 0

    # 바로 직전에 적혀있던 숫자를 기록합니다.
    # -1인 경우, 아직 숫자가 기록된 적이 없다는 뜻입니다.
    prev = -1

    # 각 숫자들을 순회합니다.
    for i in range(n):
        # 지워진 원소라면 패스합니다.
        if i == removed_idx:
            continue

        # 이전에 적혀있던 숫자가 있는 경우에만
        # 인접한 숫자간의 차를 sum_val에 더해줍니다.
        if prev != -1:
            sum_val += abs(arr[i] - prev)

        # 마지막으로 적혀있던 숫자 값을 갱신해줍니다.
        prev = arr[i]

    # 인접한 원소간의 차의 합을 반환합니다.
    return sum_val


min_score = INT_MAX

# 2배를 할 숫자의 위치 i를 결정하고,
# 그 다음 제거할 숫자의 위치 j를 결정하여
# 남은 숫자들의 인접한 차의 합 중
# 최솟값을 찾습니다.
for i in range(n):
    arr[i] *= 2

    # 제거할 숫자의 위치를 결정합니다.
    for j in range(n):
        min_score = min(min_score, score(j))

    # 그 다음 상태 진행을 위해, 
    # 이전에 2배를 한 값을 다시 이전 상태로 만들어줍니다.
    arr[i] //= 2

print(min_score)
