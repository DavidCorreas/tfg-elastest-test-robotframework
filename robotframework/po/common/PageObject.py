"""PO Login

Este Page Object encapsula la funcionalidad del Login
"""
# Import libraries
import os
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

