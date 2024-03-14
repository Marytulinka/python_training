# -*- coding: utf-8 -*-
from models.contact import Contact
import time


def test_edit_contact(app):
    app.session.login("admin", "secret")
    app.contact.edit_first_contact(Contact("Maria", "Sergeevna", "Tulina",
                                       "marytulina", "C:\\Users\\Mariya.Tulina\\PycharmProjects\\python_training\\icon-copy.jpg", "COMPANY",
                                       "TITLE", "Test test test", "7656567",
                                       "123456", "", "",
                                       "test@test.com", "", "", "",
                                       "20", "May", "1989",
                                       "20", "May", "2029"))
    app.session.logout()
    time.sleep(3)
