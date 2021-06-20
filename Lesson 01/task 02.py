numbers = [i ** 3 for i in range(1, 1001)]
print(numbers)

numbers = [i ** 3 for i in range(1001) if i % 2 != 0]
for i in numbers:
    str_list = list(str(i))
summ = sum([int(j) for j in str_list])
if summ % 7 == 0:
    print(i)
print(summ)

numbers = [i ** 3 for i in range(1001) if i % 2 != 0]
for i, _ in enumerate(numbers):
    numbers[i] += 17
for i in numbers:
    str_list = list(str(i))
summ = sum([int(i) for i in str_list])
if summ % 7 == 0:
    print(i)
