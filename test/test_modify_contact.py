# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_first_name(app):
    app.open_home_page()
    app.contact.modify_first_contact(Contact(first_name="New first name"))


def test_modify_contact_middlename(app):
    app.open_home_page()
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
