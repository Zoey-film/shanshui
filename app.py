from flask import Flask, render_template

app = Flask(__name__)

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
                         user_poems=[])

if __name__ == '__main__':
    app.run(debug=True)
