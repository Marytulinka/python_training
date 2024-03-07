# -*- coding: utf-8 -*-
import time


def test_delete_group(app):
    app.session.login("admin", "secret")
    app.group.delete_first_group()
    app.session.logout()
    time.sleep(3)


