import time

from locators import LoginPageLocators, MainPageLocators


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class LoginPage(BasePage):

    def username(self, username):
        username_field = self.driver.find_element(*LoginPageLocators.USERNAME)
        username_field.clear()
        username_field.send_keys(username)

    def password(self, password):
        password_field = self.driver.find_element(*LoginPageLocators.PASSWORD)
        password_field.clear()
        password_field.send_keys(password)

    def next_page(self):
        self.driver.find_element(*LoginPageLocators.NEXT_BUTTON).click()
        time.sleep(2)

    def full_login(self, username, password):
        self.username(username)
        self.next_page()
        self.password(password)
        self.next_page()

    def is_username_correct(self):
        return 'Не удалось найти аккаунт Google' not in self.driver.page_source

    def is_password_correct(self):
        return 'Неверный пароль.' not in self.driver.page_source


class MainPage(BasePage):

    def messages_count(self):
        user_messages = self.driver.find_elements(
            *MainPageLocators.USER_MESSAGES
        )
        messages = str(len(user_messages) // 2)
        return messages

    def send_message(self, context):
        self.driver.find_element(
            *MainPageLocators.WRITE_MESSAGE_BUTTON
        ).click()
        time.sleep(1)
        self.driver.find_element(
            *MainPageLocators.RECIPIENT
        ).send_keys(context['recipient'])
        self.driver.find_element(
            *MainPageLocators.TOPIC
        ).send_keys(context['topic'])
        self.driver.find_element(
            *MainPageLocators.TEXT
        ).send_keys(context['text'])
        self.driver.find_element(
            *MainPageLocators.SEND_MESSAGE_BUTTON
        ).click()
        time.sleep(3)

