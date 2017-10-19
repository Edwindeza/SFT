# SLM - Software

## Descripción

Código fuente del Sistema Web de Reserva de Locales Musicales (SLM)

### Variables de entorno

Configurar las siguientes variables de entorno:

* `SECRET_KEY` , Secret Key de Django
* `DB_NAME` nombre de la base de datos
* `DB_USER` usuario de la base de datos
* `DB_HOST` servidor de base de datos
* `DB_PORT` puerto de la base de datos

Asignar `DJANGO_SETTINGS_MODULE` según corresponda:
- Desarrollo: `config.settings.dev`
- Testing/QA: `config.settings.test`
- Producción: `config.settings.prod`

## Pasos para despliegue

### Pycharm

Si se usa el IDE PyCharm crear una configuración de **Django server**, y establecer las variables de entorno.

Al finalizar la asignación de variables de entorno. Hacer clic en `Run`, por defecto lo despliega en `127.0.0.1:8000`

### Terminal/CMD

Si se despliega desde la terminal de Linux o linea de comandos de Windows, asignar las variables de entorno

Al finalizar la asignación de variables de entorno. Ejecutar el siguiente comando:

> python manage.py runserver --settings=config.settings.dev

El parámetro `settings` puede variar de acuerdo al entorno y si no ha sido configurado `DJANGO_SETTINGS_MODULE`

## Indicaciones de Desarrollo

### Antes de mandar PR

* **Flake 8**, Correr localmente `flake8 .` para verificar que no se esta teniendo incongruencias con el estilo establecido
* **Pruebas unitarias**, construir y correr las pruebas unitarias
* **Verificar base**, que se tenga como base el último commit de `master` en el `branch` que se va mergear, de lo contrario seguir los siguientes pasos:
  * `git checkout master`, ir a la rama master
  * `git pull origin master`, traer los últimos cambios de master
  * `git checkout [branch]`, ir al branch que se desea mergear
  * `git rebase master`, cambiar la base del branch al ultimo commit de master. Si hay conflictos, resolverlos; si no hay dominio en la herramienta Git, primero ejecutar `git rebase --abort` para evitar que se borre lo desarrollado, luego consultar a un compañero

Lo indicado anteriormente es para no tomar tiempo del revisor en casos obvios o redundantes

SFT © 2017
