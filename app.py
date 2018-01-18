from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/tc2843', methods=['GET'])
def main():
    return render_template('profile.html')


if __name__ == '__main__':
    app.run()
