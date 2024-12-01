from flask import Flask, render_template

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
                         user_poems=user_poems_data[season])

if __name__ == '__main__':
    app.run(debug=True)
