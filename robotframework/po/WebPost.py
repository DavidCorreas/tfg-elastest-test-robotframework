# ------------------------------- Libraries ------------------------------- #
import os

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Crear post
btn_new_post = "//a[@routerlink='/create']"
btn_new_post_accent = btn_new_post +  "[contains(@class,'mat-accent')]"
btn_new_post_unselected = btn_new_post + "[not(contains(@class,'mat-accent'))]"
cpm_post_title = "//input[@type='text']"
btn_pick_image = "//input[@type='file']"
cmp_post_content = "//textarea"
btn_save_post = "//button[@type='submit']"


class WebPost(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Acceder a la creacion de un post')
    def access_new_post(self):
        # Accedemos a la pagina para crear un post
        self.osl.wait_until_element_is_visible(btn_new_post)
        self.osl.click_element(btn_new_post)
        self.osl.wait_until_element_is_visible(btn_new_post_accent)

    @keyword(name='Introducir titulo ${title}')
    def put_title(self, title):
        # Introducimos el titulo
        self.osl.wait_until_element_is_visible(cpm_post_title)
        self.osl.clear_element_text(cpm_post_title)
        self.osl.input_text(cpm_post_title, title)
    
    @keyword(name='Introducir contenido "${content}"')
    def put_content(self, content):
        # Introducimos el titulo
        self.osl.wait_until_element_is_visible(cmp_post_content)
        self.osl.clear_element_text(cmp_post_content)
        self.osl.input_text(cmp_post_content, content)

    @keyword(name='Introducir imagen ${image}')
    def put_image(self, image):
        # Obtenemos path de la imagen
        current_path = os.path.dirname(os.path.abspath(__file__))
        image_path = current_path + '/../data/fake-files/{}'.format(image)
        BuiltIn().import_library('OperatingSystem')
        operating_system = BuiltIn().get_library_instance("OperatingSystem")
        normalized_img_path = operating_system.normalize_path(image_path)

        # Introducimos imagen
        self.osl.wait_until_page_contains_element(btn_pick_image)
        self.osl.choose_file(btn_pick_image, normalized_img_path)

        # Esperamos a que aparezca la imagen
        self.osl.wait_until_element_is_visible("//img")

    @keyword(name='Guardar post')
    def save_post(self):
        self.osl.wait_until_element_is_visible(btn_save_post)
        self.osl.click_element(btn_save_post)
        self.osl.wait_until_element_is_visible(btn_new_post_unselected)
        