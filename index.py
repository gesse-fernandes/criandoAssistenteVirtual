import speech_recognition as sr
import re
import pyttsx3 


nome = ""


while True:
    mic = sr.Recognizer()
   
    with sr.Microphone() as source:
            speek = pyttsx3.init()
            voices = speek.getProperty('voices')
            #engine.setProperty('voice', voices[].id)
            #print(voices[0].id)
            speek.setProperty('voice', voices[0].id)
            mic.adjust_for_ambient_noise(source=source)

            print("Vamos Começar fale Alguma Coisa....")

            audio = mic.listen(source=source)
            try:
                frase = mic.recognize_google(audio,language='pt-BR')
                
                if re.search(r'\b'+"ajuda"+r'\b',format(frase)):
                    speek.say("Ajuda")
                    speek.runAndWait()
                    
                    print("Algo relacionado a ajuda.")
                elif re.search(r'\b'+"meu nome é "+r'\b',format(frase)):
                    t = re.search('meu nome é (.*)',format(frase))
                    nome = t.group(1)
                    print("Seu nome é "+nome)
                    speek.say("Nome falado foi "+nome)
                    speek.runAndWait()

                print("Você falou: "+ frase)
                speek.say("você falou: "+format(frase))
                speek.runAndWait()
            except sr.UnknownValueError:
                print("Algo Deu errado")

