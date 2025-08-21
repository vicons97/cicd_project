from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

class SignInPage(BasePage):
    email_field = By.NAME,"email"
    password_field = By.NAME,"password"
    submit_btn = By.ID,"submit-login"
    authentication_error = By.CLASS_NAME,"alert-danger"

    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    def enter_sign_in_info(self, email, password):
        self.logger.info(f"Llenando formulario de login con email: {email} y password: {password}")
        self.enter_text(self.email_field, email)
        self.enter_text(self.password_field, password)
        self.logger.info("Haciendo click en el botón de submit")
        self.click_element(self.submit_btn)

    def is_authentication_error_visible(self):
        return self.is_element_visible(self.authentication_error)

    def get_authentication_error_message(self):
        return self.get_text(self.authentication_error)