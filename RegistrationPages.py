from BaseApp import BasePage
from selenium.webdriver.common.by import By


# Реализуем класс с методами, для страницы регистрации.
class RegistrationLocators:
    LOCATOR_REGISTRATION_FIELD_FIRST_NAME = (By.NAME, "first_name")
    LOCATOR_REGISTRATION_FIELD_LAST_NAME = (By.NAME, "last_name")
    LOCATOR_REGISTRATION_FIELD_EMAIL = (By.NAME, "email")
    LOCATOR_REGISTRATION_FIELD_PHONE = (By.NAME, "phone")
    LOCATOR_REGISTRATION_FIELD_PASSWORD = (By.NAME, "password")
    LOCATOR_REGISTRATION_FIELD_PASSWORD_CONFIRMATION = (By.NAME, "password_confirmation")
    LOCATOR_REGISTRATION_CHECKBOX = (By.NAME, "terms")

    LOCATOR_REGISTRATION_BUTTON = (By.TAG_NAME, "button")


class RegistrationHelper(BasePage):

    def enter_data(self, name, last_name, email, phone, password, password_confirmation):
        name_field = self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_FIELD_FIRST_NAME)
        name_field.click()
        name_field.send_keys(name)

        last_name_field = self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_FIELD_LAST_NAME)
        last_name_field.click()
        last_name_field.send_keys(last_name)

        email_field = self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_FIELD_EMAIL)
        email_field.click()
        email_field.send_keys(email)

        phone_field = self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_FIELD_PHONE)
        phone_field.click()
        phone_field.send_keys(phone)

        password_field = self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_FIELD_PASSWORD)
        password_field.click()
        password_field.send_keys(password)

        password_confirmation_field = self.find_element(
            RegistrationLocators.LOCATOR_REGISTRATION_FIELD_PASSWORD_CONFIRMATION)
        password_confirmation_field.click()
        password_confirmation_field.send_keys(password_confirmation)

        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_CHECKBOX, time=2).click()

    def click_on_the_registration_button(self):
        self.find_element(RegistrationLocators.LOCATOR_REGISTRATION_BUTTON, time=2).click()

    def check_present_word(self):
        page_text = self.get_page_text()
        return page_text

