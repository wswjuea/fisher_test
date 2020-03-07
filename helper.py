def is_isbn_or_key(word):
    """
    判断传入参数是isbn或关键字
    :param word: 传入字符串
    :return: isbn or key
    """
    isbn_or_key = 'key'
    # isdigit()判断对象是否为数值
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')

    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
