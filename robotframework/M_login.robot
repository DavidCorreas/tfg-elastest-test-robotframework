*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    MobApplication.Capturar Pantallazo movil
Library    po/common/PythonPathScript.py
# ------------- #

Library    po-mobil/MobApplication.py
Library    po-mobil/MobLogin.py
Library    po/common/Common.py

*** Variables ***


*** Test Cases ***
LOGIN-0001
    [Documentation]  Registro y loging con un usuario aleatorio
    ${USER}  Common.Randomize  user@random  4
    ${PASSWORD}  Common.Randomize  passwd

    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment    SingUp
    MobApplication.Capturar Pantallazo movil
    MobLogin.Registrarse con email ${USER} y contrasena ${PASSWORD}

    Comment  LogIn
    MobLogin.Logarse con email ${USER} y contrasena ${PASSWORD}

    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil