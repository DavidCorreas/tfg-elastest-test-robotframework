*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    OutSystemsWeb.Capture Page Screenshot
Library    po/common/PythonPathScript.py
# ------------- #

Library    po/WebApplication.py
Library    po/WebLogin.py

*** Variables ***


*** Test Cases ***
LOGIN-0001
    WebApplication.Abrir aplicacion

    Comment    Login basico como administrador
    WebApplication.Capturar Pantallazo

#    WebLogin.Logarse como Admin
#    WebApplication.Capturar Pantallazo
#    WebLogin.Deslogarse
#    WebApplication.Capturar Pantallazo

    WebApplication.Cerrar Aplicacion