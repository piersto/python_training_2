# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Vasia"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact()
    app.open_home_page()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts
