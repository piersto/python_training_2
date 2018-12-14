# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMGroup
from fixture.orm import ORMContact


def test_add_contact_to_group(app, db, orm, check_ui):
    app.open_home_page()
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Vasia"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_contacts = orm.get_contacts_in_group()
    contact = random.choice(orm.get_contacts_not_in_group)
    app.contact.add_contact_to_group_by_id(contact.id)
    app.open_home_page()
    old_contacts.append(contact)
    new_contacts = orm.get_contacts_in_group()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
