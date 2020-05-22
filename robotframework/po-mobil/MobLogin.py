# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class MobLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        PageObject.__init__(self, 'OutSystemsMobile')

        self._input_user = "//*[@resource-id='Input_UsernameVal']"
        self._input_password = "//*[@resource-id='Input_PasswordVal']"
        self._start_session_btn = "//android.widget.Button[2]"
        self._logout_button = "//*[contains(@resource-id,'LoginInfo')]"
        self._hamburger_button = "//*[contains(@resource-id,'Menu')]"

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Logarse como ${rol}')
    def login_as(self, rol):
        # Recupera el usuario y la password
        # Abre el fichero en funcion del pais
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = current_path + "/../data/" + self._get_cod_pais() + '/Users.json'
        with open(file_name) as user_file:
            user_data = json.load(user_file)

        # lee el usuario y la password
        self.insert_user(user_data["Credenciales"][rol]["User"])
        self.insert_password(user_data["Credenciales"][rol]["Password"])
        self.click_accept_button()
        self.val_logged()

    @keyword(name='Deslogarse')
    def logout(self):
        self.click_logout()
        self.val_not_logged()

    # ------------------------------- Aux Functions ------------------------------- #
    def val_logged(self):
        self.osl.wait_until_element_is_visible(self._hamburger_button, 20)

    def val_not_logged(self):
        self.osl.wait_until_page_contains_element(self._input_user, 20)

    def insert_user(self, user):
        self.osl.wait_until_element_is_visible(self._input_user, 45)
        self.osl.clear_text(self._input_user)
        self.osl.input_text(self._input_user, user)

    def insert_password(self, password):
        self.osl.wait_until_element_is_visible(self._input_password)
        self.osl.clear_text(self._input_password)
        self.osl.input_password(self._input_password, password)

    def click_accept_button(self):
        self.osl.wait_until_element_is_visible(self._start_session_btn)
        self.osl.click_element(self._start_session_btn)

    def click_logout(self):
        osl = self.osl
        osl.wait_until_element_is_visible(self._hamburger_button)
        osl.click_element(self._hamburger_button)
        osl.wait_until_element_is_visible(self._logout_button)
        osl.click_element(self._logout_button)
