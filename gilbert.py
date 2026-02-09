
##---------------------- Carga de bibliotecas
from pathlib import Path

import pandas as pd
from pandas import DataFrame
import streamlit as st
import numpy as np

BASE_DIR = Path(__file__).resolve().parent

##---------------------- Base de datos
@st.cache_data
def load_frase():
    return pd.read_csv(BASE_DIR / 'data' / 'frase.csv', encoding='utf-8')

frase = load_frase()

retos = {'Retos': ['Yo no tengo muy claro que Ana tenga una ánfora, pero eso da igual, porque lo que sí sé es que tienes que hacer una anáfora', 'Alíviate o no te alivies, altérate o no te alteres, pero haz que tu texto sea aliterado', 'Qué paradójico sería que tu texto no tuviese una paradoja', 'Era como… la descripción que has hecho. Ex-ac-ta-men-te', 'Este reto es un alivio, te permite la elipsis de 1 palabra que te haya salido como obligatoria para tu texto. Elige sabiamente', 'Este reto es un alivio, te permite la elipsis de 2 palabras que te hayan salido como obligatorias para tu texto. Elige sabiamente', 'Este reto es un alivio, te permite la elipsis de 3 palabras que te hayan salido como obligatorias para tu texto. Elige sabiamente', 'Este reto es un alivio, te permite la elipsis de 4 palabras que te hayan salido como obligatorias para tu texto. Elige sabiamente', '¿Quién conoce el futuro? Bueno, pues tendrás que imaginártelo', 'Me da igual que tengas que incluir una lavadora, tu texto debe enmarcarse en la época clásica', 'Me importa poco que tu protagonista sea una impresora 3D, tus protagonistas están en la Edad Media', 'En una época donde existía la magia… tu texto estaría en su contexto correcto', 'Si no te ríes al leerlo, no molas porque no es comedia', 'Seguro que, gracias a tu emotiva oda, el protagonista de tu historia será recordado eternamente', 'Ni Ulises está a la altura de tu epopeya', 'Don Quijote estaría orgulloso de tu aporte al noble arte de las historias de caballería', '¿A quién no le gusta viajar? Nos vamos a visitar otro planeta en este viaje intergaláctico', '¿Has soñado con viajes en el tiempo? Quién no…', '¿Estás preparado? Te vas a embarcar en un camino del héroe', 'Los escritores a veces parece que no saben hacerlo, yo que sé… mira, tú usa frases simples porque no puedes usar  yuxtaposiciones ni subordinadas ni coordinadas.', '¡Te has librado! Eres libre de restricciones', 'Perdona, pero no me equivoqué al decir que tenías que escribir una antanaclasis', 'Este aire suena como una sinestesia, ¿no os parece?', 'No es dislexia, es un sinécdoque, ¡que no te enteras!', '¡Te has librado! Eres libre de restricciones', '¡No corras tanto! No puedes escribir más de 50 palabras', '¡No corras tanto! No puedes escribir más de 100 palabras', '¡No corras tanto! No puedes escribir más de 150 palabras', 'Tic-Tac Solo tienes 10 minutos para escribir ¡Rápido!', 'Y dije… que tu texto sea un diálogo', '¿No es verdad, ángel de amor, que en verso se escribe mejor?', 'Tiene que parecer un ensayo, no serlo, porque de esto sé que no tienes ni idea', 'A ver, no te alarmes, pero debes hacer una metáfora con lo que tengas', '¿Cuántas líneas tiene ese papel? Bueno, pues como mucho, puedes llenar 20 líneas', '¿Cuántas líneas tiene ese papel? Bueno, pues como mucho, puedes llenar 30 líneas', '¿Cuántas líneas tiene ese papel? Bueno, pues como mucho, puedes llenar 40 líneas', 'La prosa ha muerto, escríbeme un poema', 'Esta es difícil. Tu protagonista es ahora el antagonista… debe ser una tragedia, porque triunfa frente al bien', 'Esto es como cuando tienes que hacer un símil…', 'Tu protagonista se convierte en un lema del diccionario, ahora tienes que definirlo sin nombrarlo en ningún momento', 'Me apetece escuchar esa canción, sí, ya sabes… la que acabas de escribir', 'Los mitos griegos molan mucho, haz que el tuyo pueda colar por uno.', 'Encuentras la hoja de una novela durante un paseo matutino, ¿qué tiene escrito? ¿Podrías trascribirlo para mi?', 'Sepa vuesa merced que vuestras palabras suenan tan cercanas para alguien de mi uso, gracias por escribir unas líneas en castellano antiguo', 'Edgar Allan Poe no existe, ¿quién va a decirnos ahora "nunca más"?', 'Ni el señor gray está a la altura de tu perversión, haz que se corra (la tinta, la tinta)', 'Esto es un tema serio, te lo ha pedido un catedrático para la clase que tiene mañana.', 'Con la venia de su señoría, esa ley que usted cita y describe todavía no la he encontrado en el Código Civil.', 'A Spielberg le ha encantado tu idea, pero lo que has escrito solo da para un corto.', 'Más te vale que tu historia tenga una moraleja']}

