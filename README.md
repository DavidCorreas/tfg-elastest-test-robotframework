# TFG-ELASTEST-TEST-ROBOTFRAMEWORK
Tests end-to-end realizados con RobotFramework, un framework de testing hecho en Python.

## Objetivos
Realizar test end-to-end sobre la aplicación web y movil, alojado en [tfg-elastest-sut][tfg-elastest-sut].
Para que funcione estos test, es necesario que la aplicación esté completamente desplegada. 

Si se van a ejecutar los test sobre web no es necesarío que esté desplegada la parte móvil con el emulador. 
En caso contrario, si se quieren realizar los test sobre la aplicación móvil es necesario que esté
desplegado el emulador con la aplicación y Appium. Esto se puede encontrar en el repositorio padre
[tfg-elastest-test][tfg-elastest-test].

## Componentes
En este repositorio no solo se encuentran los test, sino que también se encuentran más ficheros ajenos
necesarios para poder ejecutarlos tanto en Jenkins como en la máquina local.

### Jenkins
En este directorio del proyecto se encuentran jobs y utilidades necesarios para el funcionamiento de
los test en Jenkins. Se puede obtener más información en el [README.md](https://github.com/DavidCorreas/tfg-elastest-test-robotframework/blob/1237ac665bd6ba32c0ca06e23457bd3ac82810fa/Jenkins/README.md)
dentro del directorio. 

### RobotFramework
En este directorio se encuentran todos los test. Para explicarlo de una forma resumida se divide en varias partes:
- TestSuites: Son todos los ficheros `*.robot` donde se encuentran automatizados todos los test. Son los
que tendremos que ejecutar si queremos realizar alguna prueba.

- PO: En este directorio se encuentran los PageObjects. Son _keywords_ o funciones que automatizan la página.
Cada pantalla de la aplicación tiene su PO que lo automatiza.

- Data: Se encuentran los datos estáticos relacionados con las pruebas. Por ejemplo usuarios o imagenes para
subir a la aplicación. Estos datos pueden ser seleccionados dependiendo del entorno o país donde se ejecute 
la prueba. Para poner un ejemplo, esto quiere decir que puede que haya dos usuarios diferentes para hacer
login dependiendo si es la página de España o de Francia. La prueba puede deducir el usuario a partir 
de unas variables de entorno que se explicarán más adelante.

### Venv
Es el entorno virtual de Python que se ha utilizado para modelar todas las pruebas. No funciona para Linux,
pero se puede crear un entorno virtual a partir de todas las dependencias que están especificadas en 
`Jenkins/Environment/requirements.txt`. Se pueden instalar las dependencias en el entorno mediante el
comando `pip install -r requirements.txt`.

## Configuración de las pruebas
El framework se ha montado para que puedan parametrizarse las pruebas y poder aprovechar el mismo test para
diferentes situaciones. Estas configuraciones se harán mediante variables de entorno (En el apartado de
despliegue se encuentra como modificar estas variables). Se dispone de las siguientes variables:

- BROWSER: Se puede definir el navegador sobre el que se ejecutarán las pruebas. Cada navegador necesita de 
un driver ajeno al proyecto, como por ejemplo el chrome necesita de un ChromeDriver.exe. Hay más información sobre 
los navegadores disponibles y cómo definirlos [aquí](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html#Open%20Browser).

- COD_PAIS: Si se dispone de una aplicación multi-idioma, se pueden configurar en el directorio `data` los datos a usar en cada
uno de los países. La prueba se realiza sobre una aplicación solo en español, por lo que únicamente se podrá pasar
como argumento `es`.

- ENVIRONMENT: Si la aplicación es multi-entorno, se define en qué entorno se desea ejecutar la prueba. En el caso
del sut de prueba solo se dispone de un entorno y solo aceptaría el argumento `DEV`.

- REMOTE_URL (String): End point donde recibe las peticiones el selenoid. Normalmente `http://selenoid:4444/wd/hub` si 
se encuentra en la misma red docker.

- TEST_CASES (String): Test cases a ejecutar. Deben de encontrarse en los test suites definidos en la variable _TEST_SUITE_
 y se definen precedidos de un `-t`. Ejemplo: `-t PRUEBA1 -t PRUEBA2`

- TEST_SUITE (String): Suites a ejecutar. Se definen tal como se haría en linea de comandos precedido por el comando `robot`.
Ejemplo: `PRUEBA-JENKINS.robot`


## Despliegue
Hay varias formas de deplegar los test que se explicarán a continuación. Como se ha dicho en el apartado de
'objetivos', es fundamental que esté desplegada la aplicación y tener la dirección de acceso.

Este apartado se dividirá en dos para explicar como ejecutar las pruebas y donde se van a ejecutar.

### Formas de ejecución de las pruebas
Se explicará cómo configurar Python para ejecutar las pruebas.

#### Python (Venv)
Esta es la mejor forma de ejecutar las pruebas si se están desarrollando ya que es la forma más rápida de lanzarlas,
pero por contra es una opción más 'tediosa' de configurar.

Se necesita de Python 3 y opcionalemnte Venv. Primero se ha de configurar este entorno. Para crear un entorno
virtual de python se puede seguir [esta documentación](https://docs.python.org/3/library/venv.html).

Una vez tengamos el entorno creado, se necesitará instalar las dependencias en él. Para ello tenemos que activar el 
entorno ejecutando `venv/bin/activate`, y después instalamos las dependencias que se encuentran en `Jenkins/Environment/requirements.txt`
ejecutando `pip install -r requirements.txt`.

Por último se necesita de el driver correspondiente para poder ejecutar las pruebas web en un navegador. Si se usa Chrome 
se ha de añadir al path el binario, pudiendose descargar [aquí](https://chromedriver.chromium.org/downloads).

#### Docker
Existe un dockerfile con Python y todo configurado para poder ejecutarse las pruebas. Este dockerfile se encuentra en
`Jenkins/Environment/dockerfile`. Por ahora solo está configurado para que disponga de un Selenoid donde lanzar las 
pruebas.

### Contra qué lanzar las pruebas
Una vez tenido el entorno que es capaz de ejecutar las pruebas de RobotFramework, se ha de tener un _endpoint_ donde 
se encuentre la aplicación para poder probarla. Se dividirán las opciones según sea móvil o web o híbridas.

#### Web
Para ejecutar una prueba web se manejan dos opciones:

- **Local**: Se despliega un navegador local gracias al driver y se ejecuta la prueba automática contra él. Se debe
configurar la variable de entorno del test `IS_REMOTE=False`
- **Remoto**: Se puede configurar una url el cual disponga de navegadores para ejecutar las pruebas. Existen varias
aplicaciones y servicios que orquestan navegadores bajo demanda como [Elastest](https://elastest.eu/) o 
[Selenoid](https://github.com/aerokube/selenoid). Para configurar los test para que se lance contra estos
servicios se deben configurar las variables de entorno `IS_REMOTE=True` y `REMOTE_URL=http://<URL>:4444/wd/hub` 
(puede ser otro _endpoint_).

#### Móvil
Para ejecutar las pruebas móviles se necesitan varios componentes.
- Emulador o dispositivo: Para probar la aplicación móvil, se necesita un dispositivo que esté
visible por un servidor [adb](https://developer.android.com/studio/command-line/adb?hl=es-419).
- Appium: Es un framework que nos permitirá automatizar pruebas automáticas de movil. Se trata 
de un servidor npm que se conectará al dispositivo y ejecutará los pasos de las pruebas. Más acerca
de appium [aquí](http://appium.io/).
- WebDriver: Appium también necesita de un driver para poder ejecutar las pruebas.

#### Híbrida (Móvil y web)
Se ha de tener ambas partes.

## Ejecución de una prueba
Una vez configurado el entorno en el que lanzar las pruebas, ha de ejecutarse el siguiente
comando para poder ejecutar las pruebas. Primero, tenemos que activar nuestro entorno virtual
Python donde tengamos RobotFramework, accedemos al directorio donde se encuentren los ficheros 
`*.robot` y ejecutamos:

`robot -d results W_login.robot`

Esto nos lanzará el test-suite W_login.robot y se nos guardarán los resultados de la prueba en
la carpeta `results`, dentro del directorio actual.

Se pueden pasar más parámetros a este comando como los siguientes:
- `-v`: Agrega o modidifica una variable de entorno.
- `-t`: Selecciona que test ejecutar dentro del test-suite.
- `-d`: Directorio donde guardar los resultados de la prueba.

Como ejemplo completo de ejecución:

- `robot -d results -v COD_PAIS:es -v ENVIRONMENT:DEV -t WEB-POSTS-0001 -t WEB-POSTS-0002 W_posts.robot`

Este comando se puede traducir a:
- En el país _es_ (España) y en el entorno _DEV_ (desarrollo) 
- Ejecuta los test _WEB-POSTS-0001_ y _WEB-POSTS-0002_
- Del test-suite W_posts.robot
- Y guarda los resultados en la carpeta _./results_

Más información sobre como lanzar una prueba de RobotFramework 
[aquí](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html#executing-test-cases).


[tfg-elastest-sut]: https://github.com/DavidCorreas/tfg-elastest-sut
[tfg-elastest-test]: https://github.com/DavidCorreas/tfg-elastest-test
[tfg-elastest]: https://github.com/DavidCorreas/tfg-elastest
