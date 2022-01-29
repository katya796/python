def sum_list_1(dataset: list) -> int:
    index = 0
    finish_list = []
    while index <= len(dataset):
        start = 0
        num = dataset[index]
        while num != 0:
            start = start + num % 10
            num = num // 10
        if start % 9 == 0:
            finish_list.append(dataset[index])
        index = index + 1
    return finish_list

def sum_list_2(dataset: list) -> int:
    #К каждому элементу списка добавляет 17 и вычисляет сумму чисел списка,
      #  сумма цифр которых делится нацело на 7
    # место для написания кода
    return 1  # Верните значение полученной суммы


my_list = [i ** 3 for i in range(1,1001,2)]
result_1 = sum_list_1(my_list)
print(result_1)
"""result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)"""
