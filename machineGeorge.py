import re 
import pywhatkit
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import Data_base_George
from transformers import AutoModelForCausalLM, AutoTokenizer

# Inicializa reconhecimento de fala:

audio =  sr.Recognizer()
maquina = pyttsx3()


# conecta ao bd
Data_base_George.conectaBD()

# carregando o modelo da hugging
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelForCausalLM.from_pretrained('gpt2')

def gerar_resposta(prompt):
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(inputs['input_ids'], max_length=100, num_return_sequence=1)
    resposta = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return resposta

def executa_comando():
    comando = ""
    
    try:
        with sr.Microphone() as source:
            print("ouvindo")
            voz = audio.listen(source)
            comando = audio.recognize_amazon(voz, lenguage='pt-br')
            comando = comando.lower()
            
            if 'george' in comando:
                comando = comando.replace('george', "").strip()
                maquina.say(comando)
                maquina.runAndWait()
    except Exception as erro:
        maquina.say("erro ao reconhecer o comando: {erro}")
    return comando


def aprender_conceito(conceito, explicacao):
    with:
        