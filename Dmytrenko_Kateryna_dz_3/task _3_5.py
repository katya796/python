from random import choice
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    list_out = [
        choice(nouns) + ' ' + choice(adverbs) + ' ' + choice(adjectives)
        for i in range(count)
        if len(nouns) and len(adverbs) and len(adjectives)
    ]
    return list_out


print(get_jokes(2))
print(get_jokes(10))