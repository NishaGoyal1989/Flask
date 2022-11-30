from flask import Flask
# to intialise the app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://nishagarg7:@localhost/sample_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False