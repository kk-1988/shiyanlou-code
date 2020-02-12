i = 0
for i in range(1,101):
    if 0 == i % 7 or i % 10 == 7 or i // 10 == 7:
        continue
    else:
        print(i)
