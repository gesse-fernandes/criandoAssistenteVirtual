import speech_recognition as sr
import re
nome = ""
while True:
    mic = sr.Recognizer()

    with sr.Microphone() as source:
            mic.adjust_for_ambient_noise(source=source)

            print("Vamos Começar fale Alguma Coisa....")

            audio = mic.listen(source=source)

            try:
                frase = mic.recognize_google(audio,language='pt-BR')
                if re.search(r'\b'+"ajudar"+r'\b',format(frase)):
                    print("Algo relacionado a ajuda.")
                elif re.search(r'\b'+"Meu nome é "+r'\b',format(frase)):
                    t = re.search('meu nome é (.*)',format(frase))
                    nome = t.group(1)
                    print("Seu nome é "+nome)

                print("Você falou: "+ frase)
            except sr.UnknownValueError:
                print("Algo Deu errado")