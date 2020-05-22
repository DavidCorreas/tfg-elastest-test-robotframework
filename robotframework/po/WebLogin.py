# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class WebLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('OutSystemsWeb')

        self._loc_user = "pid=UsernameTxt"
        self._loc_password = "pid=PassTxt"
        self._loc_button_accept = "pid=AccessBtn"
        self._loc_link_logout = "pid=icon-offFormBtn"

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Logarse como ${role}')
    def login_as(self, role):
        # Recupera el usuario y la password en funcion del rol
        # Abre el fichero en funcion del pais
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(
                current_path + "/../data/" + self._get_cod_pais() + '/Users.json') as user_file:
            user_data = json.load(user_file)

        # Lee el usuario y la password
        self.insert_user(user_data["Credenciales"][role]["User"])
        self.insert_password(user_data["Credenciales"][role]["Password"])
        self.click_accept_button()
        self.val_logged()

    @keyword(name='Deslogarse')
    def logout(self):
        self.click_logout()
        self.val_not_logged()

    # ------------------------------- Aux Functions ------------------------------- #
    # Actions
    def insert_user(self, user):
        self.osl.input_text(self._loc_user, user)

    def insert_password(self, password):
        self.osl.input_password(self._loc_password, password)

    def click_accept_button(self):
        self.osl.click_button(self._loc_button_accept)

    def click_logout(self):
        self.osl.wait_until_element_is_visible(self._loc_link_logout, 60)
        BuiltIn().wait_until_keyword_succeeds("5 sec", "200ms", "Click Element",
                                              self._loc_link_logout)

    # Validations
    def val_logged(self):
        self.osl.wait_until_element_is_visible(self._loc_link_logout, 60)

    def val_not_logged(self):
        self.osl.wait_until_element_is_not_visible(self._loc_link_logout, 60)
