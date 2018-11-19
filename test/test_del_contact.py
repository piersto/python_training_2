# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(notes="test"))
    app.contact.delete_contact()
    app.open_home_page()
