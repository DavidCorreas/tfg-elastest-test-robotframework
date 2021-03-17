from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# New Task
btn_new_task = "//*[@id='Link_NewTask']"
cmp_name = "//input[contains(@id,'Input_Name')]"
fch_date = "//input[contains(@id,'Input_DueDate')]"
btn_add = "//button[@type='submit']"

btn_bottom_task = "//a[contains(@href,'Tasks')]"
header_task = "//h1//span[text()='Tasks']"
btn_tab_name = "//div[@role='tab'][text()='{}']"
task_item_name = "//div[contains(@id,'LinkToTask')]//*[text()='{}']"
btn_icon_trash = "//a[./i[contains(@class,'trash')]]"
btn_confirm_delete = "//div[./span[contains(@class,'link-delete')]]"


class MobTask(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Ir a la página')
    def go_page(self):
        self.osl.wait_until_element_is_visible(btn_bottom_task)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_bottom_task)
        self.osl.wait_until_element_is_visible(header_task)

    @keyword(name='Ir a la pestaña "${nombre_pestana}"')
    def go_tab(self, nombre_pestana):
        tab = btn_tab_name.format(nombre_pestana)
        self.osl.wait_until_element_is_visible(tab)
        self.osl.capture_page_screenshot()
        self.osl.click_element(tab)
        self.osl.wait_until_element_is_visible(tab + "[contains(@class,'active')]")

    @keyword(name='Seleccionar tarea con nombre "${nombre_tarea}"')
    def go_task(self, nombre_tarea):
        item = task_item_name.format(nombre_tarea)
        self.osl.wait_until_element_is_visible(item)
        self.osl.capture_page_screenshot()
        self.osl.click_element(item)
        self.osl.wait_until_element_is_visible(btn_icon_trash)
        self.osl.capture_page_screenshot()

    @keyword(name='DetalleTarea.Borrar tarea')
    def delete_task(self):
        self.osl.wait_until_element_is_visible(btn_icon_trash)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_icon_trash)
        self.osl.wait_until_element_is_visible(btn_confirm_delete)
        self.osl.click_element(btn_confirm_delete)
        self._ps_emergent_msg_check_mobile()

    @keyword(name='Crear tarea con nombre "${name}", dia "${day}"')
    def login_with_credentials(self, name, day):
        self.osl.wait_until_element_is_visible(btn_new_task)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_new_task)
        self.osl.wait_until_element_is_visible(cmp_name)
        self.osl.input_text(cmp_name, name)
        self.osl.capture_page_screenshot()
        self._ps_android_set_date(fch_date, day)
        self.osl.wait_until_element_is_visible(btn_add)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_add)
        self._ps_emergent_msg_check_mobile()
