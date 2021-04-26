from robot.api.deco import keyword
from robotframework.po.common.PageObject import PageObject
from robot.libraries.BuiltIn import BuiltIn

ROBOT_LIBRARY_DOC_FORMAT = 'HTML'

btn_phones = "//a[contains(@href,'Phones')]"
title_phones = "//div[@id='Title'][text()='Phones']"

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


class WebPhones(PageObject):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
    __version__ = '1.0'

    # ------------------------------- Locators ------------------------------- #
    def __init__(self):
        super().__init__('SeleniumLibrary')

    # ------------------------------- Keywords ------------------------------- #
    @keyword(name='Go to page')
    def go_home(self):
        """
        Navegar a la página de moviles. Debe de estar visible la pestaña.
        """
        self._go_pages(btn_phones, title_phones)

    @keyword(name='Filters.Search with text ${text}')
    def filter_text(self, text):
        """
        Filters: Interact with the filters at the top of the page.

        Interact with the top text filter with the "Search" placeholder. Enter the text
        passed by parameter ${text}.

        Note: If you want to filter by this text use the keyword "Filters.Search".

        Steps:
        - Wait until the text field is on the page.
        - Enter the text from the ${text} parameter on the page.
        """
        self.osl.wait_until_element_is_visible(cmp_filter)
        self.osl.input_text(cmp_filter, text)
        self.osl.capture_page_screenshot()

    @keyword(name='Filters.Highest price first')
    def filter_highest(self):
        """
        En el filtro, clica el botón de 'Highest price' (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filters.Lowest price first')
    def filter_lowest(self):
        """
        Filters: Interact with the filters at the top of the page.

        Sorts the mobile page from lowest price to highest price.

        Note: If you want to sort by this policy use the keyword "Filters.Search".

        Steps:
        - Wait until the "Lowest Price" button is on the page.
        - Click the "Lowest Price" button in the filter.
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

    @keyword(name= 'Filters.Show devices with price from ${low_price} to ${high_price}.')
    def filter_price(self, precio_bajo, precio_alto):
        """
        En el filtro, pone un rango de precios siendo 'precio_bajo' el boton de la izquierda y
        'precio_alto' el boton de la derecha (Para buscar: Filtros.Buscar)
        """
        pass

    @keyword(name='Filters.Search')
    def filter_search(self):
        """
        Filters: Interact with the filters at the top of the page.

        Once the filters have been inserted, apply them by clicking on the "Search" button.

        Note: If you want to apply a filter, you must first fill in a field with the keywords noted with "Filter.<keyword>.
        keywords noted with "Filter.<keyword>".

        Steps:
        - Wait until the "Search" button is on the page.
        - Click on the "Search" button.
        """
        self.osl.wait_until_element_is_visible(btn_search)
        self.osl.capture_page_screenshot()
        self.osl.click_element(btn_search)
        self.osl.wait_until_element_is_visible(btn_clear)

    @keyword(name='Filters.Clear filter')
    def filters_clear(self):
        """
        Filters: Interact with the filters at the top of the page.

        Clear filters by clicking the 'clear' button. Only available when you have already filtered.

        Steps:
        - Wait until the 'Clear' button is available on the page.
        - Click the 'Clear' button.
        """
        pass

    @keyword(name='Go to details of the first result')
    def go_first(self):
        """
        Among all the records that appear on the page, select and view the detail of the first one that appears.

        Steps:
        - Wait for at least one result.
        - Select the first record.
        - Wait for the record detail to appear.
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
        Details: Interact with the detail screen of a device.

        Within the device detail, it adds to favorites and saves it in a variable in case it is used in the keyword: WebFavourites.Check saved favorites.

        Steps:
        - Wait for the favorites button to exist within the detail.
        - Check the favorites button if it was not already checked. If it was already marked, leave it as it is.
        - (The test is saved in that device has been added to favorites).
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
        BuiltIn().log("El dispositivo {} ha sido guardado en favoritos.".format(title), console=True)
        BuiltIn().set_global_variable("${FAV_PHONE}", title)
