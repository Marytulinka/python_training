# -*- coding: utf-8 -*-
from models.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact("Maria", "", "Tulina",
                                "marytulina", "Test Company",
                                "title", "Test test test", "", "7656567",
                                "123456", "432156", "test1@test.com",
                                "test2@test.com", "test3@test.com", "testcom.com",
                                "19", "April", "1988", "19",
                                "April", "2028")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


