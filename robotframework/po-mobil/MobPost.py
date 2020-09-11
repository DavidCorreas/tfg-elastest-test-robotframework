# ------------------------------- Libraries ------------------------------- #
import json
import os
import base64

from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Crear post
btn_new_post = "//a[@routerlink='/create']"
btn_new_post_accent = btn_new_post +  "[contains(@class,'cdk-focused')]"
btn_new_post_unselected = btn_new_post + "[not(contains(@class,'cdk-focused'))]"
cpm_post_title = "//input[@type='text']"
btn_pick_image = "//button[@type='button']"
cmp_post_content = "//textarea"
btn_save_post = "//button[@type='submit']"

# Seleccionar fichero
btn_hamburguesa = '//android.widget.ImageButton[@content-desc="Show roots"]'
btn_downloads = "//android.widget.ListView//android.widget.TextView[@text='Downloads']"
btn_imagen = "//android.widget.RelativeLayout[.//android.widget.TextView[@text='{}']]"


class MobPost(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

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
        self.osl.input_text(cpm_post_title, title)
    
    @keyword(name='Introducir contenido "${content}"')
    def put_content(self, content):
        # Introducimos el titulo
        self.osl.wait_until_element_is_visible(cmp_post_content)
        self.osl.input_text(cmp_post_content, content)

    @keyword(name='Introducir imagen ${image}')
    def put_image(self, image):
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + '/../data/MobCapabilities.json') as caps:
            capabilities = json.load(caps)

        # Introducimos imagen
        self.osl.wait_until_element_is_visible(btn_pick_image)
        self.osl.click_element(btn_pick_image)
        self._push_file(image)
        platform = BuiltIn().get_variable_value("${platform}")
        if capabilities[platform]["platformName"].lower() == 'android':
            self._choose_file_android(image)

        # Esperamos a que aparezca la imagen
        self.osl.wait_until_element_is_visible("//img")

    @keyword(name='Guardar post')
    def save_post(self):
        self.osl.wait_until_element_is_visible(btn_save_post)
        self.osl.click_element(btn_save_post)
        self.osl.wait_until_element_is_visible(btn_new_post_unselected)

    def _choose_file_android(self, image):
        # Cambiamos de contexto a nativo de android
        self.osl.switch_to_context(self.osl.get_contexts()[0])

        # Clicamos en el menu lateral       
        self.osl.wait_until_element_is_visible(btn_hamburguesa)
        self.osl.click_element(btn_hamburguesa)

        # Seleccionamos descargas dentro del dispositivo
        BuiltIn().sleep(2)
        self.osl.capture_page_screenshot()
        self.osl.wait_until_element_is_visible(btn_downloads)
        self.osl.click_element(btn_downloads)

        # Seleccionamos la imagen
        BuiltIn().sleep(2)
        self.osl.capture_page_screenshot()
        locator_image = btn_imagen.format(image)
        self._try_select_image(locator_image)
        # BuiltIn().wait_until_keyword_succeeds(20, 0.2, 'Try Select Image', locator_image)

    def _push_file(self, image):
        current_path = os.path.dirname(os.path.abspath(__file__))
        with open(current_path + '/../data/fake-files/{}'.format(image), mode='rb') as file:
            img = file.read()
            img_serializable = base64.encodebytes(img).decode("utf-8")
            self.osl._current_application().push_file('/sdcard/Download/' + image, img_serializable)
            # self.osl.push_file('/sdcard/Downloads', img_serializable)

    def _try_select_image(self, locator_image):
        self.osl.switch_to_context(self.osl.get_contexts()[0])
        self.osl.wait_until_element_is_visible(locator_image)
        self.osl.click_element(locator_image)
        self.osl.switch_to_context(self.osl.get_contexts()[1])
        self.osl.wait_until_element_is_visible("//img")

        
    