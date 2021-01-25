N, X = input().split()
N = int(N)
X = int(X)
arr = list(map(int, input().split()))
ans = []
for i in arr:
    if i < X:
        ans.append(i)

for i in ans:
    print(i,end = " ")
