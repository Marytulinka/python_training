# -*- coding: utf-8 -*-
from models.contact import Contact
import time


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("PRIVET", "", "Maria",
                                       "marytulina", "C:\\Users\\Mariya.Tulina\\PycharmProjects\\python_training\\icon.jpg",
                                       "company", "title", "Test test test", "7656567",
                                       "123456", "432156", "587645",
                                       "test@test.com", "test2@test.com", "test3@test.com",
                                       "homepage",
                                       "19", "April", "1988",
                                       "19", "April", "2028"))
    app.session.logout()
    time.sleep(3)
