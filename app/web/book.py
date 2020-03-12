from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from . import web

from app.forms.book import SearchForm


@web.route("/book/search")
def search():
    # request链接末端的?参数方式获取参数,request对象是由http请求触发的,所以必须放在视图函数中
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        # strip()去除前后的空格
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        # flask的jsonify,将信息(包括status code和headers)封装成json格式返回
        return jsonify(result)
    else:
        return jsonify(form.errors)
