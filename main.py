import re
import pywhatkit
import speech_recognition as sr
import pyttsx3
from datetime import datetime
import wikipedia
import Data_base_George
#usa a classe de conexao com o banco de dados que está em Data_base_George
Data_base_George.conectaBD()
# Busca_noticias.news
audio = sr.Recognizer()
maquina = pyttsx3.init()
def executa_comando():
    comando = ""
    try:
        with sr.Microphone() as source:
            print("Ouvindo...")
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-br')
            comando = comando.lower()
            if 'george' in comando:
                comando = comando.replace('george', '').strip()
                maquina.say(comando)
                maquina.runAndWait()
    except Exception as error:
        print(f"Erro ao reconhecer o comando: {error}")
    return comando
def aprender_conceito(conceito, explicacao):
    with open('conceitos.txt', 'a') as arquivo:
        arquivo.write(f'{conceito}: {explicacao}\n')
def explicar_conceito(conceito):
    with open('conceitos_matematicos.txt', 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            if linha.startswith(conceito + ':'):
                return linha.replace(conceito + ':', '').strip()
    return "Não sei esse conceito"
def comando_voz_usuario():
    comando = executa_comando()
    ## comando para a hora
    if 'horas' in comando or 'hora' in comando:
        hora = datetime.now().strftime('%H:%M')
        maquina.say('Agora são: ' + hora)
        maquina.runAndWait()
    ##comando para data
    elif 'data' in comando or 'dia do mes' in comando or 'hoje' in comando:
        data = datetime.now().strftime('%d/%m/%y')
        maquina.say("hoje é dia" + data)
        maquina.runAndWait()
    #comando para procurar conteudo
    elif 'quem é' in comando or 'george quem é' in comando or 'quem foi' in comando:
        procurar = comando.replace('quem é', '').strip().replace('quem foi', '').strip().replace('george quem é', '').strip()
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, sentences=2)
        maquina.say(resultado)
        maquina.runAndWait()
    #curiosidades
    elif 'procure por' in comando or 'o que é' in comando:
        procurar = comando.replace('procure por', '').strip()
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar, sentences=2)
        maquina.say(resultado)
        maquina.runAndWait()
        print(procurar)
    #comando para calcular
    elif 'quanto é' in comando or 'resultado de' in comando:
        regex = r'(\d+\s[-+/x]\s*\d+)'
        corresponde = re.search(regex, comando)
        if corresponde:
            corresponde = corresponde.group(0)
            corresponde = corresponde.replace('x', '*')
            resultado = eval(corresponde)
            maquina.say(resultado)
        else:
            error = 'Não encontrei algo passível de cálculo na sua fala, pode repetir?'
            maquina.say(error)
        maquina.runAndWait()
    #comando para tocar musicas no youtube
    elif 'toque' in comando or 'tocar' in comando:
        musica = comando.replace('toque', '').strip()
        pywhatkit.playonyt(musica)
        maquina.say("Reproduzindo " + musica + " no YouTube")
        maquina.runAndWait()
    elif 'aprender' in comando:
        partes = comando.replace('aprender', '').strip().split('é')
        if len(partes) == 2:
            conceito, explicacao = partes[0].strip(), partes[1].strip()
            aprender_conceito(conceito, explicacao)
            #isso conecta ao banco de dados
            direcaoBD = Data_base_George.conectaBD()
            cursor = direcaoBD.cursor()
            sql = "INSERT INTO conceito (assunto_conceito, explica_conceito) VALUES (%s, %s)"
            valor = (conceito, explicacao)
            cursor.execute(sql, valor)
            direcaoBD.commit()
            print(direcaoBD, "Adicionado no bd com sucesso")
            cursor.close()
            #fim enviar conceito aprendido para o banco de dados.
            maquina.say(f"Conceito aprendido com sucesso")
        else:
            maquina.say("Desculpe, não consegui aprender direito o conceito e a explicação. Por favor, diga-me o conceito e depois a explicação")
        maquina.runAndWait()
    elif 'explique' in comando or 'o que é' in comando:
        conceito = comando.replace('explique ', '').replace('o que é ', '').strip()
        explicacao = explicar_conceito(conceito)
        maquina.say(explicacao)
        maquina.runAndWait()
    elif 'noticias' in comando or 'ultimas noticias' in comando:
        import Busca_noticias
        nw = comando.replace('noticias', '').strip().replace('ultimas noticias').strip()
        nw = Busca_noticias().news
        maquina.say("Essas são as noticias: " + nw)
        maquina.runAndWait()
comando_voz_usuario()