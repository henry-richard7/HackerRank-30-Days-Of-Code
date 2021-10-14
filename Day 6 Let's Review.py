def str_code(input_str):
    even_pairs = ''
    odd_pairs = ''
    for i in range(len(input_str)):
        if i % 2 == 0:
            even_pairs += input_str[i]

    for i in range(len(input_str)):
        if i % 2 != 0:
            odd_pairs += input_str[i]

    return f'{even_pairs} {odd_pairs}'


n = int(input())
input_arr = []
for i in range(n):
    input_arr.append(str(input()))

for i in input_arr:
    print(str_code(i))
