from flask import Flask, request, redirect, url_for, render_template
from model import db, Result
from utils import add_results_to_csvfile

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdb.sqlite3'
db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form.get('email')
        if not email:
            return render_template('index.html', error="Пожалуйста, введите email")
        return redirect(url_for('survey', email=email))
    return render_template('index.html')



@app.route('/survey', methods=['GET', 'POST'])
def survey():
    email = request.args.get('email')

    if request.method == 'POST':
        favorite_time = request.form.get('favorite_time')
        favorite_season = request.form.get('favorite_season')
        favorite_actor = request.form.get('favorite_actor')
        favorite_genres = request.form.getlist('favorite_genres')
        favorite_genres_str = ', '.join(favorite_genres)

        new_result = Result(
            email = email,
            favorite_time=  favorite_time,
            favorite_season=  favorite_season,
            favorite_actor=favorite_actor,
            favorite_genres= favorite_genres_str
        )


        db.session.add(new_result)
        db.session.commit()
        add_results_to_csvfile()

        return render_template('thankyou.html')


    return render_template('survey.html', email=email)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        add_results_to_csvfile()
    app.run(debug=True)