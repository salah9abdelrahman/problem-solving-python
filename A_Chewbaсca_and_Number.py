num = input()
res = ''
for i in range(len(num)):
    if i == 0 and num[i] == '9':
        res += num[i]
    elif int(num[i]) >= 5:
        res += str(9 - int(num[i]))
    else:
        res += num[i]

print(res)
