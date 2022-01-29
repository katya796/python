def convert_time(duration: int) -> str:
    if duration >0 and duration < 60:
        print(str(duration) + " сек")
    if duration >= 60 and duration < 3600:
        print(str(duration // 60) + " мин " + str(duration % 60) + " сек")
    if duration >= 3600 and duration < 86400:
        print(str(duration // 3600) + " час " + str(duration % 3600 // 60) + " мин " + str(duration % 3600 % 60) + " сек")
    if duration >= 86400:
        print(str(duration // 86400) + " дн " + str(duration % 86400 // 3600) + " час " + str(duration % 86400 % 3600 // 60) + " мин " + str(duration % 86400 % 3600 % 60) + " сек")

duration = 400153
result = convert_time(duration)
print(result)