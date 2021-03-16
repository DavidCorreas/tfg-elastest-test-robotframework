from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

btn_laptops = "//a[contains(@id,'Laptop')]"
btn_phones = "//a[contains(@id,'Phones')]"
btn_accesories = "//a[contains(@id,'Accessories')]"
btn_favs = "//a[contains(@href,'Favorites')]"
btn_home = "//a[contains(@href,'Home')]"

title_laptops = "//div[@id='Title'][text()='Laptops']"
title_phones = "//div[@id='Title'][text()='Phones']"
title_accessories = "//div[@id='Title'][text()='Accessories']"
title_favs = "//div[@id='Title'][text()='Favorites']"


class WebHome(PageObject):

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Ir a la página')
    def go_home(self):
        self.go_pages(btn_home, btn_phones)

    @keyword(name='Entrar en la pagina de portatiles')
    def go_laptops(self):
        self.go_pages(btn_laptops, title_laptops)

    @keyword(name='Entrar en la pagina de móviles')
    def go_mob(self):
        self.go_pages(btn_phones, title_phones)

    @keyword(name='Entrar en la pagina de accesorios')
    def go_accessories(self):
        self.go_pages(btn_accesories, title_accessories)

    @keyword(name='Entrar en la pagina de favoritos')
    def go_favs(self):
        self.go_pages(btn_favs, title_favs)


