from flask import render_template, Blueprint, request
from pprint import pprint

from fc.func import PostsFunc

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates', static_folder='./static',
                           static_url_path='/static')
posts = PostsFunc('./data/posts.json', './data/comments.json')


@main_blueprint.route('/')
def index_page():
    """
    This function is the index page of the website.

    :param request: The request object from the user.
    :return: The rendered index.html template with the posts passed as a variable.
    """
    all_posts = posts.get_all_posts()
    return render_template('index.html', posts=all_posts)


@main_blueprint.route('/posts/<int:postid>')
def post_page(postid):
    """
    This function is responsible for rendering the post page of the website.

    Parameters:
    postid (int): The unique ID of the post to be rendered.

    Returns:
    The rendered post.html template with the post and its comments passed as variables.

    """
    found_post = posts.get_post_by_pk(postid)
    comments = posts.get_comments_by_post_id(postid)
    return render_template('post.html', post=found_post, comments=comments)


@main_blueprint.route('/search', methods=['GET'])
def search_page():
    """
    This function is responsible for handling the search page of the website.

    It takes in a search query from the user and returns a list of posts that match the query.

    :param request: The request object from the user.
    :return: The rendered search.html template with the posts and the search query passed as variables.
    """
    que = request.args.get('s')
    found_posts = posts.search_posts(que)
    return render_template('search.html', posts=found_posts, sub=que)


@main_blueprint.route('/users/<username>', methods=['GET'])
def user_page(username):
    """
    This function is responsible for handling the user page of the website.

    It takes in a username from the user and returns a list of posts made by the user.

    Parameters:
    username (str): The username of the user whose posts are to be displayed.

    Returns:
    The rendered user-feed.html template with the posts and the username passed as variables.

    """
    user_posts = posts.get_post_by_username(username)
    return render_template('user-feed.html', posts=user_posts, username=username)
