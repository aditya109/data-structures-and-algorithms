def fun(X, diff, K):
    n = len(X)
    prev = 0
    removed = 0

    for i in range(1, n):
        if i== n-1 or X[i+1]-X[prev]>diff or removed == K:
            if X[i]-X[prev] > diff:
                return False
            prev = i
        else:
            removed+=1
    return removed==K

def solve (X, K):
    temp = []

    for i in X:
        temp.append(i)

    X = temp

    print(X)


    hi = X[len(X)-1] - X [0]
    lo = 0

    while lo < hi :
        mid = (lo + hi)//2

        if fun(X, mid, K):
            hi = mid
        else: lo = mid+1
    return lo 

N = int(input())
X = map(int, input().split())
K = int(input())

out_ = solve(X, K)
print (out_)
