# app.py
from flask import Flask, render_template, request, redirect, jsonify
from sqlalchemy.exc import SQLAlchemyError
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from models import db, Song, Performance, Show
import itertools
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///setlist.db'
app.config['SECRET_KEY'] = 'password'
db.init_app(app)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # Return the Show object associated with the user_id
    return Show.query.get(int(user_id))

with app.app_context():
    db.create_all()

@app.route('/home', methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:
        return redirect('/')
    
    show_id = current_user.id
    show_name = Show.query.get(int(show_id)).name

    if request.method == 'POST':
        if 'generate_setlists' in request.form:
            songs = get_songs(show_id)
            performances = get_performances(show_id)
            
            start_song = request.form.get('start_song')
            end_song = request.form.get('end_song')

            optimal_setlists = generate_setlists(songs, performances, start_song, end_song)
            return render_template('result.html', setlists=optimal_setlists)
        
        elif 'add_song' in request.form:
            song_title = request.form.get('song')
            dancers = request.form.get('dancers').split(',')

            if song_title and all(dancer.strip() for dancer in dancers):
                existing_song = Song.query.filter_by(show_id=show_id, title=song_title).first()
                if existing_song:
                    error_message = f'A song with the title "{song_title}" already exists.'
                    return render_template('index.html', songs=get_songs(show_id), performances=get_performances(show_id), error=error_message, show=show_name)

                song = Song(title=song_title, show_id=show_id)
                db.session.add(song)
                db.session.flush()

                for dancer in dancers:
                    performance = Performance(song_title=song_title, dancer=dancer.strip())
                    db.session.add(performance)

                db.session.commit()
                return redirect('/home')  # Redirect to home

    return render_template('index.html', songs=get_songs(show_id), performances=get_performances(show_id), show=show_name)



@app.route('/delete-song/<song_title>', methods=['POST'])
@login_required
def delete_song(song_title):
    show_id = current_user.id
    song = Song.query.filter_by(title=song_title, show_id=show_id).first()

    if song:
        try:
            # Delete performances associated with the song
            performances = Performance.query.filter_by(song_title=song.title).all()
            for performance in performances:
                db.session.delete(performance)

            # Delete the song
            db.session.delete(song)
            db.session.commit()
            return redirect(f'/home')
        except SQLAlchemyError as e:
            db.session.rollback()
            return redirect(f'/home')
    else:
        error_message = 'Song not found'
        return redirect(f'/home')

def generate_setlists(songs, performances, start_song=None, end_song=None):
    performance_map = {song.title: set([perf.dancer for perf in song.performances]) for song in songs}
    setlists = []

    def evaluate_setlist(setlist):
        consecutive_count = 0
        consecutive_dancers = []
        for i in range(len(setlist) - 1):
            set_1 = performance_map[setlist[i]]
            set_2 = performance_map[setlist[i + 1]]
            common_dancers = set_1 & set_2
            if common_dancers:
                consecutive_count += 1
                consecutive_dancers.append((common_dancers, setlist[i], setlist[i + 1]))
        return consecutive_count, consecutive_dancers

    for start_index in range(len(songs)):  # Iterate over each song as the initial song
        setlist = []
        available_songs = list(performance_map.keys())

        # Rotate to start with different initial song
        available_songs = available_songs[start_index:] + available_songs[:start_index]

        if start_song:
            setlist.append(start_song)
            available_songs.remove(start_song)
        
        if end_song:
            available_songs.remove(end_song)

        while available_songs:
            if setlist:
                previous_dancers = performance_map[setlist[-1]]
            else:
                previous_dancers = set()

            best_song = None
            best_score = float('inf')

            for song in available_songs:
                current_dancers = performance_map[song]
                common_dancers = previous_dancers & current_dancers
                score = len(common_dancers)
                if score < best_score:
                    best_song = song
                    best_score = score

            setlist.append(best_song)
            available_songs.remove(best_song)

        if end_song:
            setlist.append(end_song)

        setlists.append((setlist, *evaluate_setlist(setlist)))

    setlists.sort(key=lambda x: x[1])

    return setlists

def get_songs(show_id):
    songs = Song.query.filter_by(show_id=show_id).all()
    return songs


def get_performances(show_id):
    performances = {}
    songs = get_songs(show_id)

    for song in songs:
        performances[song.title] = [performance.dancer for performance in song.performances]

    return performances


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the show exists
        show = Show.query.filter_by(name=name).first()

        if show and check_password_hash(show.password, password):
            # Login the show
            login_user(show, remember=True)
            return redirect('/home')

        # Invalid show name or password
        error_message = 'Invalid show name or password'
        return render_template('login.html', error=error_message)

    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    # Logout the current show
    logout_user()
    return redirect('/login')

@app.route('/', methods=['GET', 'POST'])
def create_show():
    if current_user.is_authenticated:
        return redirect('/home')

    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')

        # Check if the show name is already taken
        existing_show = Show.query.filter_by(name=name).first()
        if existing_show:
            error_message = 'Show name already taken'
            return render_template('create_show.html', error=error_message)

        # Create a new show
        new_show = Show(name=name, password=generate_password_hash(password))
        db.session.add(new_show)
        db.session.commit()

        # Login the new show
        login_user(new_show)

        return redirect('/home')

    return render_template('create_show.html')


if __name__ == '__main__':
    app.run(debug=True)