def odd_nums(a, b):
    for num in range(a, b + 1):
        if num % 2 != 0:
            yield num


print(odd_nums(a=1, b=15))
for i in odd_nums(a=1, b=15):
    print(i)
