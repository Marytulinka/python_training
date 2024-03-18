# -*- coding: utf-8 -*-
from models.contact import Contact
import time


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("PRIVET", "", "Maria", "",
                                   "Test", "", "", "", "", "", "", "", "",
                                   "", "", "20", "April", "1988", "20", "April", "2028"))
    app.contact.modify_first_contact(Contact("Maria", "Sergeevna", "Tulina",
                                       "marytulina", "TEST", "COMPANY", "ADDRESSS", "65432",
                                       "7656567", "123456", "", "test@test.com", "",
                                       "", "", "20", "May", "1989", "20", "May", "2029"))
    time.sleep(3)
