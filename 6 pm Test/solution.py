n,p=int(input()),int(input())
f,b=p//2,((n-p)//2)+1
if n%2==1:
    if n-p==1:
        b=0
    else:
        b=((n-p)//2)
l=[f,b]
print(min(l))
