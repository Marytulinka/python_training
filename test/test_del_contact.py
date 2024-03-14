# -*- coding: utf-8 -*-
import time


def test_del_contact(app):
    app.contact.del_first_contact()
    time.sleep(3)
