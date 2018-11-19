# -*- coding: utf-8 -*-
from model.contact import Contact


def test_del_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(birthdate="18", birthmonth="January", birth_year="1971", anniversary_day="18", anniversary_month="February", anniversary_year="2018"))
    app.contact.delete_contact()
    app.open_home_page()
