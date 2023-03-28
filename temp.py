#Libreria
import streamlit as st
import time
import os

# Set the wide modo on default
st.set_page_config(page_title="Proyectos Computer Vision",
                   page_icon="👀",
                   layout="wide",
                   initial_sidebar_state="expanded")

# UI
st.sidebar.title("Proyectos de Computer Vision 👀")
st.sidebar.write("El objetivo es probar distintas demos de proyectos de CV basados en yolov8/yolov7. 💡")

# Opciones de Modelos 
genre = st.sidebar.selectbox(
    "Selecciona el modelo de CV: ⏬",
    ('Human Pose', 'Fire Detection', 'Drowsiness', 'Emotion Detection'))

# ,'Count and Tracking', 'Track Across Cameras', 'Satelital Images'

# Select resources
Folder= {'hp':'Human Pose', 'fd':'Fire Detection', 'dw':'Drowsiness',
      'cat':'Count and Tracking', 'tic':'Track in Cameras', 'ed':'Emotion Detection',
      'sat': 'Satelital Images'}

# Get the gender video directory 
def get_vid_dir(gender):
    dictionary=[]

    for key, value in Folder.items():
        if value==gender:
            dictionary= key
    return dictionary
viddir=get_vid_dir(gender=genre)

###########################################################################
# Get routes to acces files
# 🔴🔴🔴🔴🔴 Al ejecutar el file esta ruta debe concidir con con el shell donde se ejecuto 🔴🔴🔴🔴🔴🔴🔴
oldpath= "/app/cv_demos"

folder=  oldpath + "/" + "vidsource" + "/" + viddir 
os.chdir(folder)
folderoot= os.getcwd()
opt= os.listdir()
folinput= folderoot + "/" + opt[1]
folout= folderoot + "/" + opt[0]

# Get the list of videos in input folder
os.chdir(folinput)
optin= os.listdir()

def get_subroots_in(opciones):
    return folinput + "/" + opciones
listas_in=  list(map(get_subroots_in, optin))

# Get the list of videos in output folder
os.chdir(folout)
optout= os.listdir()

def get_subroots_ot(opciones):
    return folout + "/" + opciones
listas_ot=  list(map(get_subroots_ot, optout))

# Reset path 
os.chdir(oldpath)

###########################################################
# Select the options between samples, or camera and samples.

if genre in ('Fire Detection','Human Pose', 'Drowsiness', 'Emotion Detection'):
    Opciones= st.sidebar.selectbox('Selecciona el video muestra: ⏬',options=optin)
else:
    Type= st.sidebar.radio('Selecciona el input: ⏬', ('Muestras', 'Cámara'),horizontal=True)

if genre in ('Fire Detection' ,'Human Pose', 'Drowsiness', 'Emotion Detection'):
    avi= st.write('')
else:
    notavi= st.image("/app/cv_demos/const.jpg")

# Get index position
# Funciona pq el orden de los inputs y outs es el mismo
#               🔴Cambiar  al agregar más variables🔴      ######
if genre in ('Fire Detection','Human Pose', 'Drowsiness', 'Emotion Detection'):
    posinout=optin.index(Opciones)
else:
    pass

###################################################
if st.sidebar.button('Crear'):
    st.write(f'El video del modelo {genre} se puede ver debajo:')

    col1,col2 = st.columns(2)

    video_file1 = open(listas_in[posinout], 'rb')
    video_bytes1 = video_file1.read()
    col1.video(video_bytes1)

    with st.spinner('Wait for it...'):
        time.sleep(3)
    video_file2 = open(listas_ot[posinout], 'rb')
    video_bytes2 = video_file2.read()
    col2.video(video_bytes2)
    col2.success('Done!')

else:
    st.write('')
