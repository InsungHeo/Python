n, m, k = map(int, input().split())
num = list(map(int, input().split()))
a = num[0]
b = num[0]
t = 0
total = 0

num.sort()
a = num[n-1]
b = num[n-2]

cnt = 1
while True:
    if cnt > m:
        break
    if cnt%(k+1) == 0:
        total += b
        cnt += 1
    else :
        total += a
        cnt += 1

print(total)
