*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    MobApplication.Capturar Pantallazo movil
Library    po/common/PythonPathScript.py
# ------------- #

Library    po-mobil/MobApplication.py
Library    po-mobil/MobLogin.py
Library    po-mobil/MobPost.py
Library    po-mobil/MobList.py
Library    po/common/Common.py

*** Variables ***


*** Test Cases ***
TEST-SETUP
    [Documentation]  Test necesario para crear el usuario si no existe
    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment    Intentamos registrar a David si no existe su usuario
    MobApplication.Capturar Pantallazo movil
    MobLogin.Intentar Deslogarse
    MobLogin.Registrar a David si no existe

    Comment  Cerramos la aplicacion
    MobLogin.Intentar Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil

POSTS-0001
    [Documentation]  Crear un post
    ${TITLE}  Common.Randomize  Titulo  4
    ${CONTENT}  Common.Randomize  Contenido de prueba

    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment  LogIn
    MobLogin.Intentar Deslogarse
    MobLogin.Logarse como David

    Comment  Creamos un post
    MobPost.Acceder a la creacion de un post
    MobPost.Introducir titulo ${TITLE}
    MobPost.Introducir imagen Imagen-URJC.jpg
    MobPost.Introducir contenido "${CONTENT}"
    MobPost.Guardar post

    Comment  Comrpobar que se ha añadido bien
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE}", con imagen y contenido "${CONTENT}"

    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil
