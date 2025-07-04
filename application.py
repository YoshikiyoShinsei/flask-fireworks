from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)

@app.route('/fireworks')
def fireworks():
    return render_template('fireworks.html')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)