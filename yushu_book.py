from http_flask import HTTP


class YuShuBook:
    isbn_url = "http://book.feelyou.top/isbn/{}"
    keyword_url = "https://book.feelyou.top/search/{}"

    @classmethod
    def search_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls, keyword):
        url = cls.keyword_url.format(keyword)
        result = HTTP.get(url)
        return result
