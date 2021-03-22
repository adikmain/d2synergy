from flask import Flask, render_template

app = Flask(__name__)

header_list = ['Home', 'Heroes', 'Synergy']


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', header_list=header_list)


@app.route('/heroes')
def heroes():
    return render_template('heroes.html', header_list=header_list)


@app.route('/synergy')
def synergy():
    return render_template('synergy.html', header_list=header_list)


if __name__ == '__main__':
    app.run(debug=True)
