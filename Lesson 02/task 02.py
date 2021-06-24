def get_symbol(x):
    if x[0] in '+-':
        return x[0]

list_1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0
while i < len(list_1):
    sign = get_symbol(list_1[i])
    if list_1[i].isdigit() or (sign and list_1[i][1:].isdigit()):
        if sign:
            list_1[i] = sign + list_1[i][1:].zfill(2)
        else:
            list_1[i] = list_1[i].zfill(2)

        list_1.insert(i, '"')
        list_1.insert(i + 2, '"')
        i += 2

    i += 1

print(list_1)