import re

def test_mails_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_mails_from_home_page == merge_mails_like_on_home_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_mails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.second_email, contact.third_email]))))

