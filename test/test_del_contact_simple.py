# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact_simple(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Vasia"))
    app.contact.delete_first_contact()
    app.open_home_page()
