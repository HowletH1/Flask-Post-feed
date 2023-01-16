from flask import jsonify, Blueprint

from fc.func import PostsFunc
import logging
import datetime

api_blueprint = Blueprint('api_blueprint', __name__)
posts = PostsFunc('./data/posts.json', './data/comments.json')
logging.basicConfig(filename='./logs/api.log', level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')


@api_blueprint.route('/api/posts/', methods=['GET'])
def get_all_posts():
    logging.info(f'{datetime.datetime.now()} [INFO] запрос /api/posts/')
    res = posts.load_posts_json()
    return jsonify(res)


@api_blueprint.route('/api/posts/<int:postid>', methods=['GET'])
def get_post_by_id(postid):
    logging.info(f'{datetime.datetime.now()} [INFO] запрос /api/posts/{postid}')
    return jsonify(posts.load_posts_pk(postid))
