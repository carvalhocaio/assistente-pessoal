import speech_recognition as sr


def monitora_microfone():
    # obtain audio from the microphone
    microphone = sr.Recognizer()
    with sr.Microphone() as source:
        print("Aguardando o comando: ")
        audio = microphone.listen(source)

    try:
        print(microphone.recognize_google(audio, language='pt-BR'))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recogniton Speech {e}")
