from flask import jsonify

from fisher import app
from helper import is_isbn_or_key
from yushu_book import YuShuBook


@app.route("/book/search/<path:q>/<int:page>")
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return jsonify(result)
