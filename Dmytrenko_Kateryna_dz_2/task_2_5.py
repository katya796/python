from random import uniform
import math

def transfer_list_in_str(list_in: list) -> str:
    new_list = []
    for element in list_in:
        if math.floor(element*100)%100 < 10:
            new_list.append(f'{int(element)} руб 0{(math.floor(element*100)%100)} коп')
        else:
            new_list.append(f'{int(element)} руб {(math.floor(element * 100) % 100)} коп')
    str_out = new_list
    return str_out


my_list = [round(uniform(10, 100), 2) for _ in range(1, 16)]  # автоматическая генерация случайных 15 чисел
print(f'Исходный список: {my_list}')
result_1 = transfer_list_in_str(my_list)
print(result_1)


def sort_prices(list_in: list) -> list:
    list_in.sort()
    return list_in


print(id(my_list), my_list)
result_2 = sort_prices(my_list)
print(id(result_2), result_2)
print(result_2)


def sort_price_adv(list_in: list) -> list:
    year_sorted = sorted(list_in, reverse=True)
    list_out = year_sorted
    return list_out


result_3 = sort_price_adv(my_list)
print(result_3)


def check_five_max_elements(list_in: list) -> list:
    year_sorted = sorted(sorted(list_in, reverse=True)[:5:],reverse=False)
    list_out = year_sorted
    return list_out


result_4 = check_five_max_elements(my_list)
print(result_4)
