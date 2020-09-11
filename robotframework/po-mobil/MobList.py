# ------------------------------- Libraries ------------------------------- #
import json
import os
import base64

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Lista
btn_card_title = "//mat-expansion-panel-header[span[contains(text(),'{}')]]"


class MobList(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Comprobar que existe post con titulo "${title}", imagen "${image} y contenido ${content}"')
    def access_new_post(self, title, image, content):
       