*** Settings ***
# Poner siempre #
Test Teardown    Run Keyword If Test Failed    WebApplication.Capturar Pantallazo
Library    po/common/PythonPathScript.py
# ------------- #

Library    po/WebApplication.py
Library    po/WebLogin.py
Library    po/WebPost.py
Library    po/WebList.py
Library    po/common/Common.py
Library    po-mobil/MobApplication.py
Library    po-mobil/MobLogin.py
Library    po-mobil/MobPost.py
Library    po-mobil/MobList.py


*** Variables ***


*** Test Cases ***
MOVIL-WEB-TEST-SETUP
    [Documentation]  Test necesario para crear el usuario si no existe
    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment    Intentamos registrar a David si no existe su usuario
    WebApplication.Capturar Pantallazo
    WebLogin.Intentar Deslogarse
    WebLogin.Registrar a David si no existe

    Comment  Cerramos la aplicacion
    WebLogin.Intentar Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion

MOBIL-WEB-POSTS-0001
    [Documentation]  Creamos un post en movil y consultamos que se haya creado en la web
    ${TITLE1}  Common.Randomize  Titulo  4
    ${CONTENT1}  Common.Randomize  Contenido de prueba
    Set Suite Variable  ${TITLE1}
    Set Suite Variable  ${CONTENT1}

    # ==== Parte Movil ====
    Set Library Search Order  AppiumLibrary
    Comment  Abrir Aplicacion movil
    MobApplication.Abrir aplicacion movil en Android

    Comment  LogIn
    MobLogin.Intentar Deslogarse
    MobLogin.Logarse como David

    Comment  Creamos un post
    MobPost.Acceder a la creacion de un post
    MobPost.Introducir titulo ${TITLE1}
    MobPost.Introducir imagen Imagen-URJC.jpg
    MobPost.Introducir contenido "${CONTENT1}"
    MobPost.Guardar post

    Comment  Comrpobar que se ha añadido bien
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE1}", con imagen y contenido "${CONTENT1}"


    # ==== Parte Web ====
    Set Library Search Order  SeleniumLibrary
    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment  LogIn
    WebLogin.Intentar Deslogarse
    WebLogin.Logarse como David

    Comment  Comrpobar que se ha añadido bien
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE1}", con imagen y contenido "${CONTENT1}"

    Comment  Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion

    # ==== Parte Movil ====
    Set Library Search Order  AppiumLibrary
    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil

MOBIL-WEB-POSTS-0002
    [Documentation]  Creamos un post en web y consultamos que se haya creado en el movil
    ${TITLE2}  Common.Randomize  Titulo  4
    ${CONTENT2}  Common.Randomize  Contenido de prueba
    Set Suite Variable  ${TITLE2}
    Set Suite Variable  ${CONTENT2}

    # ==== Parte Web ====
    Set Library Search Order  SeleniumLibrary
    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment  LogIn
    WebLogin.Intentar Deslogarse
    WebLogin.Logarse como David

    Comment  Creamos un post
    WebPost.Acceder a la creacion de un post
    WebPost.Introducir titulo ${TITLE2}
    WebPost.Introducir imagen Imagen-URJC.jpg
    WebPost.Introducir contenido "${CONTENT2}"
    WebPost.Guardar post

    Comment  Comrpobar que se ha añadido bien
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE2}", con imagen y contenido "${CONTENT2}"


    # ==== Parte Movil ====
    Set Library Search Order  AppiumLibrary
    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment  LogIn
    MobLogin.Intentar Deslogarse
    MobLogin.Logarse como David

    Comment  Encontramos el post creado en la prueba POSTS-0001
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE2}", con imagen y contenido "${CONTENT2}"

    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil

    # ==== Parte Movil ====
    Set Library Search Order  SeleniumLibrary
    Comment  Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion
