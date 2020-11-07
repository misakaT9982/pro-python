for i in range(101, 201):
    for j in (2, int(i ** 0.5)):  # range(2,105) 从2取到104
        if i % j == 0:
            break
    else:
        print(i, '是质数')

# 假设成立法求素数
print("==============================")
for i in range(2, 101):
    flag = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            flag = False
            break
    if flag:
        print(i)

# 使用计数法求素数
for i in range(2, 101):
    count = 0
    for j in range(2, i):
        if i % j == 0:
            count += 1
    if count == 0:
        print(i, '质数')
    else:
        print(i, '不是质数','能被',count,'个数整除')