*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    OutSystemsMobile.Capture Page Screenshot movil
Library    po/common/PythonPathScript.py
# ------------- #

Library    po-mobil/MobApplication.py
Library    po-mobil/MobLogin.py

*** Variables ***


*** Test Cases ***

LOGIN-0001
    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment    Login basico como administrador
    MobApplication.Capturar Pantallazo movil
#    MobLogin.Logarse como Admin
#    MobApplication.Capturar Pantallazo movil
#    MobLogin.Deslogarse
#    MobApplication.Capturar Pantallazo movil

    MobApplication.Cerrar Aplicacion movil