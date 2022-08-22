# -*- coding: utf-8 -*-
"""
Created on Mon May 16 23:22:29 2022

@author: Rafael
"""

import tkinter as tk

class janela2:
    
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry("400x200")
        self.app.title("Chaves Geradas")
        self.lista()
        self.lerfic()
        
        
    def lista(self):#Cira uma Listbox que recebe as chaves da função lerfic
        self.lst = tk.Listbox(self.app, width=60)
        self.lst.grid(column=0,row=0, padx=15, pady=15)
        
        
    def lerfic(self):
        f = open("arquivo.txt","r")
        for e in f:
            self.lst.insert('end',e)
        f.close()
        #Le o ficheiro e insere na Listbox
