a = list(map(int,input().split()))
a.sort()
print(abs(a[0]+a[3]-a[2]-a[1]))