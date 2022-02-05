def thesaurus(*args) -> dict:
    dict_out = {}
    for i in args:
        if dict_out.get(i[0]) is not None:
            dict_out.get(i[0]).append(i)
        else:
            dict_out.setdefault(i[0], [i])
    return dict_out


print(thesaurus("Иван", "Мария", "Петр", "Илья"))


