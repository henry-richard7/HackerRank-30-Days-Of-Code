n = int(input().strip())

arr = list(map(int, input().rstrip().split()))
reversed_array = arr[::-1]
print(" ".join(map(str, reversed_array)))
