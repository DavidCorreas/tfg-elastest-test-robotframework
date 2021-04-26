from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject
from robot.libraries.BuiltIn import BuiltIn

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

btn_laptops = "//a[contains(@href,'Laptops')]"
title_laptops = "//div[@id='Title'][text()='Laptops']"

cmp_filter = "//input[contains(@id,'Input_Search')]"
btn_lowest = "//button[contains(@id,'LowestPrice')]"
btn_search = "//button[contains(@id,'Button_search')]"
btn_clear = "//a[contains(@id,'Link_Clear')]"
result_with_number = "//div[contains(@id,'ListOfProducts')]/div[{}]"
loc_results_prices = "//div[contains(@id,'ListOfProducts')]/div//span[contains(@id,'CurrentPrice')]"

loc_phone_title = "//div[contains(@id,'Column2')]/span[text()='{}']"
loc_detail_title = "//div[contains(@id,'Column2')]/span"

# Detalles
btn_fav = "//div[@id='AddOrRemoveToFavorites']"
btn_add_favs = "//button[@id='Button_AddFavorites']"
btn_remove_favs = "//button[@id='Button_RemoveFavorites']"


class WebLaptops(PageObject):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Go to page')
    def go_home(self):
        """
        Navegar a la página de portátiles. Debe de estar visible la pestaña.
        """
        self._go_pages(btn_laptops, title_laptops)

    @keyword(name='Filtros.Buscar con el texto ${text}')
    def filter_text(self, text):
        """
        En el filtro, busca por el texto pero no le da a buscar (Para buscar: Filtros.Buscar)
        """
        self.osl.wait_until_element_is_visible(cmp_filter)
        self.osl.input_text(cmp_filter, text)
        self.osl.capture_page_screenshot()

    @keyword(name='Filtros.Precio más alto primero')
    def filter_highest(self):
        """
        En el filtro, clica el botón de 'Highest price' (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filters.Lowest price first')
    def filter_lowest(self):
        """
        En el filtro, clica el botón de 'Lowest price' (Para buscar: Filtros.Buscar)
        """
        btn_lowest_selected = btn_lowest + "[contains(@class,'selected')]"
        self.osl.wait_until_element_is_visible(btn_lowest)
        try:
            self.osl.capture_page_screenshot()
            self.osl.wait_until_element_is_visible(btn_lowest_selected,
                                                   timeout=0.5)
        except:
            self.osl.click_element(btn_lowest)
        self.osl.wait_until_element_is_visible(btn_lowest_selected)

        # Pulsar boton buscar
        self.osl.wait_until_element_is_visible(btn_search)
        self.osl.capture_page_screenshot()
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
             'Filtros.Mostrar portatiles con precio desde ${precio_bajo} hasta ${precio_alto}')
    def filter_price(self, precio_bajo, precio_alto):
        """
        En el filtro, pone un rango de precios siendo 'precio_bajo' el boton de la izquierda y
        'precio_alto' el boton de la derecha (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filters.Search')
    def filter_search(self):
        """
        Aplica los filtros pulsando el botón filtrar.
        """
        self.osl.wait_until_element_is_visible(btn_search)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_search)
        self.osl.wait_until_element_is_visible(btn_clear)

    @keyword(name='Filtros.Limpiar filtros')
    def filters_clear(self):
        """
        Limpia los filtros pulsando el botón de 'clear'. Solo disponible cuando ya se ha filtrado.
        """
        pass

    @keyword(name='Go to details of the first result')
    def go_first(self):
        """
        Entre todos los resultados, entra en el detalle del primero.
        """
        loc_first_result = result_with_number.format("1")
        loc_first_result_name = loc_first_result + "//span[contains(@id,'ProductName')]"
        self.osl.wait_until_element_is_visible(loc_first_result)
        self.osl.capture_page_screenshot()
        first_result_name = self.osl.get_text(loc_first_result_name)
        BuiltIn().wait_until_keyword_succeeds(5, 0.2, "Click Element", loc_first_result)
        self.osl.capture_page_screenshot()
        self.osl.wait_until_element_is_visible(loc_phone_title.format(first_result_name))

    @keyword(name='Details.Add to favourites')
    def add_to_favs(self):
        """
        Dentro del detalle del portatil, añade a favoritos y se lo guarda en una variable por si se
        usa en la keyword: WebFavourites.Comprobar favoritos guardados
        """
        self.osl.wait_until_element_is_visible(btn_fav)
        try:
            self.osl.wait_until_element_is_visible(btn_add_favs, timeout=1)
            self.osl.capture_page_screenshot()
            self.osl.click_element(btn_add_favs)
        except AssertionError:
            BuiltIn().log("El dispositivo ya estaba añadido a favoritos.")

        self.osl.wait_until_element_is_visible(btn_remove_favs)
        title = self.osl.get_text(loc_detail_title)
        self.osl.capture_page_screenshot()
        BuiltIn().log("El portátil {} ha sido guardado en favoritos.".format(title), console=True)
        BuiltIn().set_global_variable("${FAV_LAPTOP}", title)

