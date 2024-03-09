# -*- coding: utf-8 -*-
import time


def test_del_contact(app):
    app.session.login("admin", "secret")
    app.contact.del_first_contact()
    app.session.logout()
    time.sleep(3)
