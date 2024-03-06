# -*- coding: utf-8 -*-
import pytest
from models.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact("Tulina", "", "Maria",
                                       "marytulina", "company",
                                       "title", "Test test test", "7656567",
                                       "123456", "432156", "587645",
                                       "test@test.com", "test2@test.com", "test3@test.com",
                                       "homepage"))
    app.session.logout()
