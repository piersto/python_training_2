# -*- coding: utf-8 -*-

from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="Pierre", middlename="sto", lastname="stop", nickname="nik", title="title", company_name="Company", address="3096- rue goyer", home_phone="514", mobile_phone="515",
                               work_phone="516", fax="517", email="1@sto.com", second_email="2@sto.com", third_email="3@sto.com", homepage="sto.com", birthdate="18", birthmonth="January", birth_year="1971",
                               anniversary_day="18", anniversary_month="February", anniversary_year="2018", second_address="address second", second_home="home second", notes="notes"))



def test_open_contact_view_by_index(app):
    app.contact.open_contact_view_by_index(0)

