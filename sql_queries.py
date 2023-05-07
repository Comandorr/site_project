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

# Добавление новой викторины в базу данных
cursor.execute('''INSERT INTO quiz (name) VALUES ('Первая викторина')''')
conn.commit()

# Добавление нового вопроса в базу данных
cursor.execute('''INSERT INTO question (text, answer1, answer2, answer3, answer4)
	VALUES('Что делает команда print', 
		'печатает информацию', 
		'печатает pdf', 
		'печатает картинки', 
		'ничего')
	''')
conn.commit()

# Добавление вопроса в викторину
cursor.execute('''INSERT INTO links (quiz_id, question_id) VALUES (1, 1)''')
conn.commit()

# Вывод всей информации из таблицы (название таблицы указано после FROM)
cursor.execute('''SELECT * FROM question''')
info = cursor.fetchall()
print(info)

cursor.close()
conn.close()