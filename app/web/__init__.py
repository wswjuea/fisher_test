from flask import Blueprint

web = Blueprint('web', __name__)
# 'web'是蓝图的名称,第二个参数为import_name指定蓝图所在的包或模块,,__name__即当前文件名book

from app.web import book
