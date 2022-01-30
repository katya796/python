def convert_list_in_str(list_in: list) -> str:
    index = 0
    m = []
    while index < len(list_in):
        num = list_in[index]
        if len(list_in[index]) == 2 and (list_in[index][:1:] == '+' or list_in[index][:1:] == '-') and ord(list_in[index][1:2:]) >= 49 and ord(list_in[index][1:2:]) <= 57:
            m.append(f'"{list_in[index][:1:]}0{list_in[index][1:2:]}"')
        elif len(list_in[index]) == 2 and ((ord(list_in[index][:1:]) >= 49 and ord(list_in[index][:1:]) <= 57) or (ord(list_in[index][1:2:]) >= 49 and ord(list_in[index][1:2:]) <= 57)):
            m.append(f'"{list_in[index]}"')
        elif len(list_in[index]) == 1 and ord(list_in[index]) >= 49 and ord(list_in[index]) <= 57:
            m.append(f'"0{list_in[index]}"')
        else:
            m.append(list_in[index])
        index = index + 1
    fin_str = ""
    for i in m:
        fin_str += str(i) + " "
    str_out = fin_str
    return str_out

my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
result = convert_list_in_str(my_list)
print(result)
