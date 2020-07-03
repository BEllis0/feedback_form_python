from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ============
# DB CONNECTION
# ============

ENV = 'dev'

# dev environment
if ENV == 'dev':
    app.debug = True
    # DB CONNECTION - local
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Skiclub0@localhost/experience_rating_emails'
# production environment
else: 
    app.debug = False
    # DB CONNECTION - Heroku
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# db object for querying
db = SQLAlchemy(app)

# ============
# DB Models
# ============


# ============
# routes
# ============

# index page
@app.route('/')
def index():
    return render_template('index.html')

# form submission
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # target form data
        customer_first_name = request.form['customer_first_name']
        customer_last_name = request.form['customer_last_name']
        customer_email = request.form['customer_email']
        experience_rating = request.form['experience_rating']
        customer_comments = request.form['comments']

        print(customer_first_name, customer_last_name, customer_email, experience_rating, customer_comments)

        # handle user missing fields
        if customer_first_name == '' or customer_last_name == '':
            return render_template('index.html', message='Please enter required fields')

        # serve success page
        return render_template('success.html')


# ============
# initiated server
# ============
if __name__ == '__main__':
    app.run()

