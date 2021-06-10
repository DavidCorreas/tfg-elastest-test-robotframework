import json
import os

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Login
cmp_email = "//*[@id='Input_UsernameVal']"
cpm_password = "//*[@id='Input_PasswordVal']"
btn_submit_login = "//button[@type='submit']"
btn_new_task = "//*[@id='Link_NewTask']"

# Logout
btn_profile = "//a[contains(@href,'Profile')]"
btn_logout = "//a[text()='Log out']"
btn_logout_confirm = "//span[contains(@class,'link-delete')]"


class MobLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    @property
    def user_data(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = current_path + "/../data/" + self._get_cod_pais + '/Users.json'
        with open(file_name) as user_file:
            return json.load(user_file)

    # ------------------------------- Keywords ------------------------------- #

    @keyword(name='LogIn con usuario "${user}" y contrasena "${password}"')
    def login_with_credentials(self, user, password):
        self.osl.wait_until_element_is_visible(cmp_email)
        self.osl.input_text(cmp_email, user)
        self.osl.input_text(cpm_password, password)
        self.osl.capture_page_screenshot()

        # Clickamos logearnos
        BuiltIn().wait_until_keyword_succeeds(5, 0.2, "Wait Until Element Is Visible", btn_submit_login)
        BuiltIn().wait_until_keyword_succeeds(5, 0.2, "Click Element", btn_submit_login)
        BuiltIn().wait_until_keyword_succeeds(5, 0.2, "Wait Until Element Is Visible", btn_profile)
        BuiltIn().wait_until_keyword_succeeds(5, 0.2, "Capture Page Screenshot")

    @keyword(name='LogIn como ${rol}')
    def login_as(self, rol):
        email = self.user_data["Credenciales"][rol]["Email"]
        password = self.user_data["Credenciales"][rol]["Password"]
        self.login_with_credentials(email, password)

    @keyword(name='LogIn como Patricia Wesley')
    def login_as(self):
        pass

    @keyword(name='LogOut')
    def logout(self):
        # Clicamos el logout
        self.osl.wait_until_element_is_visible(btn_profile)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_profile)
        self.osl.wait_until_element_is_visible(btn_logout)
        self.osl.click_element(btn_logout)
        self.osl.wait_until_element_is_visible(btn_logout_confirm)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_logout_confirm)
        self.osl.wait_until_element_is_visible(cmp_email)
        self.osl.capture_page_screenshot()
