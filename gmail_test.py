from selenium import webdriver

import constants
from gmail import LoginPage, MainPage


class TestGmailSendMessage:

    def setup(self):
        desired_capabilites = {
            "browserName": "chrome",
            "maxInstances": 5
        }
        command_executor = constants.COMMAND_EXECUTOR
        self.driver = webdriver.Remote(
            command_executor=command_executor,
            desired_capabilities=desired_capabilites
        )
        self.driver.get('https://www.gmail.com/')

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.username(constants.USERNAME)
        login_page.next_page()
        assert login_page.is_username_correct(), 'Неверный Email'
        login_page.password(constants.PASSWORD)
        login_page.next_page()
        assert login_page.is_password_correct(), 'Пароль введен неверно'

    def test_message_send(self):
        LoginPage(self.driver).full_login(
            constants.USERNAME,
            constants.PASSWORD
        )
        main_page = MainPage(self.driver)
        messages_count = main_page.messages_count()
        assert messages_count == '2', (
                'Неправильно посчитано количество сообщений, '
                + messages_count + ' != 2'
        )
        context = {
            'recipient': constants.RECIPIENT_MAIL,
            'topic': constants.TOPIC,
            'text': constants.TEXT + messages_count,
        }
        main_page.send_message(context)

    def teardown(self):
        self.driver.close()
