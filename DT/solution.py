a=int(input())
z1=[input().split() for _ in range(a)]
z2=[input().split() for _ in range(a)]
k=int(input())
def ch(x):
    return x<k
for i in range(a):
    for j in range(a):
        if ch(i) or ch(j) or ch(a-i-1) or ch(a-j-1):
            z1[i][j],z2[i][j]=z2[i][j],z1[i][j]
    print(*z1[i])
for i in z2:
    print(*i)
