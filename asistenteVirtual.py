from selenium import webdriver
import time
#del speech reconition se importan los modulos que son el microfono, reconizer etc
#en google puedo encontrar que contiene speech y como usarlo
from speech_recognition import Microphone, Recognizer, AudioFile, UnknownValueError, RequestError
from gtts import gTTS
from playsound import playsound
import random
#from pyaudio import PyAudio

validaAuth = False
browser = webdriver


def validaQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True

def buscarChat(nombreChat : str):
    print("Buscando chat : ", nombreChat)
    elements = browser.find_element_by_tag_name("spam")
    for element in elements:
        print("Chat encontrado : " + str(element.text).lower())
        if element.text != '' and nombreChat.__contains__(str(element.text).lower):
            element.click()
    print("Chat no encontrado")
        
def escribir(texto):
    print("escribiendo...")
    cajitaDeTexto = browser.find_element_by_xpatch('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
    cajitaDeTexto.send_keys(texto)
    

def enviar():
    print("enviado...")
    enviar = browser.find_element_by_xpatch('//*[@id="main"]/footer/div[1]/div[3]')
    enviar.click()
    
def bootWhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)
    
    espera = True
    print("Autenticate por favor")
    
    while espera:
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            global validaAuth
            validaAuth = True
            print("Se autenticó")
            break
        
def activarAsistente():
    escuchar()
    while True:
        time.sleep(1)

def escuchar():
    print("Escuchando...")
    recognizer = Recognizer()
    microfono = Microphone() 
    
    with microfono:
        recognizer.adjust_for_ambient_noise(microfono)
        
    recognizer.listen_in_background(microfono, callback)
    
def callback(recognizer, source):
    print("Reconociendo...")
    
    try:
        reconocer = recognizer.recognize_google(source, language='es-ES')
        texto = str(reconocer).lower()
        print("Escuche : ", texto)
        if(texto.__contains__("Monica")):
            print("Llamo a Monica")
            texto = texto.replace("Monica", "")
            accion(texto)
            return
        
    except RequestError as exc:
        print("Error al escuchar : ", exc)
    except UnknownValueError:
        print("No entendi :c")
        playsound('./Resource/errorRespuesta.mp3')
        time.sleep(1)
           
def accion(texto: str):
    
    print("Reconociendo accion...")    
    
activarAsistente()
  
            