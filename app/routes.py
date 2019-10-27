from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Albert'}
    posts = [
            {
                'author': {'username': 'John'},
                'body': 'Nice day out there'
            },
            {
                'author': {'username': 'Mike'},
                'body': 'You know it'
            }
            ]

    return render_template('index.html', title='Home', user=user, posts=posts)
