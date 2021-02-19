n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = []
for i in range(n):
    b.append(min(a[i]))
b.sort()
print(b[n-1])
