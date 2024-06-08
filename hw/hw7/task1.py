def check_rhythm(stroka):
    # Определяем множество гласных букв
    vowels = set("аеёиоуыэюя")

    # Разделяем строку на фразы по пробелам
    phrases = stroka.split()

    # Если фраза только одна, выводим сообщение
    if len(phrases) <= 1:
        return "Количество фраз должно быть больше одной!"

    # Функция для подсчета гласных в слове
    def count_vowels(word):
        return sum(1 for char in word if char in vowels)

    # Подсчитываем количество гласных в каждой фразе
    syllable_counts = [sum(count_vowels(word) for word in phrase.split('-')) for phrase in phrases]

    # Проверяем, одинаково ли количество гласных во всех фразах
    if all(count == syllable_counts[0] for count in syllable_counts):
        return "Парам пам-пам"
    else:
        return "Пам парам"


# Пример использования
stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(check_rhythm(stroka))  # Должно вывести "Парам пам-пам"
