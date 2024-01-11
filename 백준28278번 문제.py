from sys import stdin

n = int(input())
s = []
for _ in range(n):
    a = stdin.readline().split()
    if a[0] == 1:
        s.append(a[1])
    elif a[0] == 2:
        if s != []:
            print(s.pop())
        else :
            print(-1)
    elif a[0] == 3:
        print(len(s))
    elif a[0] == 4:
        if s != []:
            print(0)
        else :
            print(1)
    elif a[0] == 5:
        if s != []:
            print (s[-1])
        else :
            print(-1)
## 왜 틀렸는지를 모르겠음
