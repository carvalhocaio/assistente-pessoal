from gtts import gTTS

tts = gTTS('Oi, eu sou a Sexta-Feira', lang='pt-br')
tts.save('audios/hello.mp3')
