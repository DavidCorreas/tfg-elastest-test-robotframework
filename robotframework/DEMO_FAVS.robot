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

    WebApplication.Abrir Aplicacion
    WebLogin.LogIn con email "david.correas@innoqa.es" y contrasena "hello"

    WebHome.Entrar en la pagina de móviles
    WebPhones.Filtros.Precio más bajo primero
    WebPhones.Filtros.Buscar
    WebPhones.Entrar en el primer resultado
    WebPhones.Detalles.Añadir a favoritos

    WebLaptops.Ir a la página
    WebLaptops.Filtros.Precio más bajo primero
    WebLaptops.Filtros.Buscar
    WebLaptops.Entrar en el primer resultado
    WebLaptops.Detalles.Añadir a favoritos

    WebAccessories.Ir a la página
    WebAccessories.Filtros.Precio más bajo primero
    WebAccessories.Filtros.Buscar
    WebAccessories.Entrar en el primer resultado
    WebAccessories.Detalles.Añadir a favoritos

    WebFavourites.Ir a la página
    WebFavourites.Comprobar favoritos guardados
    WebLogin.LogOut
    WebApplication.Cerrar Aplicacion
