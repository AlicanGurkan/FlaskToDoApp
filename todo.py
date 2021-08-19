from re import U
from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Alican/OneDrive/Alican GÜRKAN/Programlama çalışmaları/Phyton/Kodlama egzersizleri/Flask TODO/TODO app/todo.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    complete = db.Column(db.Boolean)
    
    
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add", methods = ["POST"])
def addtodo():
    title = request.form.get("title")
    newtodo = Todo(title = title, complete = False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for("index"))
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

