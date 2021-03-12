*** Settings ***
Test Teardown     Run Keyword If Test Failed    SeleniumLibrary.Capture Page Screenshot    # Poner siempre #
Library           po/common/PythonPathScript.py
Library           po/WebApplication.py
Library           po/common/Common.py

*** Variables ***

*** Test Cases ***
WEB-LOGIN-0001
    [Documentation]    Registro y loging con un usuario aleatorio
    ${USER}    Common.Randomize    user@random    4
    ${PASSWORD}    Common.Randomize    passwd
    Comment    Abrir Aplicacion
    WebApplication.Abrir aplicacion
    Comment    SingUp
    WebApplication.Capturar Pantallazo
    WebLogin.Registrarse con email ${USER} y contrasena ${PASSWORD}
    Comment    LogIn
    WebLogin.Logarse con email ${USER} y contrasena ${PASSWORD}
    Comment    Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion
