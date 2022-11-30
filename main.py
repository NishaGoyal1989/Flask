from flask import render_template,redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from config import app

db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__ = "todo"
    sno= db.Column(db.Integer, primary_key = True)
    title=db.Column(db.String(200), nullable = False)
    desc=db.Column(db.String(500) ,nullable = False)
    date_created=db.Column(db.DateTime, default= datetime.now())

    def __init__(self,title,desc,date_created):
        self.title=title
        self.desc=desc
        self.date_created=date_created

#different route for different endpoints
@app.route('/', methods = ['GET','POST']) 
def index():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        date_created = datetime.now()
        todo = Todo(title = title, desc= desc,date_created=date_created)
        db.session.add(todo)
        db.session.commit()
    allTodo= Todo.query.all()
    #return "Congratulations , It's a web app!!"
    return render_template("index.html",allTodo=allTodo)
     


@app.route("/products")
def products():
    return "This is product page!"


@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

db.create_all()
@app.route('/update/<int:sno>', methods=['GET','POST'])
def update(sno):
    if request.method =='POST':
        title = request.form['title']
        desc = request.form['desc'] 
        todo=Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect('/')

    todo=Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo=todo)
        

#to run the app in debug mode
if __name__ == "__main__":
    app.run(port=7000,debug = True)

