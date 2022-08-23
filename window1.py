# -*- coding: utf-8 -*-
"""
Created on Sun May 15 13:33:48 2022

@author: Rafael
"""
import tkinter as tk 
import random
import datetime as date
import window2

class janela:
    
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("500x300")
        self.app.title("EuroMilhõ€s")
        
        bt1 = tk.Button(self.app, text="Gerar Chave do EuroMilhões",command=self.gerarChave)#Botão para gerar uma chave
        bt1.grid(column=0,row=1, padx=15, pady=15)
        
        lbl1 = tk.Label(self.app, text="Chaves Geradas")
        lbl1.grid(column=1,row=0, padx=15, pady=15)
        
        self.lista()
        
        bt2 = tk.Button(self.app, text="Ver todas as chaves geradas",command=self.verChaves)#Botão para a janela que tem todas as chaves geradas
        bt2.grid(column=0,row=2, padx=15, pady=15)

#Aqui abrimos a janela e definimos onde queremos os seus elementos posicionados     
        self.app.mainloop()#executa a app
        
        
    def lista(self):#Cira uma Listbox que recebe as chaves do EurosMilhões
        self.lst = tk.Listbox(self.app, width=45)
        self.lst.grid(column=1,row=1, padx=15, pady=15)
    
    def gerarChave(self):#Cria um dicionário com a Chave do EuroMilhões
        dic={"numeros:":[],"estrelas:":[]}
        combinacao=""
        while len(dic["numeros:"]) < 5:
            i=random.randint(1, 50)
            if i not in dic["numeros:"]:
                dic["numeros:"].append(i)
                combinacao+=str(i)+","#Adiciona os numeros a Variavel para depois ser imprimido no ficheiro
        while len(dic["estrelas:"]) < 2:
            i=random.randint(1, 12)
            if i not in dic["estrelas:"]:
                dic["estrelas:"].append(i)
                combinacao+=str(i)#Adiciona as estrelas a Variavel para depois ser imprimido no ficheiro
                if len(dic["estrelas:"]) < 2: combinacao+=","#utilização do if para não acabar com uma virgula
        self.lst.insert('end',dic)
        data = date.datetime.now()
        datastr = "{}/{}/{}".format(data.day, data.month,data.year) + " " + "{}:{}:{}".format(data.hour, data.minute, data.second)#formatação da data como pedida
        
        f = open("arquivo.txt","a")
        f.write(datastr +"," + combinacao+"\n")
        f.close()#Abre o ficheiro, escreve sempre que uma chave é gerada e fecha o ficheiro
     
    def verChaves(self):
        janela2.janela2()#Importa a janela das chaves geradas
         
a=janela()

#Projeto por Rafael Tavares, curso 8623 - B/22 - Fundamentos de Python       
