# Django + Unit Testing + Selenium + BDD

Como he visto que tenéis problema para saber dónde y cómo definir los tests que tenéis os pongo este proyecto de un login sencillo para que veáis dónde poner cada test.

## Test Unitarios

Estos tests van por `aplicación`. En este caso la aplicación es `login`. En el caso de las prácticas sería una mezcla entre lo que ya habéis hecho en prácticas pasadas y lo nuevo que hacéis para que aparezca el HTML.

Para generar una app podéis usar:
```
python manage.py startapp login
```

y una vez creado añadir el código de prácticas pasadas ahí.

Si miráis hay un fichero `tests.py`. En Django hay varias formas de poner/usar los tests. Por defecto se escriben por aplicación y están en ese directorio (aunque puedes sacarlo a una carpeta tests en el root del proyecto).

Os he dejado dos tests tontos aquí para que los veáis.

Para ejecutar los tests sería con:
```
python manage.py test
```

## Tests Funcionales (BDD + Selenium)

Los he hecho con Behave y están en una carpeta llamada `features`. He añadido dentro de `bdd_example/settings.py` 'behave_django' como app para que el proyecto lo pueda usar.

Aquí podéis ver ficheros `.feature` que son BDD y su implementación dentro de `features/steps/login.py`. La configuración para que use Chrome, Firefox o lo que sea lo hago dentro de `features/environment.py`

Estos tests se ejecutan diferente, en mi caso es:

```
python manage.py behave
```

## Otras consideraciones

He crado un directorio `tests` en el root del proyecto. Aquí podrían ir los tests pero por simplificar no los he metido ahí. Lo único que podéis ver ahí son cosas "comunes" a los tests (en mi caso lo uso para rellenar la base de datos durante las pruebas nada más).