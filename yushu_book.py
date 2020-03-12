from http_fisher import HttpFisher
from flask import current_app


# current_app当前的Flask app对象,核心对象的再次导入可能会造成循环导包,用current_app可以获取当前对象的config设置信息


class YuShuBook:
    isbn_url = "http://book.feelyou.top/isbn/{}"
    keyword_url = "https://book.feelyou.top/search?q={}&count={}&start={}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HttpFisher.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword, page=1):
        url = cls.keyword_url.format(keyword, current_app.config['PER_PAGE'], cls.calculate_start(page=page))
        result = HttpFisher.get(url)
        return result

    @staticmethod
    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']
