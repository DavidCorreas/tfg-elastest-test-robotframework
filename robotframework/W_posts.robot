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

*** Variables ***


*** Test Cases ***
WEB-TEST-SETUP
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

WEB-POSTS-0001
    [Documentation]  Crear un post
    ${TITLE}  Common.Randomize  Titulo  4
    ${CONTENT}  Common.Randomize  Contenido de prueba
    Set Suite Variable  ${TITLE}
    Set Suite Variable  ${CONTENT}

    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment  LogIn
    WebLogin.Intentar Deslogarse
    WebLogin.Logarse como David

    Comment  Creamos un post
    WebPost.Acceder a la creacion de un post
    WebPost.Introducir titulo ${TITLE}
    WebPost.Introducir imagen Imagen-URJC.jpg
    WebPost.Introducir contenido "${CONTENT}"
    WebPost.Guardar post

    Comment  Comrpobar que se ha añadido bien
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE}", con imagen y contenido "${CONTENT}"

    Comment  Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion

WEB-POSTS-0002
    [Documentation]  Editar post creado en prueba WEB-POSTS-0001
    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment  LogIn
    WebLogin.Intentar Deslogarse
    WebLogin.Logarse como David

    Comment  Encontramos el post creado en la prueba WEB-POSTS-0001
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE}", con imagen y contenido "${CONTENT}"

    Comment  Editamos el post
    WebList.Editar post ${TITLE}
    WebPost.Introducir titulo ${TITLE}_edit
    WebPost.Introducir imagen Imagen-Mostoles.jpg
    WebPost.Introducir contenido "Edit: ${CONTENT}"
    WebPost.Guardar post

    Comment  Comrpobamos que se ha editado bien
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE}_edit", con imagen y contenido "Edit: ${CONTENT}"

    Comment  Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion

WEB-POSTS-0003
    [Documentation]  Eliminar post creado en prueba WEB-POSTS-0001 y editado en WEB-POSTS-0002
    Comment  Abrir Aplicacion
    WebApplication.Abrir Aplicacion

    Comment  LogIn
    WebLogin.Intentar Deslogarse
    WebLogin.Logarse como David

    Comment  Encontramos el post editado en la prueba WEB-POSTS-0002
    WebList.Poner paginado en 10
    WebList.Comprobar que existe post con titulo "${TITLE}_edit", con imagen y contenido "Edit: ${CONTENT}"

    Comment  Eliminamos el post
    WebList.Eliminar post ${TITLE}_edit
    WebList.Comprobar eliminacion del post con titulo ${TITLE}_edit

    Comment  Logout y cerramos la aplicacion
    WebApplication.Capturar Pantallazo
    WebLogin.Deslogarse
    WebApplication.Capturar Pantallazo
    WebApplication.Cerrar Aplicacion
