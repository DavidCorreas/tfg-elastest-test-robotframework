# ------------------------------- Libraries ------------------------------- #
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'


class WebLogin(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

# TODO: Hacer keywords
