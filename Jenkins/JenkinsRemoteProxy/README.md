# Jenkins Remote Proxy
Es el job a ejecutar si se van a ejecutar las pruebas en un servidor con proxy. Necesita realizar unas configuraciones extras para generar el entorno docker donde se van a ejecutar las pruebas

## Uso

El origen del proyecto es de un repositorio remoto, el cual tendremos que configurar en Jenkins. En el apartado Pipeline, se usará
la definición por _Pipeline script from SCM_. 

En este apartado se configurará la URL del proyecto, las credenciales con la que 
se hará pull, la rama que tiene los test que se quieran ejecutar. Además es recomendable establecer que la descarga del proyecto se haga 
en el workspace donde se ejecute la prueba. 

En el _Script Path_ se define donde se encuentra el Jenkinsfile que contiene el pipeline
que queremos ejecutar. En nuestro caso es `Jenkins/JenkinsRemote/Jenkinsfile`.

## Parametros
- BROWSER (Elección): Se definenen las opciones de los browsers disponibles para ejecutar en remoto (chrome, opera). Si se usa selenoid, deben estar definidos en browsers.json.
Ejemplo: chrome

- VERSION (Elección): Indica la versión el navegador Chrome a usar en Selenoid. Si la prueba se ejecuta dentro de la red de Prosegur se tiene que elegir un navegador con proxy.
Ejemplo: proxy-80.0, 80.0

- COUNTRY (Elección): Si se ejecuta la prueba para una página la cual dispone de multi-idioma, esta variable define el lenguaje a utilizar.
Ejemplo: es br fr us sg

- ENVIRONMENT (Elección): Entorno en el cual ejecutar la prueba.
Ejemplo: PRE_QA QA UAT DEMO

- REMOTE_URL (String): End point donde recibe las peticiones el selenoid. Normalmente http://selenoid:4444/wd/hub si se encuentra en la misma red docker.
Ejemplo: http://selenoid:4444/wd/hub

- TEST_CASES (String): Test cases a ejecutar. Deben de encontrarse en los test suites definidos en la variable TEST_SUITEy se definen precedidos de un -t.
Ejemplo: -t PRUEBA1 -t PRUEBA2

- TEST_SUITE (String): Suites a ejecutar. Se definen tal como se haría en linea de comandos precedido por el comando robot.
Ejemplo: PRUEBA-JENKINS.robot

- SLAVE_WORKSPACE (String): Es el workspace de Jenkins donde se copiaran los archivos para construir el docker con las pruebas. Se trata de la ruta del workspace viendola desde dentro del docker del esclavo.
Ejemplo: /var/data/slv/automatizacion/workspace/Test

- HOST_WORKSPACE (String): Workspace donde se ejecuta la prueba, desde el punto de vista de la máquina HOST. Se trata del mismo directorio que SLAVE_WORKSPACE, pero desde fuera del docker. En este directorio el docker python que ejecute la prueba dejará los resultados.
Ejemplo: /var/data/devops/jenkins/home/slave/automatizacion/workspace/Test

- NODE_LABEL (String): Nodo donde se van a ejecutar las pruebas y que es capaz de ejecutar comandos docker.
Ejemplo: SLAVE_IVV

## Run All
Este job sirve para ejecutar todos los jobs de Jenkins y necesita únicamente los parámetros de configuración. Necesita como argumento todos los nombres de los jobs que se quieren ejecutar.
