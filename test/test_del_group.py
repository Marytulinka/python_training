# -*- coding: utf-8 -*-
from models.group import Group


def test_delete_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_first_group()



