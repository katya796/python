def num_translate(value: str) -> str:
    transl_numb = {
        "zero": "ноль",
        "one": "один",
        "two": "два",
        "three": "три",
        "four": "четыре",
        "five": "пять",
        "six": "шесть",
        "seven": "семь",
        "eight": "восемь",
        "nine": "девять",
        "ten": "десять",
    }
    str_out = transl_numb.get(value, 'None')
    return str_out


print(num_translate("one"))
print(num_translate("eight"))
