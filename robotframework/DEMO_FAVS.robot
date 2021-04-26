*** Settings ***
Test Teardown     Run Keyword If Test Failed    WebApplication.Capturar Pantallazo    # Poner siempre #
Library           po/common/PythonPathScript.py
Library           po/WebApplication.py
Library           po/WebLogin.py
Library           po/WebHome.py
Library           po/WebPhones.py
Library           po/WebLaptops.py
Library           po/WebAccessories.py
Library           po/WebFavourites.py

*** Variables ***

*** Test Cases ***
ADD-TO-FAVS
    [Documentation]    Busca los portátiles, móviles y accesorios más baratos y los añade a favoritos.
    WebApplication.Open Application
    WebLogin.LogIn with email "david.correas@innoqa.es" and password "hello"
    WebHome.Go mobile page
    WebPhones.Filters.Lowest price first
    WebPhones.Filters.Search
    WebPhones.Go to details of the first result
    WebPhones.Details.Add to favourites
    WebLaptops.Go to page
    WebLaptops.Filters.Lowest price first
    WebLaptops.Filters.Search
    WebLaptops.Go to details of the first result
    WebLaptops.Details.Add to favourites
    WebAccessories.Go to page
    WebAccessories.Filters.Lowest price first
    WebAccessories.Filters.Search
    WebAccessories.Go to details of the first result
    WebAccessories.Details.Add to favourites
    WebFavourites.Go to page
    WebFavourites.Check saved favourites
    WebLogin.LogOut
    WebApplication.Close application
