a=int(input())
z=[input().strip() for _ in range(a)]
k=int(input())
l=len(z[0])
for i in range(a):
    print(end=z[i][0])
    for j in range(1,l-1):
        print(end=z[(i+k)%a][j])
    print(z[i][-1])
