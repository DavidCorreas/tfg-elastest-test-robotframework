import json
import os

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Login
btn_top_login = "//a[@href='/auth/login']"
cmp_email = "//input[@name='email']"
cpm_password = "//input[@name='password']"
btn_submit_login = "//button[@type='submit']"

# SingUp
btn_top_singup = "//a[@href='/auth/singup']"
btn_submit_singup = "//button[@type='submit']"
dialog_error = "//mat-dialog-container"
btn_accept_error = dialog_error + "//button"

# Logout
btn_logout = "//button/*[text()='LogOut']"

# Pagina posts
list_posts = "//app-post-list"


class WebLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')
        current_path = os.path.dirname(os.path.abspath(__file__))
        file_name = current_path + "/../data/" + self._get_cod_pais() + '/Users.json'
        with open(file_name) as user_file:
            self.user_data = json.load(user_file)

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Registrarse con email ${email} y contrasena ${password}')
    def singup_with_credentials(self, email, password):
        # Accedemos a la pagina para registrarnos
        self.osl.wait_until_element_is_visible(btn_top_singup)
        self.osl.click_element(btn_top_singup)
        self.osl.wait_until_element_is_visible(cmp_email)
        
        # Introducimos credenciales
        self.osl.input_text(cmp_email, email)
        self.osl.input_text(cpm_password, password)

        # Clickamos para registrarnos
        self.osl.click_element(btn_submit_singup)
        self.osl.wait_until_element_is_visible(list_posts)

    @keyword(name='Registrarse como ${rol}')
    def sing_up(self, rol):
        email = self.user_data["Credenciales"][rol]["Email"]
        password = self.user_data["Credenciales"][rol]["Password"]
        self.singup_with_credentials(email, password)

    @keyword(name='Registrar a ${rol} si no existe')
    def sing_up_if_not_exists(self, rol):
        BuiltIn().run_keyword_and_ignore_error('Registrarse como ' + rol)
        try:
            self._accept_error()
        except Exception as e:
            print(e)

    @keyword(name='Intentar volver a registrarse como ${rol}')
    def try_login(self, rol):
        # Intentamos logarnos, pero falla
        BuiltIn().run_keyword_and_ignore_error('Registrarse como ' + rol)
        try:
            self._accept_error()
        except Exception as e:
            print(e)

    @keyword(name='Logarse con email ${email} y contrasena ${password}')
    def login_with_credentials(self, email, password):
        # Accedemos al login.
        self.osl.wait_until_element_is_visible(btn_top_login)
        self.osl.click_element(btn_top_login)
        self.osl.wait_until_element_is_visible(cmp_email)
        
        # Introducimos credenciales
        self.osl.input_text(cmp_email, email)
        self.osl.input_text(cpm_password, password)

        # Clickamos logearnos
        self.osl.click_element(btn_submit_login)
        self.osl.wait_until_element_is_visible(list_posts)

    @keyword(name='Logarse como ${rol}')
    def login_as(self, rol):
        email = self.user_data["Credenciales"][rol]["Email"]
        password = self.user_data["Credenciales"][rol]["Password"]
        self.login_with_credentials(email, password)

    @keyword(name='Deslogarse')
    def logout(self):
        # Clicamos el logout
        self.osl.wait_until_element_is_visible(btn_logout)
        self.osl.click_element(btn_logout)
        self.osl.wait_until_element_is_visible(btn_top_login)

    @keyword(name='Intentar Deslogarse')
    def try_logout(self):
        BuiltIn().run_keyword_and_ignore_error("Deslogarse")

    def _accept_error(self):
        # Aceptamos el error
        self.osl.wait_until_element_is_visible(dialog_error)
        self.osl.click_element(btn_accept_error)

