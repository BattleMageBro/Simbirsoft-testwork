from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    USERNAME = (By.NAME, 'identifier')
    PASSWORD = (By.NAME, 'password')
    NEXT_BUTTON = (By.XPATH, '//span[text()="Далее"]/parent::button')


class MainPageLocators(object):
    GO_BUTTON = (By.ID, 'submit')
    USER_MESSAGES = (By.XPATH, '//span[@name="farit.valiahmetov"]')
    WRITE_MESSAGE_BUTTON = (By.XPATH, '//div[contains(text(),"Написать")]')
    RECIPIENT = (By.XPATH, '//textarea[contains(@aria-label, "Кому")]')
    TOPIC = (By.XPATH, '//input[contains(@aria-label, "Тема")]')
    TEXT = (By.XPATH, '//div[contains(@aria-label, "Тело письма")]')
    SEND_MESSAGE_BUTTON = (
        By.XPATH,
        '//div[contains(text(),"Отправить") and @role="button"]'
    )
    SENT_MESSAGE = (By.LINK_TEXT, 'Отправленные')
