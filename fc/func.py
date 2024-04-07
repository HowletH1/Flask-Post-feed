import json

from fc.post import Post


class PostsFunc:
    """
    This class provides methods for interacting with the posts' data.
    """
    def __init__(self, posts_path, comments_path):
        self.posts_path = posts_path
        self.comments_path = comments_path

    def get_all_posts(self):
        """
        Retrieve all posts from the data store.

        Returns:
        list: A list of Post objects.
        """
        return self.load_posts()

    def load_posts(self):
        """
        Load the posts data from the file system.

        Returns:
            list: A list of Post objects.
        """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            new_posts = []
            posts_data = json.load(file)

            for post in posts_data:
                new_posts.append(Post(
                    post['poster_name'],
                    post['poster_avatar'],
                    post['pic'],
                    post['content'],
                    post['views_count'],
                    post['likes_count'],
                    post['pk']))
        return new_posts

    def get_post_by_pk(self, pk):
        """
        Retrieve a post by its primary key.

        Args:
            pk (int): The primary key of the post.

        Returns:
            Post or None: The post with the specified primary key, or None if no post with that key exists.
        """
        posts = self.load_posts()
        for post in posts:
            if post.pk == pk:
                return post
        return

    def search_posts(self, substr):
        """
        Search for posts containing a specified substring.

        Args:
            substr (str): The substring to search for.

        Returns:
            list: A list of Post objects containing the specified substring.
        """
        posts = self.load_posts()
        new_posts = []

        for post in posts:
            if substr.lower() in post.content.lower():
                new_posts.append(post)
        return new_posts

    def load_comments(self):
        """
        Load the comments data from the file system.

        Returns:
            list: A list of comment data.
        """
        with open(self.comments_path, 'r', encoding='utf-8') as file:
            comments = json.load(file)
        return comments

    def get_comments_by_post_id(self, post_id):
        """
        Retrieve the comments for a specified post.

        Args:
            post_id (int): The ID of the post.

        Returns:
            list: A list of comment data for the specified post.
        """
        comments = self.load_comments()
        post_comments = []

        for comment in comments:
            if comment['post_id'] == post_id:
                post_comments.append(comment)
        return post_comments

    def get_post_by_username(self, username):
        """
        Retrieve posts posted by a specified user.

        Args:
            username (str): The username of the user.

        Returns:
            list: A list of Post objects posted by the specified user.
        """
        posts = self.load_posts()
        user_posts = []

        for post in posts:
            if post.poster_name.lower() == username.lower():
                user_posts.append(post)

        return user_posts

    def load_posts_json(self):
        """
        Load the posts data from the file system as JSON.

        Returns:
            list: A list of post data in JSON format.
        """
        with open(self.posts_path, 'r', encoding='utf-8') as file:
            posts_data = json.load(file)

        return posts_data

    def load_posts_pk(self, pk):
        """
        Retrieve a post by its primary key, using the JSON data format.

        Args:
            pk (int): The primary key of the post.

        Returns:
            dict or None: The post with the specified primary key, or None if no post with that key exists.
        """
        posts = self.load_posts_json()
        for post in posts:
            if post['pk'] == pk:
                return post
        return
