# Jenkins
Se han integrado varias opciones para la integración del proyecto para jenkins.

## Objetivos
Este módulo del proyecto tiene como objetivo dotar una integración de los test en Jenkins. Para ello, se han creado
varios jobs y utilidades que nos ayudarán a tener un seguimiento de las pruebas automatizado, gracias a Jenkins.

Los Jobs son de tipo pipeline y se explica como configurarlos en sus respectivos subapartados. Los Jobs disponibles son:
- JenkinsRemote
- JenkinsRemoteProxy

Otras utilidades que nos ayudarán a gestionar el Jenkins donde tengamos las pruebas son las siguientes:
- Environment
- LimpiezaPruebas
- Selenoid

## JenkinsRemote
Job de Jenkins para realizar las pruebas en cualquier Jenkins donde su nodo ejecutor tenga acceso a docker. 
En este directorio se encuentran todos los archivos necesarios para poder realizarse las pruebas end-to-end.

### Requisitos
Se necesita un nodo de Jenkins que sea capaz de ejecutar comandos docker, docker-compose y git.

### Uso
El origen del proyecto es de un repositorio remoto, el cual tendremos que configurar en Jenkins. En el apartado Pipeline, se usará
la definición por _Pipeline script from SCM_. 

En este apartado se configurará la URL del proyecto, las credenciales con la que 
se hará pull, la rama que tiene los test que se quieran ejecutar. Además es recomendable establecer que la descarga del proyecto se haga 
en el workspace donde se ejecute la prueba. 

En el _Script Path_ se define donde se encuentra el Jenkinsfile que contiene el pipeline
que queremos ejecutar. En nuestro caso es `Jenkins/JenkinsRemote/Jenkinsfile`.

#### Argumentos:
Necesarios para la parametrización de la prueba:

- BROWSER (Lista): Se definenen las opciones de los browsers disponibles para ejecutar en remoto (chrome, opera). Si se usa 
selenoid, deben estar definidos en browsers.json.
- COUNTRY (Lista): Si se ejecuta la prueba para una página la cual dispone de multi-idioma, esta variable define el 
lenguaje a utilizar.
- ENVIRONMENT (Lista): Entorno en el cual ejecutar la prueba.
- REMOTE_URL (String): End point donde recibe las peticiones el selenoid. Normalmente `http://selenoid:4444/wd/hub` si 
se encuentra en la misma red docker.
- TEST_CASES (String): Test cases a ejecutar. Deben de encontrarse en los test suites definidos en la variable _TEST_SUITE_
 y se definen precedidos de un `-t`. Ejemplo: `-t PRUEBA1 -t PRUEBA2`
- TEST_SUITE (String): Suites a ejecutar. Se definen tal como se haría en linea de comandos precedido por el comando `robot`.
Ejemplo: `PRUEBA-JENKINS.robot`

Necesarios para la pipeline de Jenkins.
- NODE_WORKSPACE_DOCKERD (String): Es el workspace de Jenkins donde se copiaran los archivos para construir el docker con las pruebas.
Se define para que cada job tenga su workspace y no reusen el mismo directorio. Si el _jenkins slave_ se está ejecutando en docker,
debe ser la ruta linkeada a tu zona de trabajo. 
Ejemplo: `/home/jenkins/Windows/workspace/Proyect-LOCAL`

- NODE_WORKSPACE_WINDOWS (String): Representa lo mismo que _NODE_WORKSPACE_DOCKERD_, pero sería el path relativo al sistema
de ficheros Windows. Si no se está ejecutando en Windows llevará el mismo valor que _NODE_WORKSPACE_DOCKERD_. 
Es necesaria ya que el docker python que ejecute las pruebas no puede almacenar los resultados en el volumen de Jenkins, y necesita 
almacenarlo por su cuenta en el directorio persistente.
Ejemplo: `/c/Users/DavidCorreas/Ubuntu/jenkins_slave/workspace/Proyect-LOCAL`

- NODE_LABEL (String): Nodo donde se van a ejecutar las pruebas y que es capaz de ejecutar comandos docker y tiene
acceso a los ficheros.

## JenkinsRemoteProxy

Funciona igual que el job 'JenkinsRemote', pero está configurado para poder ejecutar las pruebas dentro de 
un proxy. Se debe de introducir el proxy en `JenkinsRemteProxy/dockerfile`.

### Navegador con Proxy
Además para su correcto funcionamiento se debe configurar el job para que se ejecute con un navegador con el proxy
configurado. 

Para la ejecución de estas pruebas se necesita de un navegador. En esta infrastrucutra, se ha decidido el uso de 
Selenoid como orquestador de navegadores. Ese es un orquestador de docker que nos proporcionará navegadores 
dockerizados bajo demanda.

En el directorio `Jenkins/Selenoid` se encuentra una imagen de chrome con el proxy configurado.
Lo único que se tendría que hacer es cuando se lanzase la prueba, tiene que lanzarse contra ese navegador,
Para ello, está la variable de 'BROWSER' en el Job. Simplemente tendremos que añadir esta imagen con proxy
al Selenoid y elegirlo mediante esta variable.

## Environment
En este directorio se encuentran todos los archivos para dockerizar un entorno con todos los recursos necesarios para 
ejecutar las pruebas de robot framework.

El objetivo de este docker es subirlo a un registry o a docker hub ya compilado, para que cada vez que ejecutemos un test
no tengamos que construir el entorno de ejecución.

### Docker
Este docker contiene:

- Python 3:
- Las dependencias de python del pryecto, definidas en el fichero _requirements.txt_.
- Procedimiento para la instalación del ChromeDriver.
- Variables por defecto de los test.

## LimpiezaDatos

Se trata de un script de groovy para hacer limpieza de ficheros que generan las pruebas, conservando 
los xml para poder tener una traza más clara de todas las ejecuciones que se han ido haciendo.

## Selenoid

Se encuentran navegadores personalizados para añadirlos a Selenoid. Actualmente hay un navegador Chrome 
con un proxy para confiugrar. Si se quiere añadir un proxy, hay que modificar el fichero `Jenkins/Selenoid/DockerfileProxy`
y sustituir `<url proxy>` por el proxy.


