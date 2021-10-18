n = int(input())
reminders = []
while n > 0:
    reminder = n % 2
    n = n // 2
    reminders.append(reminder)

count = 0
result = 0

for i in range(len(reminders)):
    if reminders[i] == 0:
        count = 0
    else:
        count += 1
        result = max(result, count)

print(result)
