#!/usr/bin/env python3
from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

# Хранилище напоминаний (в памяти)
reminders = []

# HTML шаблон прямо в коде (для простоты)
HOME_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Catty Reminders</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto; padding: 20px; }
        .reminder { background: #f5f5f5; padding: 10px; margin: 10px 0; border-radius: 5px; }
        .cat { color: #ff6b6b; font-size: 1.2em; }
        input[type=text] { width: 70%; padding: 8px; }
        button { padding: 8px 15px; background: #4ecdc4; border: none; color: white; cursor: pointer; }
    </style>
</head>
<body>
    <h1>🐱 Catty Reminders <span class="cat">🐱</span></h1>
    
    <form method="POST" action="/add">
        <input type="text" name="reminder" placeholder="Например: покормить кота" required>
        <button type="submit">Добавить</button>
    </form>
    
    <h2>Твои напоминания:</h2>
    {% if reminders %}
        {% for r in reminders %}
            <div class="reminder">
                {{ r }}
                <a href="/delete/{{ loop.index0 }}" style="color: red; float: right;">[x]</a>
            </div>
        {% endfor %}
    {% else %}
        <p>Пока нет напоминаний. Создай первое!</p>
    {% endif %}
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HOME_PAGE, reminders=reminders)

@app.route('/add', methods=['POST'])
def add():
    reminder = request.form.get('reminder')
    if reminder:
        reminders.append(reminder)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(reminders):
        reminders.pop(index)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
