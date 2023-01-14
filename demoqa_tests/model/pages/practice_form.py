from selene import have
from selene.support.shared import browser
from demoqa_tests.model.controls.checkboxes import Checkboxes
from demoqa_tests.model.controls.datepicker import Datepicker
from demoqa_tests.model.controls.drop_down import Dropdown
from demoqa_tests.model.controls.radiobutton import Radiobutton
from demoqa_tests.utils import path_to_file, date_config


class PracticeForm:
    def __init__(self, user):
        self.user = user

    def open_page(self):
        browser.open('/automation-practice-form')
        return self

    def fill_name(self):
        browser.element('#firstName').type(self.user.first_name)
        browser.element('#lastName').type(self.user.last_name)
        return self

    def fill_contacts(self):
        browser.element('#userEmail').type(self.user.email)
        browser.element('#userNumber').type(self.user.phone)
        return self

    def select_gender(self):
        gender = Radiobutton(browser.all('[name=gender]'))
        gender.select_by_value(self.user.gender)
        return self

    def select_birthday(self):
        birthday_datepicker = Datepicker(browser.element('#dateOfBirthInput'))
        birthday_datepicker.set_date(self.user.birthday)
        return self

    def input_subject(self):
        browser.element('#subjectsInput').type(self.user.subject).press_enter()
        return self

    def select_hobbies(self):
        check_hobbies = Checkboxes(browser.all('[for^=hobbies-checkbox]'))
        check_hobbies.select(self.user.hobbies)
        return self

    def send_image(self):
        browser.element('#uploadPicture').set_value(path_to_file.generate_path_upload(self.user.image))
        return self

    def input_address(self):
        browser.element('#currentAddress').type(self.user.address)
        return self

    def select_state(self):
        dropdown = Dropdown('#state')
        dropdown.select(self.user.state)
        return self

    def select_city(self):
        dropdown = Dropdown('#city')
        dropdown.select(self.user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def assert_results_registration(self):
        browser.element('.table').all('td').even.should(have.texts(
            self.user.first_name + ' ' + self.user.last_name,
            self.user.email,
            self.user.gender,
            self.user.phone,
            self.user.birthday.strftime(date_config.datetime_view_format),
            self.user.subject,
            self.user.hobbies,
            self.user.image,
            self.user.address,
            self.user.state + ' ' + self.user.city))
        return self

