import requests


class HttpFisher:
    @staticmethod
    def get(url, return_json=True):
        """
        对api的get请求
        :param url:
        :param return_json:get请求是否返回json格式的对象
        :return:响应结果的内容
        """
        r = requests.get(url)
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
        # json()将json对象转化为python中的字典
        # 简化代码,减少if_else结构
        # 利用三元表达式 或 利用if_return结构表示一种特例 或 相同代码结构提取为一个函数
