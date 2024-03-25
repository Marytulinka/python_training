# -*- coding: utf-8 -*-
from models.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("Angela", "", "Jolie", "",
                                   "Test", "", "", "", "", "", "", "", "",
                                   "", "", "20", "April", "1988", "20", "April", "2028"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact("Maria", "Sergeevna", "Tulina",
                                       "marytulina", "TEST", "COMPANY", "ADDRESSS", "65432",
                                       "7656567", "123456", "", "test@test.com", "",
                                       "", "", "20", "May", "1989", "20", "May", "2029")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
