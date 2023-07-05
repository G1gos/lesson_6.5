import os

from selene import browser
from selene import be, have
from selene import command
from demoqa_tests import resources


class RegistrationPage:

    def __init__(self,
                 first_name: str = 'Damir',
                 last_name: str = 'Gimranov',
                 email: str = 'd.gimranov@atol.ru',
                 gender_name: str = 'Male',
                 user_number: str = '1234567890',
                 year_birthday: str = '1999',
                 month_birthday: str = 'May',
                 day_birthday: str = '01',

                 subject: str = 'Maths',
                 hobby: str = 'Sports',
                 path_for_picture: str = 'image/meme.jpg',
                 address: str = 'my_address',
                 state: str = 'NCR',
                 city: str = 'Noida',
                 ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender_name = gender_name
        self.user_number = user_number
        self.year_birthday = year_birthday
        self.month_birthday = month_birthday
        self.day_birthday = day_birthday

        self.subject = subject
        self.hobby = hobby
        self.path_for_picture = path_for_picture

        self.address = address
        self.state = state
        self.city = city
    def open(self):
        browser.open('/automation-practice-form')
        browser.should(have.title('DEMOQA'))
        # browser.element('[class="main-header"]').should(have.text('Practice Form'))
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, first_name: str = None):
        if first_name is None:
            first_name = self.first_name
        browser.element('#firstName').click().type(first_name)

    def fill_last_name(self, last_name: str = None):
        if last_name is None:
            last_name = self.last_name
        browser.element('#lastName').click().type(last_name)

    def fill_email(self, email: str = None):
        if email is None:
            email = self.email
        browser.element('#userEmail').click().type(email)

    def gender_button(self, gender_name: str = None):
        if gender_name is None:
            gender_name = self.gender_name
        browser.all('[name=gender]').element_by(have.value(gender_name)).element('..').click()

    def fill_user_number(self, user_number: str = None):
        if user_number is None:
            user_number = self.user_number
        browser.element('#userNumber').click().type(user_number)

    def fill_birthday(self, year_birthday: str = None, month_birthday: str = None, day_birthday: str = None):
        browser.element('#dateOfBirthInput').click()
        if year_birthday is None:
            year_birthday = self.year_birthday
        browser.element('.react-datepicker__year-select').type(year_birthday)
        if month_birthday is None:
            month_birthday = self.month_birthday
        browser.element('.react-datepicker__month-select').type(month_birthday)
        if day_birthday is None:
            day_birthday = self.day_birthday
        browser.element(f'.react-datepicker__day--0{day_birthday}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, subject: str = None):
        if subject is None:
            subject = self.subject
        browser.element('#subjectsContainer').click().type(subject).press_enter()

    def fill_hobby(self, hobby: str = None):
        if hobby is None:
            hobby = self.hobby
        browser.element(f'//label[contains(text(), {hobby})]').click()

    def upload_picture(self, picture):
        browser.element('#uploadPicture').send_keys('')
def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()
    registration_page.fill_first_name('Damir')
    registration_page.fill_last_name('Gigos')
    registration_page.fill_email('d.gimranov@atol.ru')
    registration_page.gender_button('Male')
    registration_page.fill_user_number('9254742233')
    registration_page.fill_birthday('1999', 'May', '11')
    registration_page.fill_subject('English')




# registration_page.fill_last_name('Kramarenko')
# ...
# registration_page.submit()
# registration_page.should_have_registered(yasha)
# ... или использовав идеи шаблона Fluent PageObject:
# registration_page.open()
# registration_page \
#     .fill_first_name('Yasha') \
#     .fill_last_name('Kramarenko') \
#     .fill_email('yashaka@gmail.com') \
#     ... \
#     .submit()
# registration_page.should_have_registered('Yasha Kramarenko', 'yashaka@gmail.com', ...)
