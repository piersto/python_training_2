from sys import maxsize


class Contact:

    def __init__(self, first_name=None, middlename=None, lastname=None, nickname=None, title=None, company_name=None, address=None, home_phone=None,
                        mobile_phone=None, work_phone=None, fax=None, email=None, second_email=None, third_email=None, homepage=None, birthdate=None,
                        birthmonth=None, birth_year=None, anniversary_day=None, anniversary_month=None, anniversary_year=None, second_address=None,
                        second_home=None, notes=None, id=None, all_phones_from_home_page=None, all_mails_from_home_page=None, first_name_from_home_page=None):
        self.first_name = first_name
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company_name = company_name
        self.address = address
        self.home_phone =home_phone
        self.mobile_phone = mobile_phone
        self.work_phone = work_phone
        self.fax = fax
        self.email = email
        self.second_email = second_email
        self.third_email = third_email
        self.homepage = homepage
        self.birthdate = birthdate
        self.birthmonth = birthmonth
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.second_address = second_address
        self.second_home = second_home
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_mails_from_home_page = all_mails_from_home_page
        self.first_name_from_home_page = first_name_from_home_page

    def __repr__(self):
        return "%s:%s;%s;%s;%s" % (self.id, self.first_name, self.middlename, self.lastname, self.nickname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name \
                and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

