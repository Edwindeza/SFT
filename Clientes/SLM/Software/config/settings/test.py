from .base import *  # noqa


STATIC_ROOT = os.path.join(BASE_DIR, 'apps', 'static')  # NOQA
# Usado debido a que cuando se corren los tests se requiere acceder
# a los archivos estaticos
