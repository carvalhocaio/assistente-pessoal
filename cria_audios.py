from gtts import gTTS
from playsound import playsound # for Windows
#from subprocess import call # for OSX and Linux


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/comando_invalido.mp3')

    playsound('audios/comando_invalido.mp3') # for Windows
    #call(['afplay', 'audios/hello.mp3']) # for OSX
    #call(['aplay', 'audios/hello.mp3']) # for Linux


cria_audio('Desculpe, mas não posso fazer isso...')
