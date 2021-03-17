*** Settings ***
Test Teardown     Run Keyword If Test Failed    MobApplication.Capturar Pantallazo Movil
Library           po/common/PythonPathScript.py
Library           po-mobil/MobApplication.py
Library           po-mobil/MobLogin.py
Library           po-mobil/MobTask.py
Library           po-mobil/MobProject.py


*** Variables ***

*** Test Cases ***
NEW-TASK
    [Documentation]    Busca los portátiles, móviles y accesorios más baratos y los añade a favoritos.

    MobApplication.Abrir aplicacion movil en Android
    MobLogin.LogIn con usuario "miguel.cervera@innoqa.es" y contrasena "Gr@tis69"

    MobProject.Ir a la página
    MobProject.Crear proyecto con nombre "Projecto demo"
    MobProject.Entrar en el proyecto "Projecto demo"
    MobProject.DetalleProyecto.Crear tarea en proyecto vacio con nombre "Prueba Tarea" y fecha "23-05-2021"
    MobProject.DetalleProyecto.Marcar "Prueba Tarea" como completado
    MobProject.DetalleProyecto.Volver a proyectos

    MobTask.Ir a la página
    MobTask.Ir a la pestaña "Completed"
    MobTask.Seleccionar tarea con nombre "Prueba Tarea"
    MobTask.DetalleTarea.Borrar tarea

    MobLogin.LogOut
    MobApplication.Cerrar Aplicacion Y Sesion Appium


