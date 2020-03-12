from wtforms import Form, StringField, IntegerField
from wtforms.validators import Length, NumberRange, DataRequired


class SearchForm(Form):
    q = StringField(
        validators=[
            DataRequired(message='错误信息'),
            Length(min=1, max=30, message='自定义错误提示')
        ]
    )

    page = IntegerField(
        validators=[
            NumberRange(min=1, max=99)
        ],
        default=1
    )
