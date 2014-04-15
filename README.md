# Proyecto Energia

Ahora mismo la *"aplicación"* se encuentra operativa en [precio-energia.appspot.com](precio-energia.appspot.com).

## Getting Started
Modo de funcionamiento para empezar a jugar:

```bash
mkdir PrecioEnergia # Creamos la carpeta donde se va a bajar toda la fiesta
cd PrecioEnergia
git init # Iniciamos el repositorio en la carpeta actual
git remote add precioenergia https://github.com/PrecioEnergia/PrecioEnergia.git #Creamos el alias (precioenergia) a la conexion remota (o algo así)
git pull precioenergia master # Nos bajamos el branch master al directorio actual 
```

Ahora para hacer el deploy basta correr:

```bash
python manage.py runserver
```
Esto os petará porque hay que instalar:
* [pip](http://www.pip-installer.org/en/latest/installing.html)
* [mercurial](http://mercurial.selenic.com/) 
* [y el SDK google_appengine](https://developers.google.com/appengine/downloads.html#Google_App_Engine_SDK_for_Python)

Podéis echarle un ojo [aquí](https://developers.google.com/appengine/docs/python/gettingstartedpython27/#getstarted-framework-django).

Si pese a eso os sigue petando (a mi me pasa, solo puedo correrlo en local desde el eclipse) la opción más probable es porque python no está cogiendo bien la ruta del SDK, creo que habría que jugar con la variable *PYTHONPATH*


Para hacer el deploy del proyecto a  moverse a donde hayamos descargado el *google_appengine* y ejecutar: 

```bash
appcfg.py --oauth2 -A precio-energia update ../workspace-python/PrecioEnergia #O la ruta donde quiera que esté el proyecto
```

Podremos acceder a [http://localhost:8080](http://localhost:8080) y tendremos la aplicación web lista para jugar en local.

## Funcionamiento dentro de Eclipse
Abrimos el proyecto con eclipse-pydev. Instalamos el Google Suit Plugin para tener appengine dentro de eclipse.

Importamos el proyecto (Import > General > Existing Project into workspace). 

Seguro que se puede hacer checkout del proyecto directamente desde dentro de eclipse con algún plugin, en ese caso no hace falta importarlo.

Para ejecutarlo Run As > Pydev: Google AppRun

(Supongo que para hacer esto os pedirá la localización de las librerías del appengine).
