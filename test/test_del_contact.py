# -*- coding: utf-8 -*-
from models.contact import Contact


def test_del_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("PRIVET", "", "Maria", "",
                                   "Test", "", "", "", "", "", "", "", "",
                                   "", "", "20", "April", "1988", "20", "April", "2028"))
    old_contacts = app.contact.get_contact_list()
    app.contact.del_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)

