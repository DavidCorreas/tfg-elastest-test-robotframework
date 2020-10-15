# ------------------------------- Libraries ------------------------------- #
import json
import os

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class MobApplication(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Config ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Abrir aplicacion movil en ${platform}')
    def open_application(self, platform):
        # Obtener la plataforma para todo el test
        BuiltIn().set_test_variable("${platform}", platform)

        # Recuperar la url en base al entorno
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + '/../data/MobCapabilities.json') as caps:
            capabilities = json.load(caps)

        self.osl.open_application(
            remote_url=self._get_remote_url_mob(), deviceName="emulator-5554",
            platformName=capabilities[platform]["platformName"], app=capabilities[platform]["app"],
            noReset=True, disableWindowAnimation=True, nativeWebScreenshot=True,
            androidScreenshotPath='results/screenshots',
            automationName=capabilities[platform]["automationName"], newCommandTimeout=60000, appWaitDuration=30000, autoGrantPermissions=True)

        self.osl.switch_to_context(self.osl.get_contexts()[1])

    @keyword(name='Cerrar Aplicacion movil')
    def close_application(self):
        self.osl.quit_application()

    @keyword(name='Cerrar Aplicacion Y Sesion Appium')
    def close_session(self):
        self.osl.close_application()

    @keyword(name='Capturar Pantallazo movil')
    def capture_page_screenshot(self):
        self.osl.capture_page_screenshot()
