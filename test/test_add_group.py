# -*- coding: utf-8 -*-
from models.group import Group
import time


def test_add_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("тест", "тест", "тест"))
    app.session.logout()
    time.sleep(3)

def test_add_empty_group(app):
    app.session.login("admin", "secret")
    app.group.create(Group("", "", ""))
    app.session.logout()
    time.sleep(3)


