# Jenkins

Se han integrado varias opciones para la integración del proyecto para jenkins.

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

## JenkinsLocal
Job de jenkins donde se obtienen los archivos de los test directamente del sistema de ficheros del programador, por lo que 
se hace una ejecución de los test en remoto más rápida (ya que no hay que hacer un checkout del repositorio), además de 
no es necesario hacer commit y push al repositorio cada vez que se quiera probar. 

Como ejecuta desde el workspace del programador, puede ejecutar las pruebas de cualquier rama en la que te encuentres.

### Requisitos
Es necesario un jenkins slave capaz de acceder a tu sistema de ficheros y que pueda ejecutar comandos docker.

### Uso
Es necesario crear un job de jenkins de tipo pipeline. En este, se debe introducir el Jenkinsfile del directorio de 
JenkinsLocal dentro del job, y es necesario crear los siguientes argumentos que recibirá el pipeline.

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
- PROYECT_PATH: Localización tanto del proyecto, como sus dependencias a copiar (OutSystemsWeb, OutSystemsMobile). Si estamos en Windows deberá ser el path dentro de la VM del Dockerd (C:/... == /c/...)
Ejemplo: Editamos un proyecto localizado en `C:\Users\DavidCorreas\Ubuntu\jenkins_slave\Proyect`.
Tenemos un volumen: `C:\Users\DavidCorreas\Ubuntu\jenkins_slave:/home/jenkins/Windows`. Esta variable tendría que ser: `/home/jenkins/Windows` 

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

## JenkinsRemote

Job de Jenkins en el que se obtienen todos los recursos de los repositorios.

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

En cuanto a los argumentos son iguales a los del Job de JenkinsLocal, exceptuando a _PROYECT_PATH_, que no se definirá ya que 
el origen del proyecto es remoto.


