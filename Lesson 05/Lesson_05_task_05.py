src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

numbers = set()
unique = [i for i in src if i not in numbers and (numbers.add(i) or True)]
print(unique)