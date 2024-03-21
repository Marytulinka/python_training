# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact("PRIVET", "", "Maria",
                                "marytulina", "Test Company",
                                "title", "Test test test", "", "7656567",
                                "123456", "432156", "test1@test.com",
                                "test2@test.com", "test3@test.com", "testcom.com",
                                "19", "April", "1988", "19",
                                "April", "2028"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)

