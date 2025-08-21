from .base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger import get_logger

class HomePage(BasePage):

    #Locators
    login_button = (By.CLASS_NAME, "user-info")
    register_button = (By.XPATH, "//[@class='blockcart cart-preview inactive']")
    logout_button = (By.CLASS_NAME, "logout")
    username_text = (By.CLASS_NAME, "account")
    search_field = (By.ID, "search_query_top")
    search_button = (By.NAME, "submit_search")
    search_results = (By.CLASS_NAME, "product-name")

    #Variables
    url = "https://teststore.automationtesting.co.uk/index.php"

    #Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.logger = get_logger(__name__)

    #Actions
    def click_login(self):
        self.logger.info("Haciendo click en el botón de login")
        self.click_element(self.login_button)

    def click_register(self):
        self.logger.info("Haciendo click en el botón de registro")
        self.click_element(self.register_button)

    def navigate_to_home_page(self):
        self.logger.info("Navegando a la página principal")
        self.driver.get("https://teststore.automationtesting.co.uk/index.php")
        self.logger.info("Página principal cargada exitosamente")

    def click_logout(self):
        self.logger.info("Haciendo click en el botón de logout")
        self.click_element(self.logout_button)

    def get_username(self):
        self.logger.info("Obteniendo el nombre de usuario")
        return self.get_text(self.username_text)

    def is_logged_in(self):
        return self.is_element_visible(self.logout_button)
