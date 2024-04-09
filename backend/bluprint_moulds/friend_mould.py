from flask import Blueprint
# 设置子域名subdomain
friend = Blueprint('friend', __name__, url_prefix='/friend',)


@friend.route('/list')
def friend_list():
    return 'friend list'