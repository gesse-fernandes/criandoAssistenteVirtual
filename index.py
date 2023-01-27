import speech_recognition as sr

mic = sr.Recognizer()

with sr.Microphone() as source:
        mic.adjust_for_ambient_noise(source=source)

        print("Vamos Começar fale Alguma Coisa....")

        audio = mic.listen(source=source)

        try:
            frase = mic.recognize_google(audio,language='pt-BR')
            print("Você falou: "+ frase)
        except sr.UnknownValueError:
            print("Algo Deu errado")