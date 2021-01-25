n = int(input())
ans = 0
for i in range(1, n):
    arr = []
    num = i
    while(i != 0):
        arr.append(i%10)
        i = i//10
    sum_arr = num
    for j in arr :
        sum_arr += j
    if n == sum_arr:
        ans = num
        break

print(ans)
    
    
