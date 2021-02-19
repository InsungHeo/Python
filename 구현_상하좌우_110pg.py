n = int(input())
ip = list(input().split())

a = 1
b = 1

for i in range(len(ip)):
    if ip[i] == 'L' and b != 1:
        b -= 1
    elif ip[i] == 'R' and b != n:
        b += 1
    elif ip[i] == 'U' and a != 1:
        a -= 1
    elif ip[i] == 'D' and a != n:
        a += 1
    else :
        continue

print(a, b)
