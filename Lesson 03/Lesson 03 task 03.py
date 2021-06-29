def thesaurus(*names):
    dict_of_names = {}
    for name in names:
        key = name[0].title()
        if key not in dict_of_names:
            dict_of_names[key] = []
        dict_of_names[key].append(name)
    return dict_of_names


print(thesaurus('Лена', 'Рома', 'Александр', 'Алексей'))