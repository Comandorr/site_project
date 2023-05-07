import sqlite3
from random import shuffle
# Подключение к файлу с базой данных
conn = sqlite3.connect('victorines.db')
cursor = conn.cursor()

quiz_nomer = int(input('Выберите номер викторины (от 1 до 3)'))

command = '''
SELECT question.text, question.answer1, question.answer2, question.answer3, question.answer4
FROM question, links
WHERE links.quiz_id == ? AND question.id == links.question_id'''

cursor.execute(command, [quiz_nomer])
info = cursor.fetchall()

for i in info:
    print(i[0])
    answers = [i[1], i[2], i[3], i[4]]
    shuffle(answers)
    print('-', answers[0])
    print('-', answers[1])
    print('-', answers[2])
    print('-', answers[3])
    print('\n')

cursor.close()
conn.close()
