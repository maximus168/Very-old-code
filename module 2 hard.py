num_ = int(input('Введите число: ', ))
list = []
for i in range(1, num_):
    for j in range (i+1, num_):
        sum = int(i + j)
        if num_ % sum == 0:
            list += f'{i}{j}'
print('result:', list)
