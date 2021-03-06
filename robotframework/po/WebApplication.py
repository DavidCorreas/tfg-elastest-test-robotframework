# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class WebApplication(PageObject):

    # ------------------------------- Config ------------------------------- #
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        # Library Load
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Abrir aplicacion')
    def open_application(self):
        # Recuperar la url en base al entorno
        current_path = os.path.dirname(os.path.abspath(__file__))

        # Obtener variables del json
        enviroment_path = current_path + "/../data/" + self._get_cod_pais() + '/Environment.json'
        with open(enviroment_path) as environment_file:
            environment_data = json.load(environment_file)
        url = environment_data["Environments"][self._get_environment()]["Url"]

        # Configurar navegador si es remoto (para elastest)
        BuiltIn().log("ES REMOTO:")
        BuiltIn().log(self._get_is_remote())

        if self._get_is_remote() == "True":
            suite_name = BuiltIn().get_variable_value("${SUITE_NAME}")
            test_name = BuiltIn().get_variable_value("${TEST_NAME}")

            # Resolucion (FHD por defecto)
            resolution = "1920x1080x24"
            if self._get_resolution() == 'HD':
                resolution = "1280x720x24"

            # Capabilities elastest
            # capabilities = {
            #     "live": True,
            #     "enableLog": True,
            #     "screenResolution": resolution,
            #     "name": suite_name + "." + test_name,
            #     "chromeOptions": {
            #         "args": ["live=true", "elastestTimeout=0"]
            #     }
            # }

            # Capabilities selenoid
            capabilities = {
                "enableVNC": True,
                "browserName": self._get_browser(),
                "version": self._get_version(),
                "enableVideo": False,
                "enableLog": True,
                "screenResolution": resolution,
                "name": suite_name + "." + test_name
            }

            self.osl.open_browser(url,
                                  self._get_browser(),
                                  remote_url=self._get_remote_url(),
                                  desired_capabilities=capabilities)

        # Abrir navegador si no es remoto (IS_REMOTE=False)
        else:
            self.osl.open_browser(url, self._get_browser())

        self.osl.maximize_browser_window()

    @keyword(name='Cerrar Aplicacion')
    def close_application(self):
        self.osl.close_all_browsers()

    @keyword(name='Capturar Pantallazo')
    def capture_page_screenshot(self):
        self.osl.capture_page_screenshot()
