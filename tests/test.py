import pytest
from app import app

keys_list = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk",
}


def api_test_all_posts():
    resp = app.test_client().get('/api/posts/')
    assert resp.status_code == 200
    api_resp = resp.json
    assert type(api_resp) == list
    assert set(api_resp[0].keys()) == keys_list


def api_test_post():
    resp = app.test_client().get('/api/posts/1')
    assert resp.status_code == 200
    api_resp = resp.json
    assert type(api_resp) == dict
    assert set(api_resp.keys()) == keys_list
