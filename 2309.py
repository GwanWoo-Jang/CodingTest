arr = []
for i in range(9):
    arr.append(int(input()))
for i in range(0,9):
    for j in range(i+1,9):
        new_arr = arr[:]
        new_arr.remove(arr[i])
        new_arr.remove(arr[j])
        arr_sum = 0
        for k in new_arr:
            arr_sum += k
        if arr_sum == 100:
            break
    if arr_sum == 100:
        break
new_arr.sort()
for i in new_arr:
    print(i)
