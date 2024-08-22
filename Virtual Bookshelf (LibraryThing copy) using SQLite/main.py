#Virtual Bookshelf

from flask import Flask,render_template,redirect,request
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from sqlalchemy import String,INTEGER,FLOAT
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)
app.secret_key = "hi-lol"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"

#Making a database
class Base(DeclarativeBase):
    pass

#Creating a database
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#Creating a table
class Book(db.Model):
    id:Mapped[int] = mapped_column(INTEGER,primary_key=True)
    title: Mapped[str] = mapped_column(String(250),nullable=True,unique=True)
    author: Mapped[str] = mapped_column(String(250),nullable=True)
    rating: Mapped[float] = mapped_column(FLOAT,nullable=True)

#This will create table schema in the database
with app.app_context():
    db.create_all()


#This function will return a tuple with the number of books on the first index and all the books in a list, where each book is a dictionary
def count_books()->tuple:
    count = 0
    books = []
    with app.app_context():
        rows = db.session.execute(db.select(Book).order_by(Book.id)).scalars()
        for row in rows:
            count += 1
            dictionary = {"id":row.id,"title":row.title,"author":row.author,"rating":row.rating}
            books.append(dictionary)
    return count,books


#This function will assign the right id number
def new_id()->int:
    ids = []
    with app.app_context():
        rows = db.session.execute(db.select(Book)).scalars()
        for row in rows:
            ids.append(row.id)
    if len(ids) == 0:
        return 1
    else:
        for i in range(1,max(ids)):
            if i not in ids:
                return i


#Flask form for the website(The page where you add a book)
class BookForm(FlaskForm):
    title = StringField(label="Title of the book:",validators=[DataRequired()])
    author = StringField(label="Author of the book:",validators=[DataRequired()])
    rating = StringField(label="Rating of the book out of the 10",validators=[DataRequired()])
    submit = SubmitField(label="Add Book")

#Flask form for the website(The page where you change the rating of a book)
class RatingForm(FlaskForm):
    rating = StringField(label="The new rating of the book out of 10:",validators=[DataRequired()])
    submit = SubmitField(label="Change Rating")

#This is the home page
@app.route("/")
def home():
    count,books = count_books()
    form = BookForm()
    return render_template("index.html",count=count,books=books)

#This will add a new book to database which will appear on the website
@app.route("/add",methods=["GET","POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        rating = float(form.rating.data)
        if rating > 10:
            rating = 10
        elif rating < 0:
            rating = 0
        id = new_id()
        with app.app_context():
            new_book = Book(id=id,title=title,author=author,rating=rating)
            db.session.add(new_book)
            db.session.commit()
        return redirect("/")
    return render_template("add.html",form=form)


#This will edit the rating of a book
@app.route("/edit/<int:id>",methods=["GET","POST"])
def edit(id:int):
    form = RatingForm()
    if form.validate_on_submit():
        with app.app_context():
            new_rating = float(form.rating.data)
            if new_rating > 10:
                new_rating = 10
            elif new_rating <0:
                new_rating = 0
            row = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
            row.rating = new_rating
            db.session.commit()
        return redirect('/')
    return render_template("edit.html",form=form,id=id)


#This will delete a book
@app.route("/delete/<int:id>",methods=["GET","POST"])
def delete(id:int):
    row = db.session.execute(db.select(Book).where(Book.id == id)).scalar()
    db.session.delete(row)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run()