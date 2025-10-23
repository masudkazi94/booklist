from flask import Flask, render_template, request, redirect, url_for
from models import db, Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        desc = request.form['desc']
        year = request.form['year']
        read = 'read' in request.form

        new_book = Book(title=title, author=author, desc=desc, year=year, read=read)
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('index'))
    return render_template('add_book.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_book(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.desc = request.form['desc']
        book.year = request.form['year']
        book.read = 'read' in request.form

        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_book.html', book=book)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_book(id):
    book = Book.query.get_or_404(id)

    if request.method == 'POST':
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))
    
@app.route('/toggle/<int:id>')
def toggle(id):
    book = Book.query.get_or_404(id)
    book.read = not book.read
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
