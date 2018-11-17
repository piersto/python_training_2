# -*- coding: utf-8 -*-

from model.contact import Contact


def test_modify_contact_first_namme(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="New first name"))
    app.session.logout()


def test_modify_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(middlename="New middlename"))
    app.session.logout()
