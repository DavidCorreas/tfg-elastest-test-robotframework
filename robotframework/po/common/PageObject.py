"""PO Login

Este Page Object encapsula la funcionalidad del Login
"""
# Import libraries
import os
from datetime import datetime

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import not_keyword


class PageObject:

    COD_PAIS = "es"
    ENVIRONMENT = "DEV"
    BROWSER = "chrome"
    VERSION = "85.0"
    IS_REMOTE = False
    RESOLUTION = "FHD"
    # Endpoint selenium hub
    REMOTE_URL_MOB = "http://localhost:4444/wd/hub"
    LOCAL_URL_MOB = "http://localhost:4723/wd/hub"
    # Endpoint selenoid
    REMOTE_URL = "http://localhost:4445/wd/hub"

    def __init__(self, library):
        self.library = library

    @not_keyword
    def _go_pages(self, loc_btn, loc_wait):
        self.osl.wait_until_page_contains_element(loc_btn)
        self.osl.scroll_element_into_view(loc_btn)
        self.osl.capture_page_screenshot()
        self.osl.click_element(loc_btn)
        self.osl.wait_until_page_contains_element(loc_wait)
        self.osl.capture_page_screenshot()

    @property
    def osl(self):
        BuiltIn().import_library(self.library)
        osl = BuiltIn().get_library_instance(self.library)
        if self.library == 'SeleniumLibrary':
            osl.set_selenium_timeout(15)
        if self.library == 'AppiumLibrary':
            osl.set_appium_timeout(15)

        current_path = os.path.dirname(os.path.realpath(__file__))
        current_path = os.path.join(current_path, "../..", "data", "ReferenceData.py")
        current_path = current_path.replace('\\', '/')
        BuiltIn().import_variables(current_path)

        return osl

    @property
    def _get_cod_pais(self):
        cod_pais = BuiltIn().get_variable_value("${cod_pais}")
        if cod_pais is None:
            cod_pais = self.COD_PAIS
        return cod_pais

    @property
    def _get_browser(self):
        browser = BuiltIn().get_variable_value("${browser}")
        if browser is None:
            browser = self.BROWSER
        return browser

    @property
    def _get_version(self):
        version = BuiltIn().get_variable_value("${version}")
        if version is None:
            version = self.VERSION
        return version

    @property
    def _get_environment(self):
        environment = BuiltIn().get_variable_value("${environment}")
        if environment is None:
            environment = self.ENVIRONMENT
        return environment

    @property
    def _get_resolution(self):
        resolution = BuiltIn().get_variable_value("${resolution}")
        if resolution is None:
            resolution = self.RESOLUTION
        return resolution

    @property
    def _get_is_remote(self):
        is_remote = BuiltIn().get_variable_value("${is_remote}")
        if is_remote is None:
            is_remote = self.IS_REMOTE
        return is_remote

    @property
    def _get_remote_url(self):
        remote_url = BuiltIn().get_variable_value("${remote_url}")
        if remote_url is None:
            remote_url = self.REMOTE_URL
        return remote_url

    @property
    def _get_remote_url_mob(self):
        remote_url_mob = BuiltIn().get_variable_value("${remote_url_mob}")
        if remote_url_mob is None:
            remote_url_mob = self.REMOTE_URL_MOB
        return remote_url_mob

    @property
    def _get_local_url_mob(self):
        local_url_mob = BuiltIn().get_variable_value("${local_url_mob}")
        if local_url_mob is None:
            local_url_mob = self.LOCAL_URL_MOB
        return local_url_mob

    @not_keyword
    def _ps_android_set_date(self, locator, date):
        """
        Selecciona la fecha indicada, interactuando con el widget de android para establecer una fecha.

        :param locator: Localizador del elemento del cual clickando, sale el widget de la fecha
        :param date: Dia en tipo datetime o string con formato %d-%m-%Y
        """
        month_dict = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                      'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11,
                      'December': 12}
        dt_date = date if not isinstance(date, str) else datetime.strptime(date, '%d-%m-%Y')
        year = dt_date.year
        month = dt_date.month
        day = dt_date.day

        btn_year = "//android.widget.TextView[contains(@resource-id,'date_picker_header_year')]"
        item_year = \
            "//android.widget.TextView[@text='" + str(year) + "'][contains(@resource-id,'text1')]"
        item_first_day = "//android.view.View[contains(@text,'10')]"
        btn_right = "//android.widget.ImageButton[@resource-id='android:id/next']"
        btn_left = "//android.widget.ImageButton[@resource-id='android:id/prev']"
        btn_set = "//android.widget.Button[@resource-id='android:id/button1']"

        self.osl.wait_until_element_is_visible(locator)
        self.osl.click_element(locator)

        ""
        "Cambiamos El contexto para que funcione con el nativo"
        self.osl.switch_to_context(self.osl.get_contexts()[0])
        # Seleccionar ano
        self.osl.wait_until_element_is_visible(btn_year)
        self.osl.click_element(btn_year)
        self.osl.wait_until_element_is_visible(item_year)
        self.osl.click_element(item_year)

        # Seleccionar mes con minimo numero de clicks
        str_current_date = self.osl.get_element_attribute(item_first_day, "content-desc")
        current_month = month_dict[str_current_date.split()[1]]

        months_right = {((x + current_month) % 12) if ((x + current_month) % 12) != 0 else 12 for x
                        in range(1, 6)}
        if month in months_right:
            abs_month = month if current_month <= month else month + 12
            num_clicks = abs_month - current_month
            for x in range(num_clicks):
                self.osl.click_element(btn_right)
        else:
            abs_current_month = current_month if current_month >= month else current_month + 12
            num_clicks = abs_current_month - month
            for x in range(num_clicks):
                self.osl.click_element(btn_left)

        # Seleccionar dia
        _date = str(day) + " " + list(month_dict.keys())[list(month_dict.values()).index(month)]
        loc_date = "//android.view.View[contains(@content-desc,'" + _date + "')]"

        self.osl.wait_until_element_is_visible(loc_date)
        self.osl.click_element(loc_date)

        self.osl.click_element(btn_set)
        self.osl.wait_until_page_does_not_contain_element(btn_set)

        self.osl.switch_to_context(self.osl.get_contexts()[1])

    @not_keyword
    def _ps_emergent_msg_check_mobile(self, msg_type='SUCCESS', timeout=None):
        """Valida la existencia del mensaje, y lo cierra.

        Por defecto se espera un mensaje de tipo Success sin validar el contenido del texto.
        Este KeyWord soporta los siguientes tipos de mensaje ``msg_type``:

        - ``SUCCESS``: Mensaje de color Verde que indica que las operaciones se han realizado.
        - ``WARNING``: Mensaje de color Amarillo que indica alguna alerta o error controlado del sistema.
        - ``INFO``: Mensaje de color Azul que indica informacion del sistema.
        - ``ERROR``: Mensaje de color Rojo que indica un error grave.

        Examples:
        | PS Emergent Msg Check |                |   # Accepta un mensaje de tipo SUCCESS.  |
        | PS Emergent Msg Check | WARNING        |   # Acepta el mensaje de tipo WARNING. |
        | PS Emergent Msg Check | INFO           |   # Acepta el mensaje de tipo INFO con el texto indicado.  |

        Funcionalidad especifica del Framework de Prosegur.
        """

        map = {
            'SUCCESS': 'feedback-message-success',
            'WARNING': 'feedback-message-warning',
            'INFO': 'feedback-message-info',
            'ERROR': 'feedback-message-error',
            'RELEASE': '//*[@resource-id="feedbackMessageContainer"]'
        }

        locator = "//*[contains(@class,'" + map[msg_type] + "')]"
        loc_msg_close = locator + "/i"
        if msg_type == 'RELEASE':
            locator = map[msg_type]
            loc_msg_close = locator + "/*"

        old_timeout = None
        BuiltIn().log_to_console("Esperando que salga un mensaje del tipo " + msg_type + "\n")

        if timeout is not None:
            old_timeout = self.osl.set_appium_timeout(timeout)

        # Espera a que finalice la animacion
        self.osl.wait_until_element_is_visible(locator)

        # Cierra el mensaje emergente
        BuiltIn().wait_until_keyword_succeeds(self.osl.get_appium_timeout(), 0.2,
                                              'Click Element', loc_msg_close)

        if timeout is not None:
            self.osl.set_appium_timeout(old_timeout)
