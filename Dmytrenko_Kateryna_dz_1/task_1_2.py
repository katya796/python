def sum_list_1(dataset: list) -> int:
    index = 0
    finish_list = 0
    while index < len(dataset):
        start = 0
        num = dataset[index]
        while num != 0:
            start = start + num % 10
            num = num // 10
        if start % 7 == 0:
            finish_list = finish_list + dataset[index]
        index = index + 1
    return finish_list

def sum_list_2(dataset: list) -> int:
    dataset_new = [i+17 for i in dataset]
    index = 0
    finish_list = 0
    while index < len(dataset_new):
        start = 0
        num = dataset_new[index]
        while num != 0:
            start = start + num % 10
            num = num // 10
        if start % 7 == 0:
            finish_list = finish_list + dataset_new[index]
        index = index + 1
    return finish_list


my_list = [i ** 3 for i in range(1,1001,2)]
result_1 = sum_list_1(my_list)
print(result_1)
result_2 = sum_list_2(my_list)
print(result_2)
