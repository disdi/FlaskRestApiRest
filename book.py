from flask import Flask, request, jsonify
from models import db, Book
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'book.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
db.create_all()

ma = Marshmallow(app)

class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'price')

book_schema = BookSchema()
books_schema = BookSchema(many=True)

# endpoint to show all books
@app.route("/api/book", methods=["GET"])
def getbook():
    all_books = Book.query.all()
    result = books_schema.dump(all_books)
    return jsonify(result.data)


# endpoint to get book detail by id
@app.route("/api/book/<id>", methods=["GET"])
def book_detail(id):
    book = Book.query.get(id)
    return book_schema.jsonify(book)

# endpoint to create new book
@app.route("/api/book", methods=["POST"])
def add_book():
    title = request.json['title']
    price = request.json['price']

    new_book = Book(title, price)

    db.session.add(new_book)
    db.session.commit()

    return jsonify({
      'id': new_book.id,
      'title': new_book.title,
      'price': new_book.price
    })

# endpoint to update book
@app.route("/api/book/<id>", methods=["PUT"])
def book_update(id):
    book = Book.query.get(id)
    title = request.json['title']
    price = request.json['price']

    book.title = title
    book.price = price

    db.session.commit()
    return book_schema.jsonify(book)

# endpoint to delete book
@app.route("/api/book/<id>", methods=["DELETE"])
def book_delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
    db.session.commit()

    return book_schema.jsonify(book)


if __name__ == '__main__':
    app.run(debug=True)
