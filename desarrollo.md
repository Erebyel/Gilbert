# Desarrollo de Gilbert

## Bibliotecas
Gilbert está desarrollado en Python3 y utiliza las bibliotecas:
- NumPy para algunas funciones (como crear los números aleatorios que se utilizarán para seleccionar las palabras de la lista,
- Pandas, para crear la tabla de palabras y
- Streamlit para el entorno en el que estás ejecutándolo.

## Datos de entrada
Gilbert utiliza un conjunto de datos en el que se almacenan los artículos, sujetos, verbos y adjetivos que utilizará para generar las frases y, también, para facilitar las palabras aleatorias. Los retos los almacena en un diccionario aparte.

A partir de ese diccionario, se generan diferentes funciones que permiten crear los diferentes componentes y comportamientos del programa.

## Funciones
### Creación de ideas

La primera función que creé fue **idea**, su lógica permite crear una frase articulada, aunque no la construye; su objetivo es seleccionar correctamente los elementos elegidos aleatoriamente por el sistema. Si son aleatorios, ¿importa qué seleccione? Pues sí, porque las palabras tienen géneros diferentes, no es lo mismo ***un elefante asombrado*** que ***una ardilla acaparadora***. Lo primero que hace la función es generar aleatoriamente tres números dentro del rango de datos total. Escoge un artículo y un sujeto según el primer número aleatorio y, luego, evalúa con un condicional el artículo elegido para seleccionar correctamente el género del adjetivo (que están cada uno en una columna diferente) y lo escoge según el segundo número aleatorio que se ha generado. En los dos casos, elige luego el verbo almacenado en *acciones*.

```
def idea():
    '''Genera una frase aleatoria que podrás utilizar como la idea principal del relato.
    El programa no utiliza ninguna lógica ni coherencia para la selección de las columnas,
    por lo que puedes enfrentarte a ideas bastante incoherentes; lo que puede resultar en
    un ejercicio bastante estimulante para la imaginación'''
    aleatorios = np.random.randint(len(frase['artículo']), size=3)
    if frase['artículo'][aleatorios[0]] == 'El':
        return ' '.join([frase['artículo'][aleatorios[0]], frase['sujeto'][aleatorios[0]], frase['adjetivo masculino'][aleatorios[1]], frase['acciones'][aleatorios[2]]])
    else:
        return ' '.join([frase['artículo'][aleatorios[0]], frase['sujeto'][aleatorios[0]], frase['adjetivo femenino'][aleatorios[1]], frase['acciones'][aleatorios[2]]])
```

### Creación de un listado de palabras aleatorias

Para complicar un poco el ejercicio, planteé que, además, existiera un número aleatorio de palabras que se tuviesen que utilizar en el texto. Para ello, la función **palabras** genera una lista aleatoria en la que puede aparecer entre 1 y 11 palabras; la razón del máximo es simple: el número 11 me gusta. Estas palabras se eligen aleatoriamente de la columna de adjetivos y, posteriormente, devuelve la lista convertida en un set para evitar las palabras duplicadas.

```
def palabras():
    '''Genera un listado de palabras aleatorio en base a adjetivos que debes utilizar en el
    desarrollo del texto; estas palabras pueden aparecer en todas sus variantes de género y número.'''
    palabras = []
    for n in range(int(np.random.randint(1, high=11, size=1))):
        palabras.append(frase['adjetivo masculino'][int(np.random.randint(len(frase['artículo']), size=1))])
    return set(palabras)
```

### Barajar y extraer un reto

El caso de los retos se trata aparte, no están en el conjunto original, sino que están formados por una lista guardada en una clave de diccionario para poder recuperar uno de forma aleatoria, que es lo que hace la siguiente función.

```
def reto():
    '''Lanza un reto aleatorio de los que existen dentro de la lista, para hacer más complicado
    (o facilitar a veces) la ejecución del relato.'''
    return retos['Retos'][int(np.random.randint(len(retos['Retos']), size=1))]
```

### Solicitar un elemento

En un principio, y para poder solicitar las tres funciones anteriores, creé la función **dice**, que llama y almacena en un diccionario las respuestas de las tres funciones anteriores. Por supuesto, esta función se quedaba corta para crear el juego y ejecutarlo en la web; así que le di otra vuelta y creé la función **juego**.

```
def dice():
    '''¡Devuelve la respuesta que ha generado Gilbert!'''
    return {'idea': idea(), 'palabras': palabras(), 'reto': reto()}
```

### Armando el juego

Al igual que **dice**, la función **juego** depende de las funciones anteriores, pero es más compleja que esta última ya que facilita la elección de la dificultad del juego y, según la dificultad elegida, devolverá solo la idea, la idea y el listado de palabras, o añadirá también el reto. Para su funcionamiento, **juego** requiere de un parámetro de entrada: fácil, normal o difícil; según el elegido recorrerá una estructura condicional que responderá a las diferentes dificultades. En la entrada, de no especificarse el nivel, el sistema se lo solicitará al usuario hasta que lo escriba correctamente.

```
def juego(nivel = ''):
    '''Elige el nivel de dificultad que tendrá la tarea de Gilbert: fácil, normal o difícil.'''

    while nivel not in ['fácil', 'normal', 'difícil']:
        nivel = input('Elige el nivel de dificultad: fácil, normal o difícil: ').lower()
    partida  = dice()
    if nivel == 'fácil':
        return idea()
    elif nivel == 'normal':
        return idea(), ', '.join(palabras())
    elif nivel == 'difícil':
        return idea(), ', '.join(palabras()), reto()
    else:
        return 'Parece que ha ocurrido algo inesperado.'
```
