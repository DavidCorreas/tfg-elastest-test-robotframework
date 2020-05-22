"""PO Login

Este Page Object encapsula la funcionalidad del Login
"""
# Import libraries
import os
from robot.libraries.BuiltIn import BuiltIn


class PageObject:

    COD_PAIS = "es"
    ENVIRONMENT = "PRE_QA"
    REMOTE_URL_MOB = "http://127.0.0.1:4723/wd/hub"
    REMOTE_URL = "http://esdc1csdla112.emea.prosegur.local:4444/wd/hub"
    BROWSER = "gc"
    IS_REMOTE = False
    RESOLUTION = "FHD"

    def __init__(self, library):

        # variables
        BuiltIn().import_library(library)
        self.osl = BuiltIn().get_library_instance(library)

        # Variables por defecto
        if self._get_browser() is None:
            BuiltIn().set_suite_variable("${browser}", self.BROWSER)
        if self._get_cod_pais() is None:
            BuiltIn().set_suite_variable("${cod_pais}", self.COD_PAIS)
        if self._get_environment() is None:
            BuiltIn().set_suite_variable("${environment}", self.ENVIRONMENT)
        if self._get_is_remote() is None:
            BuiltIn().set_suite_variable("${is_remote}", self.IS_REMOTE)
        if self._get_remote_url() is None:
            BuiltIn().set_suite_variable("${remote_url}", self.REMOTE_URL)
        if self._get_resolution() is None:
            BuiltIn().set_suite_variable("${resolution}", self.RESOLUTION)
        if self._get_remote_url_mob() is None:
            BuiltIn().set_suite_variable("${remote_url_mob}", self.REMOTE_URL_MOB)

        current_path = os.path.dirname(os.path.realpath(__file__))
        current_path = os.path.join(current_path, "../..", "data", "ReferenceData.py")
        current_path = current_path.replace('\\', '/')
        BuiltIn().import_variables(current_path)

    @staticmethod
    def _get_cod_pais():
        return BuiltIn().get_variable_value("${cod_pais}")

    @staticmethod
    def _get_browser():
        return BuiltIn().get_variable_value("${browser}")

    @staticmethod
    def _get_environment():
        return BuiltIn().get_variable_value("${environment}")

    @staticmethod
    def _get_resolution():
        return BuiltIn().get_variable_value("${resolution}")

    @staticmethod
    def _get_is_remote():
        return BuiltIn().get_variable_value("${is_remote}")

    @staticmethod
    def _get_remote_url():
        return BuiltIn().get_variable_value("${remote_url}")

    @staticmethod
    def _get_remote_url_mob():
        return BuiltIn().get_variable_value("${remote_url_mob}")
