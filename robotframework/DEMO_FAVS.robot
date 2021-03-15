*** Settings ***
Test Teardown     Run Keyword If Test Failed    WebApplication.Capturar Pantallazo    # Poner siempre #
Library           po/common/PythonPathScript.py
Library           po/WebApplication.py
Library           po/WebLogin.py
Library           po/WebHome.py


*** Variables ***

*** Test Cases ***
ADD-TO-FAVS
    [Documentation]    Busca los portátiles, móviles y accesorios más baratos y los añade a favoritos.

    WebApplication.Abrir Aplicacion
    WebLogin.LogIn con email "david.correas@innoqa.es" y contrasena "hello"

    WebHome.Entrar en la pagina de portatiles
    WebHome.Ir a la página
    WebHome.Entrar en la pagina de móviles
    WebHome.Ir a la página
    WebHome.Entrar en la pagina de accesorios
    WebHome.Ir a la página
    WebHome.Entrar en la pagina de favoritos

    WebLogin.LogOut
    WebApplication.Cerrar Aplicacion
