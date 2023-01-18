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


def test_all_posts():
    res = app.test_client().get('/api/posts/')
    assert res.status_code == 200
    resp = res.json
    assert type(resp) == list
    assert set(resp[0].keys()) == keys_list


def test_post():
    res = app.test_client().get('/api/posts/1')
    assert res.status_code == 200
    resp = res.json
    assert type(resp) == dict
    assert set(resp.keys()) == keys_list
