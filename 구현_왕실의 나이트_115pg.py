start = input()
x = [[i, j] for i in range(1, 9) for j in range(1, 9)]
mv = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
cnt = 0

a = ord(start[0])-96
b = int(start[1])
s = [a, b]

for mn in mv:
    nx = [i+j for i, j in zip(s, mn)]
    for k in x:
        if k == nx:
            cnt += 1
print(cnt)
            
