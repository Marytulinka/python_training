# -*- coding: utf-8 -*-
from models.group import Group
import time


def test_add_group(app):
    app.group.create(Group("тест", "тест", "тест"))
    time.sleep(3)

def test_add_empty_group(app):
    app.group.create(Group("", "", ""))



