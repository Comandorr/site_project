import sqlite3
# Подключение к файлу с базой данных
conn = sqlite3.connect('victorines.db')
cursor = conn.cursor()

# Очистка базы данных (если этот файл уже запускался раньше)
cursor.execute('''DROP TABLE IF EXISTS quiz''')
conn.commit()
cursor.execute('''DROP TABLE IF EXISTS question''')
conn.commit()
cursor.execute('''DROP TABLE IF EXISTS links''')
conn.commit()

# Создание таблицы для викторин
cursor.execute('''CREATE TABLE IF NOT EXISTS quiz (id INTEGER PRIMARY KEY, name TEXT)''')
conn.commit()

# Создание таблицы для вопросов
cursor.execute('''CREATE TABLE IF NOT EXISTS  question (
	id INTEGER PRIMARY KEY,
	text TEXT,
	answer1 TEXT,
	answer2 TEXT,
	answer3 TEXT,
	answer4 TEXT)''')
conn.commit()

# Создание таблицы для связей между викторинами и вопросами
# В одной викторине может быть сразу несколько вопросов
# Один вопрос может быть сразу в нескольких викторинах
cursor.execute('''PRAGMA foreign_keys = on''')
cursor.execute('''CREATE TABLE IF NOT EXISTS  links (
	id INTEGER PRIMARY KEY,
	quiz_id INTEGER,
	question_id INTEGER,
	FOREIGN KEY (quiz_id) REFERENCES quiz (id),
	FOREIGN KEY (question_id) REFERENCES question (id)
	)''')
conn.commit()

# Добавление новых викторин в базу данных
cursor.execute('''INSERT INTO quiz (name) VALUES ('Вопросы про команды Python')''')
conn.commit()

cursor.execute('''INSERT INTO quiz (name) VALUES ('Математические примеры')''')
conn.commit()

cursor.execute('''INSERT INTO quiz (name) VALUES ('Столицы стран')''')
conn.commit()

# Добавление новых вопросов в базу данных
cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Что делает команда print', 
		'печатает информацию', 'печатает pdf', 
		'печатает картинки', 'ничего')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Что делает команда input', 
		'позволяет ввести текст', 'позволяет ввести число', 
		'управляет героем игры', 'ничего')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Что делает команда break', 
		'останавливает цикл', 'паузу', 
		'закрывает программу', 'ничего')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('2+7=?', 
		'9', '8', '10', '11')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('16*2=?', 
		'32', '30', '34', '28')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('17-27', 
		'-10', '0', '-9', '-11')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Амстердам - это столица страны?', 
		'Нидерланды', 'Голландия', 'Дания', 'Исландия')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Загреб - это столица страны?', 
		'Хорватия', 'Македония', 'Сербия', 'Словакия')''')
conn.commit()

cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Улан-Батор - это столица страны?', 
		'Монголия', 'Казахстан', 'Туркменистан', 'Грузия')''')
conn.commit()

# Добавление вопросов в викторину
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (1, 1)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (1, 2)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (1, 3)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (2, 4)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (2, 5)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (2, 6)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (3, 7)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (3, 8)''')
conn.commit()
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (3, 9)''')
conn.commit()

# Вывод всей информации из таблицы (название таблицы указано после FROM)
cursor.execute('''SELECT * FROM question''')
info = cursor.fetchall()
print(info)

cursor.close()
conn.close()