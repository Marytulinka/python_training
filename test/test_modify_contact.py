# -*- coding: utf-8 -*-
from models.contact import Contact
import time


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact("PRIVET", "", "Maria", "",
                                   "C:\\Users\\Mariya.Tulina\\PycharmProjects\\python_training\\icon-copy.jpg",
                                   "","","","","","","","",
                                   "","","","20","April","1988","20","April","2028"))
    app.contact.modify_first_contact(Contact("Maria", "Sergeevna", "Tulina",
                                       "marytulina", "C:\\Users\\Mariya.Tulina\\PycharmProjects\\python_training\\icon-copy.jpg",
                                        "COMPANY", "TITLE", "Test test test", "7656567",
                                       "123456", "", "",
                                       "test@test.com", "", "", "",
                                       "20", "May", "1989",
                                       "20", "May", "2029"))
    time.sleep(3)
