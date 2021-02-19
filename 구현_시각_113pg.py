n = int(input())
l = [str(i)+str(j)+str(k) for i in range(0, n+1) for j in range(60) for k in range(60)]

cnt = 0
for i in l:
    for j in i:
        if j == '3':
            cnt += 1
            break
print(cnt)
