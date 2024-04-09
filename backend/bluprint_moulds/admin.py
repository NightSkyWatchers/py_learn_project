import flask
from flask import Blueprint

ad = Blueprint('ad', __name__, subdomain='admin')


@ad.route('/ad')
def admin_page():
    return 'This is the admin page.'