import random
from random import choice

"""Импортируем choice из random"""


def get_jokes(n, flag=False):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    """Создаем три списка из уловия задачи"""

    for i in range(n):
        random_index_1 = choice(nouns)
        random_index_2 = choice(adverbs)
        random_index_3 = choice(adjectives)
        out_jokes = f'{random_index_1} {random_index_2} {random_index_3}'
        # out_jokes = [random.choice(nouns), random.choice(adverbs), random.choice(adjectives)]    # использовался как альтернативный способ
        print(out_jokes)
        """Задали логику нашей функции с возможностью вывода более 1 радномно-собранной строки"""

        if flag == True:
            list_delete = out_jokes.split()
            for noun in nouns:
                for value in list_delete:
                    if noun == value:
                        nouns.remove(noun)
                        """Создан цикл для удаления повторяющихся слов из списка nouns"""

            for adverb in adverbs:
                for value in list_delete:
                    if adverb == value:
                        adverbs.remove(adverb)
                        """Создан цикл для удаления повторяющихся слов из списка adverbs"""

            for adjective in adjectives:
                for value in list_delete:
                    if adjectives == value:
                        adjectives.remove(adjective)
                        """Создан цикл для удаления повторяющихся слов из списка adjectives"""


get_jokes(n=2, flag=True)
"""Реализован вызов функции get_jokes"""
