from flask import Blueprint

news = Blueprint('news', __name__, url_prefix='/news')


@news.route('list')
def news_list():
    return 'news_list'
