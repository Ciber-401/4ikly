# # Задача 4:
# # Напишите проверку на то, является ли строка палиндромом.
# # Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.

# # Пример:
#         # тот -> тот
#         # потоп -> потоп
#         # көк -> көк


# # СЛОВА ДЛЯ ПРОВЕРКИ:
words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще']
for i in words:
    if i.lower() == i[:: -1].lower():
        print(i,'это слово полиндром')
    else:
        print(i,'это слово не палиндром')