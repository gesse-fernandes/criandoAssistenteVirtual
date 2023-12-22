import speech_recognition as sr
import re
import pyttsx3 
import os
import requests
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
            speek.say("Vamos Começar fale Alguma Coisa")
            speek.runAndWait()
            audio = mic.listen(source=source)
            try:
                frase = mic.recognize_google(audio,language='pt-BR')
                
                if re.search(r'\b'+"gostaria de saber os preços da Ceasa de Tianguá"+r'\b',format(frase)):
                    r = requests.get("https://contweb.net.br/ceasa-es-server/api/cotacaoGeralFrutasTiangua", verify=True ,headers={'User-Agent': "Magic Browser"})
                    prices = r.json()
                    tam = len(prices)
                    i =0
                    while i < tam:

                        speek.say("O nome é "+ format(prices[i]["nome"]))
                        speek.runAndWait()
                        speek.say("o Preço minimo é "+ format(prices[i]["min"]))
                        speek.runAndWait()
                        speek.say("o Preço médio é "+ format(prices[i]["mc"]))
                        speek.runAndWait()
                        speek.say("o Preço Máximo é "+ format(prices[i]["max"]))
                        speek.runAndWait()
                             

                        i+=1

                    
                    print("Algo relacionado a ajuda.")
                
                elif re.search(r'\b'+"meu nome é "+r'\b',format(frase)):
                    t = re.search('meu nome é (.*)',format(frase))
                    nome = t.group(1)
                    print("Seu nome é "+nome)
                    speek.say("Nome falado foi "+nome)
                    speek.runAndWait()
                elif re.search(r'\b'+"programa"+r'\b',format(frase)):
                   speek.say("você encerrou")
                   speek.runAndWait()
                   os._exit(0)

                print("Você falou: "+ frase)
                speek.say("você falou: "+format(frase))
                speek.runAndWait()
            except sr.UnknownValueError:
                print("Algo Deu errado")

