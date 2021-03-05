import speech_recognition as sr
from playsound import playsound
from requests import requests
from bs4 import BeautifulSoup

hotword = 'isa'

def monitora_audio():
    # obtain audio from the microphone
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Aguardando o comando: ")
            audio = microphone.listen(source)

            try:
                trigger = microphone.recognize_google(audio, language='pt-BR')
                trigger = trigger.lower()

                if hotword  in trigger:
                    print('Comando: ', trigger)
                    responde('feedback')
                    executa_comandos(trigger)
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recogniton Speech {e}")
    return trigger


def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')


def executa_comandos(trigger):
    if 'noticias' in trigger:
        ultimas_noticias()


def ultimas_noticias():
    site = get('https://news.google.com/rss?hl=pt-BR&gl=BR&ceid=BR:pt-419')
    noticias = BeautifulSoup(site.text, 'html.parser')
    for item in noticias.findAll('item')[:5]:
        mensagem = item.title.text
        print(mensagem)


def main():
    monitora_audio()

main()
