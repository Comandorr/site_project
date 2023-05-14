from flask import Flask, redirect, url_for
import sqlite3
from random import randint
nomer = 0
quiz_nomer = 0

def index():
    global nomer, quiz_nomer
    quiz_nomer = randint(1, 3)
    nomer = 0
    conn = sqlite3.connect('victorines.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT name FROM quiz''')
    info = cursor.fetchall()
    cursor.close()
    conn.close()
    html = '''<h1>Сайт с викторинами</h1>'''
    for i in info:
        html += '<p>' + i[0] + '</p>'
    html += '<a href="/test">Начать викторину</a>'
    return html
    #return '''<h1>Сайт с викторинами</h1> <a href="/test">Начать викторину</a>'''

def test():
    global nomer, quiz_nomer
    command = '''
    SELECT question.text, question.answer1, question.answer2, question.answer3, question.answer4
    FROM question, links
    WHERE links.quiz_id == ? AND question.id == links.question_id'''
    conn = sqlite3.connect('victorines.db')
    cursor = conn.cursor()
    cursor.execute(command, [quiz_nomer])
    info = cursor.fetchall()
    cursor.close()
    conn.close()

    vopros = info[nomer]
    html = ''
    for v in vopros:
        html += '<p>'+v+'</p>'
    html += '''<p><a href="/test">Далее</a></p>'''

    nomer += 1
    if nomer == 3:
        return redirect(url_for('result'))
    else:
        return html

def result():
    return 'вы прошли викторину! <a href="/">Вернуться на главную</a>'

app = Flask(__name__)
app.add_url_rule('/', 'index', index)
app.add_url_rule('/test', 'test', test)
app.add_url_rule('/result', 'result', result)
app.run()