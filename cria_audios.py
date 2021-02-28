from gtts import gTTS
from playsound import playsound # for Windows
#from subprocess import call # for OSX and Linux


def cria_audio(audio):
    tts = gTTS(audio, lang='pt-br')
    tts.save('audios/bem_vindo.mp3')

    playsound('audios/bem_vindo.mp3') # for Windows
    #call(['afplay', 'audios/hello.mp3']) # for OSX
    #call(['aplay', 'audios/hello.mp3']) # for Linux


cria_audio('Olar, eu sou a Isa')
