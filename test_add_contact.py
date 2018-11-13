# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from contact import Contact
import unittest

class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.log_in(wd)
        self.fill_contact_form(wd, Contact(first_name="Pierre", middlename="sto", lastname="stop", nickname="nik", title="title", company_name="Company", address="3096- rue goyer", home_phone="514", mobile_phone="515",
                               work_phone="516", fax="517", email="1@sto.com", second_email="2@sto.com", third_email="3@sto.com", homepage="sto.com", birthdate="18", birthmonth="January", birth_year="1971",
                               anniversary_day="18", anniversary_month="February", anniversary_year="2018", second_address="address second", second_home="home second", notes="notes"))
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.log_in(wd)
        self.fill_contact_form(wd, Contact(first_name="", middlename="", lastname="", nickname="", title="", company_name="", address="", home_phone="", mobile_phone="",
                               work_phone="", fax="", email="", second_email="", third_email="", homepage="", birthdate="-", birthmonth="-", birth_year="",
                               anniversary_day="-", anniversary_month="-", anniversary_year="", second_address="", second_home="", notes=""))
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def go_back_to_home_page(self, wd):
        wd.find_element_by_link_text("home page").click()

    def submit_contact_form(self, wd):
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def fill_contact_form(self, wd, contact):
        self.open_add_contact_page(wd)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_name)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.second_email)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.third_email)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birthdate)
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birthmonth)
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.second_address)
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.second_home)
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        self.submit_contact_form(wd)
        self.go_back_to_home_page(wd)


    def open_add_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def log_in(self, wd):
        self.open_login_page(wd)
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()

    def open_login_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()