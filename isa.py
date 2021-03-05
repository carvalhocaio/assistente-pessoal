import speech_recognition as sr
from playsound import playsound

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
                    ### executar os comandos
                    break

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    f"Could not request results from Google Speech Recogniton Speech {e}")
    return trigger


def responde(arquivo):
    playsound('audios/' + arquivo + '.mp3')


def main():
    monitora_audio()

main()
