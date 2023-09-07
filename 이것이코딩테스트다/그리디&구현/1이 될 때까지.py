#그리디
n,k = map(int,input().split()) // input값을 int형으로 변환하여 변수에 값 지정
result = 0

while True:

    # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k //n이 k로 나누어 떨어지지 않을때 가장 가까운 k로 나누어 떨어지는 수 알수 있음
    result += (n - target) // 총 연산을 수행하는 횟수
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)