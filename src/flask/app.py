from flask import Flask, render_template
import src.hero_stats as hero_stats
app = Flask(__name__)

header_list = ['Home', 'Heroes', 'Synergy']
heroes_list = sorted(hero_stats.heroes_list)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', header_list=header_list)


@app.route('/heroes')
def heroes():
    return render_template('heroes.html', header_list=header_list, heroes_list=heroes_list)


@app.route('/synergy')
def synergy():
    return render_template('synergy.html', header_list=header_list)


if __name__ == '__main__':
    app.run(debug=True)
