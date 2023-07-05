from selene import browser
from selene import be, have
from selene import command
from demoqa_tests import resources


class RegistrationPage:
    def open(self):
        browser.open('/automation-practice-form')
        browser.should(have.title('DEMOQA'))
        # browser.element('[class="main-header"]').should(have.text('Practice Form'))
        # browser.all('[id^=google_ads][id$=container__]').with_(timeout=3).wait_until(
        #     have.size_greater_than_or_equal(3)
        # )
        # browser.all('[id^=google_ads][id$=container__]').perform(command.js.remove)

    def fill_first_name(self, value):
        browser.element('#firstName').click().type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').click().type(value)

    def fill_email(self, value):
        browser.element('#userEmail').click().type(value)

    def gender_button(self, gender_name):
        browser.all('[name=gender]').element_by(have.value(gender_name)).element('..').click()

    def fill_user_number(self, value):
        browser.element('#userNumber').click().type(value)

    def fill_birthday(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)').click()

    def fill_subject(self, value):
        browser.element('#subjectsContainer').click().type(value).press_enter()

    def fill_hobbies(self, hobby_value):
        browser.element(f'//label[contains(text(), {hobby_value})]').click()

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
