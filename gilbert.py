
##---------------------- Carga de bibliotecas
from pathlib import Path

import pandas as pd
from pandas import DataFrame
import streamlit as st
import numpy as np

st.set_page_config(page_title="Gilbert.dice", page_icon="📝", layout="centered")

BASE_DIR = Path(__file__).resolve().parent

##---------------------- Base de datos
@st.cache_data
def load_frase():
    return pd.read_csv(BASE_DIR / 'data' / 'frase.csv', encoding='utf-8')

@st.cache_data
def load_retos():
    return pd.read_csv(BASE_DIR / 'data' / 'retos.csv', encoding='utf-8')

frase = load_frase()
retos = load_retos()

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
    for _ in range(np.random.randint(1, high=11)):
        palabras.append(frase['adjetivo masculino'][np.random.randint(len(frase['artículo']))])
    return set(palabras)

def reto():
    '''Lanza un reto aleatorio de los que existen dentro de la lista, para hacer más complicado
    (o facilitar a veces) la ejecución del relato.'''
    return retos['Retos'][np.random.randint(len(retos['Retos']))]

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
st.markdown(
    """
    <style>
    .main-title {font-size: 2.6rem; font-weight: 800; margin-bottom: 0.2rem;}
    .subtitle {font-size: 1.15rem; color: #4f4f4f; margin-bottom: 1.5rem;}
    .section-title {font-size: 1.2rem; font-weight: 700; margin-top: 1.2rem;}
    .card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 1rem 1.2rem;
        box-shadow: 0 6px 18px rgba(15, 23, 42, 0.08);
        margin: 0.6rem 0 1rem 0;
        color: #111827;
    }
    .card h1,
    .card h2,
    .card h3,
    .card h4,
    .card h5,
    .card h6,
    .card p,
    .card li,
    .card strong,
    .card em,
    .card a {
        color: #111827;
    }
    .highlight {
        font-size: 1.05rem;
        font-weight: 600;
        color: #111827;
    }
    .chip {
        display: inline-block;
        background: #eef2ff;
        color: #3730a3;
        font-weight: 600;
        padding: 0.2rem 0.6rem;
        border-radius: 999px;
        font-size: 0.85rem;
        margin-right: 0.35rem;
        margin-bottom: 0.35rem;
    }
    .sidebar-note {
        font-size: 0.9rem;
        color: #6b7280;
        margin-top: 0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

##--- Textos
st.markdown('<div class="main-title">Gilbert.dice</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generador de frases aleatorias para inspirarte, trabajar la imaginación y perder el miedo a la página en blanco.</div>', unsafe_allow_html=True)

#--   Botones
proyecto = st.sidebar.button('ℹ️ Detalles del proyecto')
desarrollo = st.sidebar.button('🛠️ Desarrollo de Gilbert')
st.sidebar.divider()
mostrar_reglas = st.sidebar.button('📜 Reglas del juego')

##--- Rutina del programa
def guardar_resultado(nivel):
    st.session_state["gilbert_nivel"] = nivel
    st.session_state["gilbert_resultado"] = juego(nivel)

def mostrar_resultado():
    nivel = st.session_state.get("gilbert_nivel")
    gilbert = st.session_state.get("gilbert_resultado")
    if not nivel or not gilbert:
        return
    st.markdown('<div class="section-title">La idea para tu próximo relato</div>', unsafe_allow_html=True)
    if nivel == 'fácil':
        st.markdown(f'<div class="card"><div class="highlight">{gilbert}</div></div>', unsafe_allow_html=True)
        return
    st.markdown(f'<div class="card"><div class="highlight">{gilbert[0]}</div></div>', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Palabras obligatorias</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="card">' + ''.join(f'<span class="chip">{palabra}</span>' for palabra in gilbert[1].split(", ")) + '</div>',
        unsafe_allow_html=True,
    )
    if nivel == 'difícil':
        st.markdown('<div class="section-title">Reto adicional</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="card"><div class="highlight">{gilbert[2]}</div></div>', unsafe_allow_html=True)

if "panel_activo" not in st.session_state:
    st.session_state["panel_activo"] = "reglas"

if proyecto:
    st.session_state["panel_activo"] = "proyecto"

if desarrollo:
    st.session_state["panel_activo"] = "desarrollo"

control_col1, control_col2 = st.columns([3, 1.4])
with control_col1:
    fichero = st.radio(
        "Selecciona la dificultad:",
        ('fácil', 'normal', 'difícil'),
        horizontal=True,
        label_visibility="collapsed",
    )
with control_col2:
    comenzar = st.button('🎲 Descubre una nueva idea')

if comenzar:
    guardar_resultado(fichero)
    
if mostrar_reglas:
    st.session_state["panel_activo"] = "reglas"

mostrar_resultado()

st.divider()

if st.session_state["panel_activo"] == "proyecto":
    st.markdown('<div class="card">' + sobre_proyecto + '</div>', unsafe_allow_html=True)
elif st.session_state["panel_activo"] == "desarrollo":
    st.markdown('<div class="card">' + desarrollado + '</div>', unsafe_allow_html=True)
else:
    st.markdown('<div class="card">' + reglas + '</div>', unsafe_allow_html=True)

##--- Pie del menú de la izquierda
st.sidebar.markdown('Un proyecto personal de [**Erebyel**](http://www.erebyel.es).')
