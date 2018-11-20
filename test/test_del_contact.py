# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(birthdate="18", birthmonth="January", birth_year="1971", anniversary_day="18", anniversary_month="February", anniversary_year="2018"))
    app.contact.delete_contact()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
