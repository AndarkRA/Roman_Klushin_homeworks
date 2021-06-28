typing = input('Введите число от 0 до 10 на английском: ')
def num_translate():
    num_translate = {'zero': 'ноль', 'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре',
    'five': 'пять', 'six': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
    print(num_translate.get(typing).title())
    return

num_translate()














