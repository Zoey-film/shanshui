from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Sample user poems data
user_poems_data = {
    'spring': [
        {'content': """Cherry blossoms dance\nIn the gentle spring breeze now\nPink petals take flight""", 'user': 'Emily Chen'},
        {'content': """Morning dew glistens\nAs new leaves unfurl their wings\nNature awakens""", 'user': 'Michael Smith'},
        {'content': """Spring rain softly falls\nWashing winter's memories\nNew beginnings bloom""", 'user': 'Sarah Johnson'}
    ],
    'summer': [
        {'content': """Cherry blossoms dance\nIn the gentle spring breeze now\nPink petals take flight""", 'user': 'Emily Chen'},
        {'content': """Morning dew glistens\nAs new leaves unfurl their wings\nNature awakens""", 'user': 'Michael Smith'},
        {'content': """Spring rain softly falls\nWashing winter's memories\nNew beginnings bloom""", 'user': 'Sarah Johnson'}
    ],
    'fall': [
        {'content': """Cherry blossoms dance\nIn the gentle spring breeze now\nPink petals take flight""", 'user': 'Emily Chen'},
        {'content': """Morning dew glistens\nAs new leaves unfurl their wings\nNature awakens""", 'user': 'Michael Smith'},
        {'content': """Spring rain softly falls\nWashing winter's memories\nNew beginnings bloom""", 'user': 'Sarah Johnson'}
    ],
    'winter': [
        {'content': """Cherry blossoms dance\nIn the gentle spring breeze now\nPink petals take flight""", 'user': 'Emily Chen'},
        {'content': """Morning dew glistens\nAs new leaves unfurl their wings\nNature awakens""", 'user': 'Michael Smith'},
        {'content': """Spring rain softly falls\nWashing winter's memories\nNew beginnings bloom""", 'user': 'Sarah Johnson'}
    ],
}

# Database setup
def init_db():
    conn = sqlite3.connect('poems.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS poems
                 (content TEXT NOT NULL,
                  author TEXT NOT NULL,
                  seed_page TEXT NOT NULL,
                  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()

# Initialize the database when the app starts
init_db()

def get_user_poems(season):
    conn = sqlite3.connect('poems.db')
    c = conn.cursor()
    c.execute('SELECT content, author FROM poems WHERE seed_page = ? ORDER BY created_at DESC', (season,))
    poems = [{'content': row[0], 'user': row[1]} for row in c.fetchall()]
    conn.close()
    return poems

@app.route('/submit_poem', methods=['POST'])
def submit_poem():
    content = request.form.get('content')
    author = request.form.get('author')
    seed_page = request.form.get('seed_page')
    
    if content and author and seed_page:
        conn = sqlite3.connect('poems.db')
        c = conn.cursor()
        c.execute('INSERT INTO poems (content, author, seed_page) VALUES (?, ?, ?)',
                 (content, author, seed_page))
        conn.commit()
        conn.close()
    
    return redirect(url_for('season_page', season=seed_page))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<season>')
def season_page(season):
    season_data = {
        'spring': {
            'title': 'Spring Poem',
            'content': 'Spring poem content...',
            'bg_image': 'spring.jpg'
        },
        'summer': {
            'title': 'Summer Poem',
            'content': 'Summer poem content...',
            'bg_image': 'summer.png'
        },
        'fall': {
            'title': 'Fall Poem',
            'content': 'Fall poem content...',
            'bg_image': 'fall.png'
        },
        'winter': {
            'title': 'Winter Poem',
            'content': 'Winter poem content...',
            'bg_image': 'winter.png'
        }
    }
    
    return render_template('season_template.html',
                         season_name=season.capitalize(),
                         featured_poem=season_data[season],
                         bg_image=season_data[season]['bg_image'],
                         user_poems=get_user_poems(season))

if __name__ == '__main__':
    app.run(debug=True)
