# -*- coding: utf-8 -*-
import pytest
from models import Contact
from contactdate import Contactdate


@pytest.fixture
def cd(request):
    fixture = Contactdate()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(cd):
    cd.login("admin", "secret")
    cd.create_new_contact(Contact("Tulina", "", "Maria",
                                       "marytulina", "company",
                                       "title", "Test test test", "7656567",
                                       "123456", "432156", "587645",
                                       "test@test.com","test2@test.com", "test3@test.com",
                                       "homepage"))
    cd.logout()
