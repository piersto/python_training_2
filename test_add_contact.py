# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class AddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_id("LoginForm").submit()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Pierre")
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys("sto")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("stop")
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys("nik")
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys("title")
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys("Company")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("3096- rue goyer")
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys("514")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("515")
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys("516")
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys("517")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("1@sto.com")
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys("2@sto.com")
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys("3@sto.com")
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys("sto.com")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("18")
        wd.find_element_by_name("bday").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("January")
        wd.find_element_by_name("bmonth").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1971")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("18")
        wd.find_element_by_name("aday").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("February")
        wd.find_element_by_name("amonth").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys("2018")
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys("address second")
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys("home second")
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys("notes")
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Notes:'])[1]/following::input[1]").click()
        wd.find_element_by_link_text("home page").click()
        wd.find_element_by_link_text("Logout").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.wd.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
