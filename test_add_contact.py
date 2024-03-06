# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login("admin", "secret")
    app.create_new_contact(Contact("Tulina", "", "Maria",
                                       "marytulina", "company",
                                       "title", "Test test test", "7656567",
                                       "123456", "432156", "587645",
                                       "test@test.com", "test2@test.com", "test3@test.com",
                                       "homepage"))
    app.logout()
