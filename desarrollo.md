Gilbert está desarrollado en Python 3 y utiliza las siguientes bibliotecas:

- **NumPy**, para generar los números aleatorios con los que se seleccionan las palabras.
- **Pandas**, para construir la tabla de datos que contiene artículos, sujetos, verbos y adjetivos.
- **Streamlit**, como entorno de ejecución.

## Datos de entrada
Gilbert trabaja con un conjunto de datos que almacena artículos, sujetos, verbos y adjetivos. Con ellos genera tanto las frases como las palabras aleatorias que deben incorporarse al texto. Los retos se guardan en un diccionario independiente.

A partir de estos datos se construyen las funciones que dan forma a los distintos comportamientos del programa.

## Funciones

### Creación de ideas

La primera función que desarrollé fue **idea**. Su lógica permite construir una frase gramaticalmente coherente a partir de elementos seleccionados al azar. Aunque la elección es aleatoria, el orden y el género sí importan: no es lo mismo *un elefante asombrado* que *una ardilla acaparadora*.

La función genera tres números aleatorios dentro del rango de datos. Con el primero selecciona el artículo y el sujeto. A partir del artículo elegido, evalúa el género para escoger el adjetivo correspondiente desde la columna adecuada. El tercer número determina el verbo.

¿Podría haber hecho esto con una IA? Sí, podría haber usado un agente, pero el tema es conseguir un sistema funcional y óptimo para lo que se busca, sin gastar demasiados recursos, vamos.

```
python
def idea():
    '''Genera una frase aleatoria que podrás utilizar como la idea principal del relato.
    El programa no utiliza ninguna lógica ni coherencia para la selección de las columnas,
    por lo que puedes enfrentarte a ideas bastante incoherentes; lo que puede resultar en
    un ejercicio bastante estimulante para la imaginación'''
    aleatorios = np.random.randint(len(frase['artículo']), size=3)
    if frase['artículo'][aleatorios[0]] == 'El':
        return ' '.join([frase['artículo'][aleatorios[0]],
                         frase['sujeto'][aleatorios[0]],
                         frase['adjetivo masculino'][aleatorios[1]],
                         frase['acciones'][aleatorios[2]]])
    else:
        return ' '.join([frase['artículo'][aleatorios[0]],
                         frase['sujeto'][aleatorios[0]],
                         frase['adjetivo femenino'][aleatorios[1]],
                         frase['acciones'][aleatorios[2]]])
```

### Creación de un listado de palabras aleatorias
Para añadir complejidad, la función palabras genera un conjunto de entre 1 y 11 palabras que deben aparecer en el texto. El máximo es 11 por preferencia personal. Las palabras se toman de la columna de adjetivos y se devuelven como un set para evitar duplicados.

```
python
def palabras():
    '''Genera un listado de palabras aleatorio en base a adjetivos que debes utilizar en el
    desarrollo del texto; estas palabras pueden aparecer en todas sus variantes de género y número.'''
    palabras = []
    for n in range(int(np.random.randint(1, high=11, size=1))):
        palabras.append(frase['adjetivo masculino']
                        [int(np.random.randint(len(frase['artículo']), size=1))])
    return set(palabras)
```

### Barajar y extraer un reto
Los retos se almacenan en una lista dentro de un diccionario. La función reto recupera uno de forma aleatoria.

```
python
def reto():
    '''Lanza un reto aleatorio de los que existen dentro de la lista, para hacer más complicado
    (o facilitar a veces) la ejecución del relato.'''
    return retos['Retos'][int(np.random.randint(len(retos['Retos']), size=1))]
```

### Solicitar un elemento
La función dice agrupa las tres funciones anteriores y devuelve sus resultados en un diccionario.

```
python
def dice():
    '''¡Devuelve la respuesta que ha generado Gilbert!'''
    return {'idea': idea(), 'palabras': palabras(), 'reto': reto()}
```

### Armando el juego
La función juego organiza la experiencia completa. Según el nivel de dificultad elegido, devuelve solo la idea, la idea con las palabras, o la idea con palabras y reto.
Si no se especifica un nivel válido, el sistema lo solicita al usuario hasta recibir una opción correcta.

```
python
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

**Actualización 2026:** Algunas de estas funciones vienen del planteamiento original, pueden haber variado en la revisión hecha en febrero de 2026; pero la esencia del funcionamiento se mantiene.
