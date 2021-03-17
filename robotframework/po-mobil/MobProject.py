from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

# Projects
btn_new_project = "//*[@id='Link_NewProject']"
btn_bottom_project = "//a[contains(@href,'Projects')]"
header_project = "//h1//span[text()='Projects']"
cmp_name = "//input[contains(@id,'Input_Name')]"
btn_add = "//button[@type='submit']"

btn_back = "//*[@id='Link_PreviousScreen']"
chk_task_name = "//div[@data-block='MainFlow.Task_ListItem'][.//*[text()='{}']]//input"

# List projectos
item_project = "//div[contains(@id,'Project_ListItem')]//*[text()='{}']"
title_project = "//div[@id='ProjectName']/*[text()='{}']"

# New task
btn_new_task = "//button[contains(@id,'AddTask')]"
fch_date = "//input[contains(@id,'Input_DueDate')]"


class MobProject(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('AppiumLibrary')

    # ------------------------------- Keywords ------------------------------- #

    @keyword(name='Ir a la página')
    def go_page(self):
        self.osl.wait_until_element_is_visible(btn_bottom_project)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_bottom_project)
        self.osl.wait_until_element_is_visible(header_project)

    @keyword(name='Crear proyecto con nombre "${project}"')
    def login_with_credentials(self, project):
        self.osl.wait_until_element_is_visible(btn_new_project)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_new_project)
        self.osl.wait_until_element_is_visible(cmp_name)
        self.osl.input_text(cmp_name, project)
        self.osl.capture_page_screenshot()
        self.osl.wait_until_element_is_visible(btn_add)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_add)
        self._ps_emergent_msg_check_mobile()

    @keyword(name='Entrar en el proyecto "${project}"')
    def go_project(self, project):
        item_project_name = item_project.format(project)
        self.osl.wait_until_element_is_visible(item_project_name)
        self.osl.capture_page_screenshot()
        self.osl.click_element(item_project_name)

    @keyword(name='DetalleProyecto.Crear tarea en proyecto vacio con nombre "${name}" y fecha "${date}"')
    def new_task(self, name, date):
        self.osl.wait_until_element_is_visible(btn_new_task)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_new_task)
        self.osl.wait_until_element_is_visible(cmp_name)
        self.osl.input_text(cmp_name, name)
        self._ps_android_set_date(fch_date, date)
        self.osl.wait_until_element_is_visible(btn_add)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_add)
        self._ps_emergent_msg_check_mobile()

    @keyword(name='DetalleProyecto.Volver a proyectos')
    def return_project(self):
        self.osl.wait_until_element_is_visible(btn_back)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_back)
        self.osl.wait_until_element_is_visible(header_project)

    @keyword(name='DetalleProyecto.Marcar "${nombre_tarea}" como completado')
    def check_task(self, nombre_tarea):
        checkbox = chk_task_name.format(nombre_tarea)
        self.osl.wait_until_element_is_visible(checkbox)
        self.osl.capture_page_screenshot()
        self.osl.click_element(checkbox)
        self.osl.wait_until_element_is_visible(checkbox + "[@checked]")
        self._ps_emergent_msg_check_mobile()
