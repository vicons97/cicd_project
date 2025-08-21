from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import allure

@allure.title("Inicio de sesión exitoso")
@pytest.mark.smoke
def test_login(pages):
    with allure.step("Navegar a la página principal"):
        pages.home.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        pages.home.click_login()

    with allure.step("Ingresar credenciales"):
        pages.sign_in.enter_sign_in_info("test@test.com", "test123")

    with allure.step("Verificar inicio de sesión exitoso"):
        assert pages.home.is_logged_in(), "No se inició sesión correctamente"
        assert pages.home.get_username() == "John Smith", "El nombre de usuario no coincide"

@allure.title("Inicio de sesión fallido")
@pytest.mark.regression
def test_login2(pages):
    with allure.step("Navegar a la página principal"):
        pages.home.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        pages.home.click_login()

    with allure.step("Ingresar credenciales"):
        pages.sign_in.enter_sign_in_info("testuser@test.com", "testpassword")

    with allure.step("Verificar inicio de sesión exitoso"):
        assert pages.sign_in.is_authentication_error_visible(), "El mensaje de error no es visible"
        assert pages.sign_in.get_authentication_error_message() == "Authentication failed.", "El mensaje de error no coincide"



@allure.title("Inicio de sesión fallido")
@pytest.mark.regression
def test_login3(pages):
    with allure.step("Navegar a la página principal"):
        pages.home.navigate_to_home_page()

    with allure.step("Hacer click en el botón de login"):
        pages.home.click_login()

    with allure.step("Ingresar credenciales"):
        pages.sign_in.enter_sign_in_info("testuser@test.com", "testpassword")

    with allure.step("Verificar inicio de sesión exitoso"):
        assert pages.sign_in.is_authentication_error_visible(), "El mensaje de error no es visible"
        assert pages.sign_in.get_authentication_error_message() == "Authentication failed.", "El mensaje de error no coincide"


