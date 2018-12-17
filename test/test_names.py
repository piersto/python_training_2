from model.contact import Contact


def test_first_name_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.first_name == contact_from_edit_page.first_name


def test_lastname_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname


def test_address_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.address == contact_from_edit_page.address


def test_contacs_on_home_page_vs_db(app, db):
    contact_from_home_page = app.contact.get_contact_list()
    contact_from_db = db.get_contact_list()
    assert sorted(contact_from_home_page,  key=Contact.id_or_max) == sorted(contact_from_db, key=Contact.id_or_max)

