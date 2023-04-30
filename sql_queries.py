import sqlite3
conn = sqlite3.connect('victorines.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS quiz (
	id INTEGER PRIMARY KEY, 
	name TEXT
	)''')
conn.commit()

cursor.execute('''CREATE TABLE IF NOT EXISTS  question (
	id INTEGER PRIMARY KEY,
	text TEXT,
	answer1 TEXT,
	answer2 TEXT,
	answer3 TEXT,
	answer4 TEXT
	)''')
conn.commit()

cursor.execute('''PRAGMA foreign_keys = on''')
cursor.execute('''CREATE TABLE IF NOT EXISTS  links (
	id INTEGER PRIMARY KEY,
	quiz_id INTEGER,
	question_id INTEGER,
	FOREIGN KEY (quiz_id) REFERENCES quiz (id),
	FOREIGN KEY (question_id) REFERENCES question (id)
	)''')
conn.commit()

cursor.close()
conn.close()