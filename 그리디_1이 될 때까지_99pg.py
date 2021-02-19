n, k = map(int, input().split())
t = 0
a = []
N = n
cnt = 0
while True:
    a.append(N%k)
    N //= N
    cnt += 1
    if N == 0:
        break

t = sum(a)+cnt
