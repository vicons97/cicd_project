# conftest.py
import pytest
import tempfile
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

from pages.home_page import HomePage
from pages.sing_in_page import SignInPage

# Importa ChromeDriverManager solo si no estamos en GitHub Actions
if not os.environ.get("GITHUB_ACTIONS"):
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    # Opciones para ejecución en cualquier entorno
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    if os.environ.get("GITHUB_ACTIONS"):
        # Configuración específica para GitHub Actions
        chrome_options.add_argument("--headless")
        user_data_dir = tempfile.mkdtemp()
        chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        # Configuración para ejecución local
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)

    yield driver
    driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def sign_in_page(driver):
    return SignInPage(driver)

@pytest.fixture
def pages(driver):
    class Pages:
        def __init__(self, driver):
            self.home = HomePage(driver)
            self.sign_in = SignInPage(driver)
    
    return Pages(driver)