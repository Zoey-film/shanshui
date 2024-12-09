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

@app.route('/favicon.ico')
def favicon():
    return redirect(url_for('static', filename='images/favicon.ico'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<season>')
def season_page(season):
    season_data = {
        'spring': {
            'title': 'Spring Poem',
            'content': """故园行
己亥年二月

竹暗烟村雨，花深古渡洲。
春风吹我面，缕缕是乡愁。


A Journey to My Old Home
Second Month of the Year of Jihai

Bamboo shadows veil the village in misty rain,
Flowers bloom deep on the ancient ferry plain.
Spring breezes caress my face so gently,
Each strand whispers of homesick melancholy.""",
            'bg_image': 'spring4.png'
        },
        'summer': {
            'title': 'Summer Poem',
            'content': """游团湖
戊戌年五月

云身荷影鉴湖光，莲叶翻风碧四方。
菡萏遥开三百里，千般仙子水中央。

A Tour of Tuan Lake
Fifth Month of the Year of Wuxu

Clouds and lotus shadows mirror the lake’s light,
Lotus leaves sway as winds spread green in all directions.
Buds bloom afar, stretching three hundred miles,
A thousand fairies grace the waters’ heart.""",
            'bg_image': 'summer1.png'
        },
        'fall': {
            'title': 'Fall Poem',
            'content': """夜过夔门
癸卯年九月

苍风白帝汉宫秋，万里长江此转头。
卧听潮声人半寐，一川幽梦月如钩。

Passing Kui Gate at Night
Ninth Month of the Year of Guimao

Autumn winds sweep White Emperor’s ancient halls,
The Yangtze turns here after countless miles.
Half-asleep, I lie and listen to the tide,
Dreams flow with the river, beneath a crescent moon.""",
            'bg_image': 'fall.png'
        },
        'winter': {
            'title': 'Winter Poem',
            'content': """定风波
岳阳楼
怀古戊戌年八月

千里霜涛越古楼，北山寒雁寄汀洲。碧水泓洄东去否？依旧。繁华洗替几曾休？
百世英雄龙虎斗，淘走。惟余一幕洞庭秋。但愿红尘人共久，牵手。临风谈笑泛兰舟。

Settling the Wind
At Yueyang Tower
Reflections on the Past, Eighth Month of the Year of Wuxu

Frosted waves stretch a thousand miles beyond the ancient tower,
Cold geese from the northern hills rest on the shoals below.
Does the emerald water still circle eastward in its flow?
Unchanging, Splendor rises and fades, ceaseless in its ebb and glow.
Heroes across centuries clashed like tigers and dragons,
Swept away, Only a scene of Lake Dongting in autumn stays.
May mortals linger long amidst this worldly haze,
Hand in hand, Laughing in the breeze aboard a fragrant orchid boat.""",
            'bg_image': 'winter2.png'
        }
    }
    
    return render_template('season_template.html',
                         season_name=season.capitalize(),
                         featured_poem=season_data[season],
                         bg_image=season_data[season]['bg_image'],
                         user_poems=get_user_poems(season))

if __name__ == '__main__':
    app.run(debug=True)
