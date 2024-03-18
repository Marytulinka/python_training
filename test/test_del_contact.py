# -*- coding: utf-8 -*-
from models.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("PRIVET", "", "Maria", "",
                                   "Test", "", "", "", "", "", "", "", "",
                                   "", "", "20", "April", "1988", "20", "April", "2028"))
    app.contact.del_first_contact()

