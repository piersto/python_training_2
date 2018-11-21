# -*- coding: utf-8 -*-

from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def submit_contact_form(self):
        wd = self.app.wd
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contact_form(contact)
        self.fill_contact_drop_downs(contact)
        self.submit_contact_form()
        self.app.go_back_to_home_page()

    def fill_contact_drop_downs(self, contact):
        wd = self.app.wd
        self.select_from_drop_down("bday", contact.birthdate)
        self.select_from_drop_down("bmonth", contact.birthmonth)
        self.select_from_drop_down("aday", contact.anniversary_day)
        self.select_from_drop_down("amonth", contact.anniversary_month)

    def select_from_drop_down(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def type(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.type("firstname", contact.first_name)
        self.type("middlename", contact.middlename)
        self.type("lastname", contact.lastname)
        self.type("nickname", contact.nickname)
        self.type("title", contact.title)
        self.type("company", contact.company_name)
        self.type("address", contact.address)
        self.type("home", contact.home_phone)
        self.type("mobile", contact.mobile_phone)
        self.type("work", contact.work_phone)
        self.type("fax", contact.fax)
        self.type("email", contact.email)
        self.type("email2", contact.second_email)
        self.type("email3", contact.third_email)
        self.type("homepage", contact.homepage)
        self.type("address2", contact.second_address)
        self.type("phone2", contact.second_home)
        self.type("notes", contact.notes)
        self.type("byear", contact.birth_year)
        self.type("ayear", contact.anniversary_year)

    def modify_first_contact(self, new_contact_data):
        wd = self.app.wd
        # open modification form
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        self.fill_contact_drop_downs(new_contact_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.app.go_back_to_home_page()

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Edit / add address book entry'])[1]/following::input[1]")) > 0):
            wd.find_element_by_link_text("add new").click()

    def delete_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()
        self.accept_next_alert = True
        wd.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='Select all'])[1]/following::input[2]").click()
        wd.switch_to_alert().accept()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_xpath("//img[@alt='Edit']"))

    def get_contact_list(self):
        wd = self.app.wd
        contacts = []
        self.app.open_home_page()
        for element in wd.find_elements_by_css_selector("tr[name=entry]"):
            text = element.text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(first_name=text, id=id))
        return contacts




