### final project ###

import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
import random


app = Flask(__name__)


if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database

# Flask-SQLAlchemy
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///herbev.db"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)

class Dictionary(db.Model):

    __tablename__ = "dictionary"
    herbew = db.Column(db.Text, primary_key=True)
    transcription = db.Column(db.Text)
    russian = db.Column(db.Text)
    root = db.Column(db.Text)
    theme = db.Column(db.Text)
    img = db.Column(db.Text)


    def __init__(self, herbew, transcription, russian, root, theme, img):
        self.herbew = herbew
        self.transcription = transcription
        self.russian = russian
        self.root = root
        self.theme = theme
        self.img = img

class Texts(db.Model):

    __tablename__ = "texts"
    herbew = db.Column(db.Text, primary_key=True)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    theme = db.Column(db.Text)
    img = db.Column(db.Text)


    def __init__(self, herbew, title, text, theme, img):
        self.herbew = herbew
        self.title = title
        self.text = text
        self.theme = theme
        self.img = img

@app.route("/")

def index():
    return render_template("index.html")

@app.route("/map")
def map():
    return render_template("map.html")
    
    
@app.route("/study", methods=["GET", "POST"])
def study():
    
    theme="room"
    title = 'Моя комната'
    study_title = 'Переведите слово:'
    link = 'room/'
    dictionary = Dictionary.query.filter(Dictionary.theme == theme)
    items = list(dictionary)
    random.shuffle(items)
    question=items[0:4]
    answer=question[0:1]
    random.shuffle(question)
    print(answer[0].transcription)
    if request.method == "POST":
        ans=request.form.get("training")
        print(ans)
        print(answer[0].transcription)
        if answer[0].transcription == ans:
            return render_template("apology.html", apologies="Правильно!")
    return render_template("study.html", answer=answer, question=question, link=link, title = title, study_title=study_title)
    
    
@app.route("/dictionary", methods=["GET", "POST"])
def dictionary():
    # query database for username
    if request.method == "POST":
       
        lang=request.form.get("Lang_search")
    
        if lang == 'herbew':
            search = Dictionary.query.filter(Dictionary.herbew==request.form.get("word"))
        if lang == 'transcription':
           search = Dictionary.query.filter(Dictionary.transcription==request.form.get("word"))
        if lang == 'russian':
            search = Dictionary.query.filter(Dictionary.russian==request.form.get("word"))
        return render_template("search.html", search = search)    

    dictionary=Dictionary.query.order_by(Dictionary.herbew)
    return render_template("dictionary.html", dictionary = dictionary)



@app.route("/grammar")
def grammar():
    return render_template("grammar.html")
    
@app.route("/phrasebook")
def phrasebook():
    return render_template("phrasebook.html")

@app.route("/lesson1")
def lesson1():
    theme = "lesson1"
    items = Texts.query.filter(Texts.theme == theme)
    #random.shuffle(items)
    return render_template("lesson1.html", items=items)

@app.route("/lesson2")
def lesson2():
    theme = "numbers"
    numbers = Dictionary.query.filter(Dictionary.theme == theme)
    #numbers = db.execute("SELECT * FROM dictionary WHERE theme = :theme", theme = theme)
    return render_template("lesson2.html", numbers=numbers)

@app.route("/lesson3")
def lesson3():
    theme = "school"
    title = 'В школе'
    link = 'school/'
    dictionary = Dictionary.query.filter(Dictionary.theme == theme)
    items = list(dictionary)
    random.shuffle(items)
    return render_template("cards.html", items=items, title = title, link = link, theme = theme)

@app.route("/lesson4")
def lesson4():
    theme = "room"
    title = 'Моя комната'
    link = 'room/'
    dictionary = Dictionary.query.filter(Dictionary.theme == theme)
    items = list(dictionary)
    random.shuffle(items)
    return render_template("cards.html", items=items, title = title, link = link, theme = theme)

@app.route("/lesson5")
def lesson5():
    return render_template("lesson5.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            text = "Вы не ввели логин";
            return render_template("apology.html", apologies = text)

        # ensure password was submitted
        elif not request.form.get("password"):
            text = "Вы не ввели пароль";
            return render_template("apology.html", apologies = text)

        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
 
        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            
            text = "Неправильный логин и/или пароль";
            return render_template("apology.html", apologies = text)

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]
        
        #print (old_pass_hash);
        print(rows[0]["hash"]);
        
        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user."""
     # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            text = "Вы не ввели логин";
            return render_template("apology.html", apologies = text)
        
        # query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
 
        # ensure username exists
        if len(rows) == 1 :
            text = "Такой логин уже существует";
            return render_template("apology.html", apologies = text)

        # ensure password was submitted
        elif not request.form.get("password"):
            text = "Вы не ввели пароль";
            return render_template("apology.html", apologies = text)
            
        # ensure password was submitted
        elif not request.form.get("password2"):
            text = "Вы не ввели контрольный пароль";
            return render_template("apology.html", apologies = text)
        
        # ensure password was submitted
        elif not request.form.get("password") == request.form.get("password2"):
            text = "Пароли не совпадают";
            return render_template("apology.html", apologies = text)
        
        pass_hash = pwd_context.encrypt(request.form["password"])
        #print (pass_hash)
        # query database for username
        db.execute("INSERT INTO users (username, hash) VALUES(:username, :password)", username=request.form["username"], password=pass_hash)
        
        rows_reg = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
        
        flash('Вы зарегистрировались!')
        # remember which user has logged in
        session["user_id"] = rows_reg[0]["id"]
        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/profile", methods=["GET", "POST"])
def profile():
    """Log user out."""
    if request.method == "POST":
    
            
            ### PASSWORD ###
            
            # ensure username was submitted
            if not request.form.get("old_password"):
                text = "Вы не ввели старый пароль";
                return render_template("apology.html", apologies = text)
            
           
            # remember which user has logged in
            user_id = session["user_id"]
        
            # query database for username
            rows = db.execute("SELECT * FROM users WHERE id = :uid", uid = user_id)
            
            # ensure username exists
            if not pwd_context.verify(request.form.get("old_password"), rows[0]["hash"]):
                text = "Неправильный пароль";
                return render_template("apology.html", apologies = text)
    
            # ensure password was submitted
            elif not request.form.get("new_password"):
                text = "Вы не ввели новый пароль";
                return render_template("apology.html", apologies = text)
                
            # ensure password was submitted
            elif not request.form.get("new_password2"):
                text = "Вы не ввели контрольный новый пароль";
                return render_template("apology.html", apologies = text)
            
            # ensure password was submitted
            elif not request.form.get("new_password") == request.form.get("new_password2"):
                text = "Пароли не совпадают";
                return render_template("apology.html", apologies = text)
            
            new_pass_hash = pwd_context.encrypt(request.form["new_password"])
           
            db.execute("UPDATE users SET hash = :new_pass_hash WHERE id = :uid", new_pass_hash = new_pass_hash, uid = user_id)
            
           
            
            flash('Вы сменили пароль!')
           
            return redirect(url_for("index"))
    else:
        return render_template("profile.html")