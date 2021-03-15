import json
import os

from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Login
btn_top_login = "//div[contains(@id,'LoginInfo')]//i"
cmp_email = "//*[@id='Input_UsernameVal']"
cpm_password = "//*[@id='Input_PasswordVal']"
btn_submit_login = "(//button[@type='submit'])[1]"
img_login = "//img[@class='img-circle']"


class WebLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')
        
    @property
    def user_data(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = current_path + "/../data/" + self._get_cod_pais + '/Users.json'
        with open(file_name) as user_file:
            return json.load(user_file)
            
    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='SignUp con nombre ${name}, email ${email} y contraseña ${pass}')
    def singup_with_credentials(self, name, email, password):
        pass

    @keyword(name='SignUp como ${rol}')
    def sing_up(self, rol):
        name = self.user_data["Credenciales"][rol]["Name"]
        email = self.user_data["Credenciales"][rol]["Email"]
        password = self.user_data["Credenciales"][rol]["Password"]

        self.singup_with_credentials(name, email, password)

    @keyword(name='LogIn con email "${email}" y contrasena "${password}"')
    def login_with_credentials(self, email, password):
        # Accedemos al login.
        self.osl.wait_until_element_is_visible(btn_top_login)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_top_login)

        self.osl.wait_until_element_is_visible(cmp_email)
        self.osl.input_text(cmp_email, email)
        self.osl.input_text(cpm_password, password)
        self.osl.capture_page_screenshot()

        # Clickamos logearnos
        self.osl.click_element(btn_submit_login)
        self.osl.wait_until_element_is_visible(img_login)
        self.osl.capture_page_screenshot()

    @keyword(name='LogIn como ${rol}')
    def login_as(self, rol):
        email = self.user_data["Credenciales"][rol]["Email"]
        password = self.user_data["Credenciales"][rol]["Password"]
        self.login_with_credentials(email, password)

    @keyword(name='LogOut')
    def logout(self):
        # Clicamos el logout
        self.osl.wait_until_element_is_visible(btn_top_login, 3)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_top_login)
        self.osl.wait_until_element_is_not_visible(img_login)
        self.osl.capture_page_screenshot()
