arr = []
arr_add = []
arr_max_sum = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))

for i in range(len(arr) - 2):
    for j in range(4):
        arr_add.extend(arr[i][j:j + 3])
        arr_add.append(arr[i + 1][j + 1])
        arr_add.extend(arr[i + 2][j:j + 3])
        arr_max_sum.append(sum(arr_add))
        arr_add = []

print(max(arr_max_sum))
