from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#app is an instance of Flask, taking in the __name__ of the script file. 
#This lets Python know how to import from files relative to this one.
app = Flask(__name__)
# 4 forward slashes is an absolute path - complete path
# 3 forward slashes is a relative path - we need to specify exact location - it just resides in the project location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    #__tablename__ = 'example'
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    #overriding default implementation of __repr__() method
    def __repr__(self):
        return '<Task %r>' %self.id

#@app.route('/') -by default only GET works
@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form["content"]
        new_task = Todo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return "There was an issue adding your task"

    else:
        task_list = Todo.query.order_by(Todo.date_created).all()
        return render_template("index.html", tasks = task_list)

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "There was a problem deleting that task"

@app.route('/update/<int:id>', methods = ['GET', 'POST'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)

    if request.method == "POST":
        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return "There was a problem updating that task"
    
    else:
        return render_template("update.html", task = task_to_update)

if __name__ == "__main__":
    app.run(debug=True)