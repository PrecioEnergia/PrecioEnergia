# Proyecto Energia


Modo de funcionamiento:

```bash
git clone https://github.com/gonzmg88/precioenergiaAppEngine
```

Si vamos a la carpeta del proyecto y hacemos:

```bash
python manage.py runserver
```

Para hacer el deploy del proyecto a appengine: 

```bash
appcfg.py --oauth2 -A precio-energia update ../workspace-python/PrecioEnergia
```

Podremos acceder a http://localhost:8080 y tendremos la aplicación web lista para jugar en local.

## Funcionamiento dentro de Eclipse
Abrimos el proyecto con eclipse-pydev. Instalamos el Google Suit Plugin para tener appengine dentro de eclipse.

Importamos el proyecto (Import > General > Existing Project into workspace). Seguro que se puede hacer el fork del proyecto directamente desde dentro de eclipse con algún plugin, en ese caso no hace falta importarlo.

Para ejecutarlo Run As > Pydev: Google AppRun

(Supongo que para hacer esto os pedirá la localización de las librerías del appengine).
