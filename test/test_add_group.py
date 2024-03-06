# -*- coding: utf-8 -*-
import pytest
from models.group import Group
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login("admin", "secret")
    app.create_group(Group("тест", "тест", "тест"))
    app.session.logout()



