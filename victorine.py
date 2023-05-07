import sqlite3
from random import shuffle
# Подключение к файлу с базой данных
conn = sqlite3.connect('victorines.db')
cursor = conn.cursor()

cursor.execute('''SELECT name FROM quiz''')
info = cursor.fetchall()
for i in range(len(info)):
    print(i+1, '-', info[i][0])


quiz_nomer = int(input('\nВыберите номер викторины (от 1 до 3)\n'))

command = '''
SELECT question.text, question.answer1, question.answer2, question.answer3, question.answer4
FROM question, links
WHERE links.quiz_id == ? AND question.id == links.question_id'''

cursor.execute(command, [quiz_nomer])
info = cursor.fetchall()

right = 0
wrong = 0

for i in info:
    print('\n')
    print(i[0])
    answers = [i[1], i[2], i[3], i[4]]
    shuffle(answers)
    print('-', answers[0])
    print('-', answers[1])
    print('-', answers[2])
    print('-', answers[3])

    ask = input('\nКакой ответ правильный?\n')
    if ask == i[1]:
        print('ПРАВИЛЬНО!')
        right += 1
    else:
        print('ОШИБКА!')
        wrong += 1

print('\nВы прошли викторину и набрали', right,
      'правильных ответов и', wrong, 'ошибок!')

cursor.close()
conn.close()
