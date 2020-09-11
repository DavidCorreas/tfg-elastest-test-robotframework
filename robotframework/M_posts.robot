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
    Set Suite Variable  ${TITLE}
    Set Suite Variable  ${CONTENT}

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

POSTS-0002
    [Documentation]  Editar post creado en prueba POSTS-0001
    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment  LogIn
    MobLogin.Intentar Deslogarse
    MobLogin.Logarse como David

    Comment  Encontramos el post creado en la prueba POSTS-0001
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE}", con imagen y contenido "${CONTENT}"

    Comment  Editamos el post
    MobList.Editar post ${TITLE}
    MobPost.Introducir titulo ${TITLE}_edit
    MobPost.Introducir imagen Imagen-Mostoles.jpg
    MobPost.Introducir contenido "Edit: ${CONTENT}"
    MobPost.Guardar post

    Comment  Comrpobamos que se ha editado bien
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE}_edit", con imagen y contenido "Edit: ${CONTENT}"

    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil

POSTS-0003
    [Documentation]  Eliminar post creado en prueba POSTS-0001 y editado en POSTS-0002
    Comment  Abrir Aplicacion
    MobApplication.Abrir aplicacion movil en Android

    Comment  LogIn
    MobLogin.Intentar Deslogarse
    MobLogin.Logarse como David

    Comment  Encontramos el post editado en la prueba POSTS-0002
    MobList.Poner paginado en 10
    MobList.Comprobar que existe post con titulo "${TITLE}_edit", con imagen y contenido "Edit: ${CONTENT}"

    Comment  Eliminamos el post
    MobList.Eliminar post ${TITLE}_edit
    MobList.Comprobar eliminacion del post con titulo ${TITLE}_edit

    Comment  Logout y cerramos la aplicacion
    MobApplication.Capturar Pantallazo movil
    MobLogin.Deslogarse
    MobApplication.Capturar Pantallazo movil
    MobApplication.Cerrar Aplicacion movil
