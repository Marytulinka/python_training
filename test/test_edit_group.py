# -*- coding: utf-8 -*-
from models.group import Group
import time


def test_edit_first_group(app):
    app.session.login("admin", "secret")
    app.group.edit_first_group(Group("тест!!", "тест!!", "тест!!"))
    app.session.logout()
    time.sleep(3)


