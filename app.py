from flask import Flask, render_template, request

app = Flask(__name__)

# routes

# index page
@app.route('/')
def index():
    return render_template('index.html')

# initiated server
if __name__ == '__main__':
    app.debug = True
    app.run()

