x = int(input())

phone_book = {}

for i in range(x):
    text = input().split()
    phone_book[text[0]] = text[1]

while True:
    try:
        friend_name = input()
        if friend_name in phone_book:
            print(friend_name + "=" + phone_book[friend_name])
        else:
            print("Not found")
    except EOFError:
        break
