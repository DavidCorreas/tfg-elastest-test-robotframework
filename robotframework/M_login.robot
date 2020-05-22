*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    OutSystemsMobile.Capture Page Screenshot
Library    po/common/PythonPathScript.py
# ------------- #

Library    po-mobil/MobApplication.py
Library    po-mobil/MobLogin.py

*** Variables ***


*** Test Cases ***

LOGIN-0001
    Comment  Abrir Aplicacion
    MobApplication.Abrir Aplicacion    Android

    Comment    Login basico como administrador
    MobApplication.Capturar Pantallazo
#    MobLogin.Logarse como Admin
#    MobApplication.Capturar Pantallazo
#    MobLogin.Deslogarse
#    MobApplication.Capturar Pantallazo

    MobApplication.Cerrar Aplicacion