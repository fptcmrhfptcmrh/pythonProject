import math
a=input().split()
ax=int(a[0])
ay=int(a[1])
ar=int(a[2])
b=input().split()
bx=int(b[0])
by=int(b[1])
br=int(b[2])
d=math.sqrt(abs(ax-bx)**2 + abs(ay-by)**2)
rs=ar+br
if d>=rs:
    print("NO")
else:
    print("YES")