##---------------------- Funciones
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

def palabras():
    '''Genera un listado de palabras aleatorio en base a adjetivos que debes utilizar en el
    desarrollo del texto; estas palabras pueden aparecer en todas sus variantes de género y número.'''
    palabras = []
    for n in range(int(np.random.randint(1, high=11, size=1))):
        palabras.append(frase['adjetivo masculino'][int(np.random.randint(len(frase['artículo']), size=1))])
    return set(palabras)

def reto():
    '''Lanza un reto aleatorio de los que existen dentro de la lista, para hacer más complicado
    (o facilitar a veces) la ejecución del relato.'''
    return retos['Retos'][int(np.random.randint(len(retos['Retos']), size=1))]

def dice():
    '''¡Devuelve la respuesta que ha generado Gilbert!'''
    return {'idea': idea(), 'palabras': palabras(), 'reto': reto()}

def juego(nivel = ''):
    '''Elige el nivel de dificultad que tendrá la tarea de Gilbert: fácil, normal o difícil.'''

    nivel = (nivel or '').lower()
    if nivel not in ['fácil', 'normal', 'difícil']:
        nivel = 'fácil'
    if nivel == 'fácil':
        return idea()
    elif nivel == 'normal':
        return idea(), ', '.join(palabras())
    elif nivel == 'difícil':
        return idea(), ', '.join(palabras()), reto()
    else:
        return 'Parece que ha ocurrido algo inesperado.'

##---------------------- Objetos externos
with (BASE_DIR / 'reglas.md').open("r", encoding="utf-8") as texto:
    reglas = texto.read()
with (BASE_DIR / 'sobre_proyecto.md').open("r", encoding="utf-8") as texto:
    sobre_proyecto = texto.read()
with (BASE_DIR / 'desarrollo.md').open("r", encoding="utf-8") as texto:
    desarrollado = texto.read()

##---------------------- Aplicación Streamlit
##--- Textos
st.title('Gilbert.dice')
st.header('Generador de frases aleatorias')
st.markdown('### Podrás utilizarlas para inspirarte, trabajar la imaginación y perder el miedo a la página en blanco.')

##--- Menú de la izquierda
st.sidebar.title("Acepta el reto y pincha en comenzar")
st.sidebar.write('Elige la dificultad y enfréntate a la página en blanco.')
fichero = st.sidebar.selectbox("Selecciona la dificultad:",('fácil', 'normal', 'difícil'))

#--   Botones
comenzar = st.sidebar.button('Generar')
saber_mas = st.sidebar.button('Reglas del juego')
proyecto = st.sidebar.button('Detalles del proyecto')
desarrollo = st.sidebar.button('Desarrollo de Gilbert')

##--- Rutina del programa
if comenzar:
    gilbert = juego(fichero)
    if fichero == 'fácil':
        st.markdown('La idea para tu próximo relato es:')
        st.markdown('**' + gilbert + '**\n')
    elif fichero == 'normal':
        st.markdown('La idea para tu próximo relato es:')
        st.markdown('**' + gilbert[0] + '**\n')
        st.markdown('El texto debe incluir estas palabras:')
        st.markdown('**' + gilbert[1] + '**\n')
    else:
        st.markdown('La idea para tu próximo relato es:')
        st.markdown('**' + gilbert[0] + '**\n')
        st.markdown('El texto debe incluir estas palabras:')
        st.markdown('**' + gilbert[1] + '**\n')
        st.markdown('Además, debes tratar de cumplir con el siguiente reto:')
        st.markdown('**' + gilbert[2] + '**\n')

if saber_mas:
    st.markdown(reglas)

if proyecto:
    st.markdown(sobre_proyecto)

if desarrollo:
    st.markdown(desarrollado)

##--- Pie del menú de la izquierda
st.sidebar.markdown('Un proyecto personal de [**Erebyel** (María Reyes Rocío Pérez)](http://www.erebyel.es).')
