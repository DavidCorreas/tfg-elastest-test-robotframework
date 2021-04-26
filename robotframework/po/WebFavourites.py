from robot.api.deco import keyword
from robot.libraries.BuiltIn import BuiltIn

from robotframework.po.common.PageObject import PageObject

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

btn_favs = "//a[contains(@href,'Favorites')]"
title_favs = "//div[@id='Title'][text()='Favorites']"

cmp_filter = "//input[contains(@id,'Input_Search')]"
btn_lowest = "//button[contains(@id,'LowestPrice')]"
btn_search = "//button[contains(@id,'Button_search')]"
btn_clear = "//a[contains(@id,'Link_Clear')]"
result_with_number = "//div[contains(@id,'ListOfProducts')]/div[{}]"
loc_results_prices = "//div[contains(@id,'ListOfProducts')]/div//span[contains(@id,'CurrentPrice')]"

loc_phone_title = "//div[contains(@id,'Column2')]/span[text()='{}']"
loc_detail_title = "//div[contains(@id,'Column2')]/span"

# Detalles
btn_add_favs = "//button[@id='Button_AddFavorites']"
btn_remove_favs = "//button[@id='Button_RemoveFavorites']"


class WebFavourites(PageObject):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Go to page')
    def go_home(self):
        """
        Navegar a la página de accesorios. Debe de estar visible la pestaña.
        """
        self._go_pages(btn_favs, title_favs)

    @keyword(name='Filtros.Buscar con el texto ${text}')
    def filter_text(self, text):
        """
        En el filtro, busca por el texto pero no le da a buscar (Para buscar: Filtros.Buscar)
        """
        self.osl.wait_until_element_is_visible(cmp_filter)
        self.osl.input_text(cmp_filter, text)

    @keyword(name='Filtros.Precio más alto primero')
    def filter_highest(self):
        """
        En el filtro, clica el botón de 'Highest price' (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filtros.Precio más bajo primero')
    def filter_lowest(self):
        """
        En el filtro, clica el botón de 'Lowest price' (Para buscar: Filtros.Buscar)
        """
        btn_lowest_selected = btn_lowest + "[contains(@class,'selected')]"
        self.osl.wait_until_element_is_visible(btn_lowest)
        try:
            self.osl.wait_until_element_is_visible(btn_lowest_selected,
                                                   timeout=0.5)
        except:
            self.osl.click_element(btn_lowest)
        self.osl.wait_until_element_is_visible(btn_lowest_selected)

        # Pulsar boton buscar
        self.osl.wait_until_element_is_visible(btn_search)
        self.osl.click_element(btn_search)
        self.osl.wait_until_element_is_visible(btn_clear)

        tryes = 5
        while True:
            try:
                prices = [int(float(self.osl.get_text(res).replace("$", ""))) for res in
                          self.osl.get_webelements(loc_results_prices)]
                if all(prices[i] <= prices[i + 1] for i in range(len(prices) - 1)):
                    break
            except Exception as e:
                print(str(e))

            if tryes < 0:
                BuiltIn().fail()
            tryes -= 1
            BuiltIn().sleep(1)

    @keyword(name=
             'Filtros.Mostrar favoritos con precio desde ${precio_bajo} hasta ${precio_alto}')
    def filter_price(self, precio_bajo, precio_alto):
        """
        En el filtro, pone un rango de precios siendo 'precio_bajo' el boton de la izquierda y
        'precio_alto' el boton de la derecha (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filtros.Buscar')
    def filter_search(self):
        """
        Aplica los filtros pulsando el botón filtrar.
        """
        self.osl.wait_until_element_is_visible(btn_search)
        self.osl.click_element(btn_search)
        self.osl.wait_until_element_is_visible(btn_clear)

    @keyword(name='Filtros.Limpiar filtros')
    def filters_clear(self):
        """
        Limpia los filtros pulsando el botón de 'clear'. Solo disponible cuando ya se ha filtrado.
        """
        pass

    @keyword(name='Comprobar que existe favorito con nombre ${nom_fav}')
    def check_name_fav(self, nom_fav):
        pass

    @keyword(name='Check saved favourites')
    def check_favs(self):
        """
        Si la prueba ha agregado a favoritos algún producto, comprueba que exista como favoritos.
        Para ello los busca individualmente y comprueba que estén.
        """
        fav_phone = BuiltIn().get_variable_value("${FAV_PHONE}")
        BuiltIn().log("Telefonos guardados: {}".format(fav_phone), console=True)
        fav_laptop = BuiltIn().get_variable_value("${FAV_LAPTOP}")
        BuiltIn().log("Portátiles guardados: {}".format(fav_laptop), console=True)
        fav_accessorie = BuiltIn().get_variable_value("${FAV_ACCESSORIES}")
        BuiltIn().log("Accesorios guardados: {}".format(fav_accessorie), console=True)

        if fav_phone is not None:
            BuiltIn().log("Comprobando que está el teléfono: '{}'".format(fav_phone), console=True)
            self.filter_text(fav_phone)
            self.filter_search()
            self.osl.wait_until_element_is_visible("//*[text()='{}']".format(fav_phone))
            self.filters_clear()

        if fav_laptop is not None:
            BuiltIn().log("Comprobando que está el portatil: '{}'".format(fav_laptop), console=True)
            self.filter_text(fav_laptop)
            self.filter_search()
            self.osl.wait_until_element_is_visible("//*[text()='{}']".format(fav_laptop))
            self.filters_clear()

        if fav_accessorie is not None:
            BuiltIn().log("Comprobando que está el accesorio: '{}'".format(fav_accessorie), console=True)
            self.filter_text(fav_accessorie)
            self.filter_search()
            self.osl.wait_until_element_is_visible("//*[text()='{}']".format(fav_accessorie))
            self.filters_clear()
