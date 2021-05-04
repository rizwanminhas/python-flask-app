from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_welcome_email

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://demo_user:demo_password@localhost:5432/demo_app'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        firstName = request.form['first_name']
        lastName = request.form['last_name']
        email = request.form['email']
        if firstName == '' or lastName == '' or email == '':
            return render_template('index.html', message='please enter all fields.')

        if db.session.query(User).filter(User.email == email).count() == 0:
            data = User(firstName, lastName, email)
            db.session.add(data)
            db.session.commit()
            send_welcome_email(email, firstName, lastName)
            return render_template('success.html')

        return render_template('index.html', message='User ' + email + ' already exists.')

if __name__ == '__main__':
    app.debug = True
    app.run()