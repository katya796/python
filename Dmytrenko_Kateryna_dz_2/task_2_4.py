def convert_name_extract(list_in: list) -> list:
    new_list = []
    for element in list_in:
        element_new = element[::-1]
        name = element[(len(element_new) - element_new.index(" "))::]
        new_list.append(f'Привет, {name.title()}!')
        list_out = new_list
    return list_out


my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
result = convert_name_extract(my_list)
print(result)
