# ------------------------------- Libraries ------------------------------- #
import json
import os
import base64

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# TopBar
btn_messages = "//a[@routerlink='/']"

# Card
btn_card_title = "//mat-expansion-panel-header[span[contains(text(),'{}')]]"
img_card = "//img[contains(@src,'{}')]"
cmp_card_content = "//p[contains(text(),'{}')]"
btn_card_edit = "//mat-expansion-panel[." + btn_card_title + "]//a"
btn_card_delete = "//mat-expansion-panel[." + btn_card_title + "]//button"


# Selector paginado
btn_selector = "//mat-select"
btn_selector_option = "//mat-option[@ng-reflect-value='{}']"

class MobList(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Comprobar que existe post con titulo "${title}", con imagen y contenido "${content}"')
    def check_post(self, title, content):
        loc_title = btn_card_title.format(title)
        loc_image = img_card.format(title.lower())
        loc_content = cmp_card_content.format(content)
        loc_edit = btn_card_edit.format(title)

        # Comprobamos que este la tarjeta
        self.osl.wait_until_element_is_visible(loc_title)

        # Vemos si ya esta abierta y comprobamso que exista la imagen
        try:
            self.osl.wait_until_element_is_visible(loc_image)
        except:
            self.osl.click_element(loc_title)
            self.osl.wait_until_element_is_visible(loc_image)
        
        self.osl.capture_page_screenshot()
        self.osl.wait_until_element_is_visible(loc_content)

    @keyword(name='Comprobar eliminacion del post con titulo ${title}')
    def check_delete(self, title):
        BuiltIn().run_keyword_and_expect_error('*', 'Comprobar que existe post con titulo "{}", con imagen y contenido "_"'.format(title))
        
    @keyword(name='Editar post ${title}')
    def edit_card(self, title):
        # Tiene que estar la carta abierta (usar keyword "Comprobar que existe post...")
        loc_edit = btn_card_edit.format(title)
        self.osl.wait_until_element_is_visible(loc_edit)
        self.osl.click_element(loc_edit)

    @keyword(name='Eliminar post ${title}')
    def delete_post(self, title):
        loc_delete = btn_card_delete.format(title)
        self.osl.wait_until_element_is_visible(loc_delete)
        self.osl.click_element(loc_delete)

    @keyword(name='Poner paginado en ${num}')
    def items_per_page(self, num):
        loc_option = btn_selector_option.format(num)
        self.osl.wait_until_element_is_visible(btn_selector)
        self.osl.click_element(btn_selector)
        self.osl.wait_until_element_is_visible(loc_option)
        self.osl.click_element(loc_option)
       