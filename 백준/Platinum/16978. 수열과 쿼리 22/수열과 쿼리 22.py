import sys
input = sys.stdin.readline

def Main():
    def Modify(i, diff):
        while i <= N:
            tree[i] += diff
            i += (i & -i)
    def Sum(i):
        result = 0
        while i>0:
            result+=tree[i]
            i -= (i & -i)
        return result

    N = int(input())
    arr= [0]+list(map(int, input().split()))
    tree = [0]*(N+1)
    q1 = [0]
    q2 = []
    ans = []
    M = int(input())
    idx = 0
    for i in range(1,N+1):
        Modify(i,arr[i])
    for m in range(M):
        lst = list(map(int, input().split()))
        if lst[0] == 1:
            q1.append((lst[1],lst[2]))
        else:
            q2.append((lst[1],lst[2],lst[3],idx))
            idx += 1
            ans.append(0)
    q2.sort(key=lambda e: e[0],reverse=True)
    while q2 :
        cnt, A, B, ix = q2.pop()
        if cnt == 0:
            ans[ix] = Sum(B)-Sum(A-1)
        else:
            q2.append((cnt,A,B,ix))
            break
    for i in range(1,len(q1)):
        a,b = q1[i]
        Modify(a,b-arr[a])
        arr[a] = b
        while q2:
            cnt, A, B, ix = q2.pop()
            if cnt == i:
                ans[ix] = Sum(B) - Sum(A - 1)
            else:
                q2.append((cnt,A,B,ix))
                break
    for i in ans:
        print(i)
Main()