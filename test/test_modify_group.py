# -*- coding: utf-8 -*-
from models.group import Group
import time


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(name="New group"))
    time.sleep(3)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.modify_first_group(Group(header="New header"))

