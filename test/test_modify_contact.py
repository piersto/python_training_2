# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_first_name(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Vasia"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(first_name="New first name"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)


def test_modify_contact_middlename(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Vasia"))
    old_contacts = app.contact.get_contact_list()
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
