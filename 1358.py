import sys
input = sys.stdin.readline

w,h,x,y,p = map(int, input().split())
r = h//2
cnt = 0
for _ in range(p):
    x1, y1 = map(int, input().split())
    if (x1-x)**2+(y1-(y+r))**2 <= r**2:
        cnt += 1
    elif x<=x1<=(x+w) and y<=y1<=(y+h):
        cnt += 1
    elif (x1-(x+w))**2 + (y1-(y+r))**2 <= r**2:
        cnt += 1
print(cnt)