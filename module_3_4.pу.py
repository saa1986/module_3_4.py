# Пункты задачи:
# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
# При помощи цикла for переберите предполагаемо подходящие слова.
# Пропишите корректное относительно задачи условие, при котором добавляются слова в результирующий список same_words.
# После цикла верните образованный функцией список same_words.
# Вызовите функцию single_root_words и выведете на экран(консоль) возвращённое ей значение.

def single_root_words(root_word, *other_words):
    # Создаем пустой список для хранения подходящих слов
    same_words = []
    # Проходим по всем переданным словам
    for word in other_words:
        root_word_lower = root_word.lower()  # Приводим корневое слово к нижнему регистру
        # Проверяем, содержится ли корневое слово в текущем слове или наоборот
        if root_word.lower() in word.lower() or word.lower() in root_word.lower():
            same_words.append(word)  # Если да, добавляем это слово в список
    return same_words  # Возвращаем список подходящих слов

# Вызов функции и сохранение результатов
result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

# Выводим результаты
print(result1)  # Вывод: ['richiest', 'richies']
print(result2)  # Вывод: ['Disable', 'Mable']