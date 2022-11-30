from flask import Flask,request,render_template,redirect
from flask_sqlalchemy import SQLAlchemy
from config import app

db = SQLAlchemy(app)


#...

class User_details(db.Model):
    """An admin user capable of viewing reports.
    :param str email: email address of user
    :param str password: encrypted password for the user
    """
    __tablename__ = 'user_details'
    email = db.Column(db.String, primary_key=True)
    password = db.Column(db.String)
    
    def __init__(self,email,password):
        self.email=email
        self.password=password
       


    
@app.route('/adduser', methods = ['GET','POST']) 
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = User_details(email = email, password= password)
        db.session.add(user)
        db.session.commit()
        return redirect('/user')

    return render_template("adduser.html")

@app.route('/user') 
def home():
    return "User Added Successfully"


#to run the app in debug mode
if __name__ == "__main__":
    #db.create_all()
    app.run(port= 8000, debug = True)
