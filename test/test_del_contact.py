# -*- coding: utf-8 -*-

def test_del_contact(app):
    app.open_home_page()
    app.contact.delete_contact()
    app.open_home_page()
