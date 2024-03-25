from selenium.webdriver.support.ui import Select
from models.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_new_contact_page()
        self.fill_contact_form(contact)
        self.return_to_home_page()
        self.group_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # FIO
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # Photo
        # wd.find_element_by_name("photo").send_keys(contact.photo)
        # Company
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("address", contact.address)
        # Telephone
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # email
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # Birthday
        self.change_date_value("bday", contact.bday)
        self.change_date_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_date_value("aday", contact.aday)
        self.change_date_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        wd.find_element_by_xpath("//div[@id='content']/form/input[20]").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_date_value(self, date_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(date_name).click()
            Select(wd.find_element_by_name(date_name)).select_by_visible_text(text)

    def modify_first_contact(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        self.fill_contact_form(contact)
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.group_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.group_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def go_to_home_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_id("maintable")) > 0:
            wd.find_element_by_link_text("home").click()

    def open_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    group_cache = None

    def get_contact_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("tr[name='entry']"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                last_name = element.find_elements_by_css_selector("td")[1].text
                first_name = element.find_elements_by_css_selector("td")[2].text
                self.group_cache.append(Contact(id=id, firstname=first_name, lastname=last_name))
        return list(self.group_cache)
        

