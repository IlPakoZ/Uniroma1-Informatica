# -*- coding: utf-8 -*-
"""
Created on Fri Nov 22 10:41:49 2019

@author: xJ0T3
"""

import math

class Gatto:
    
    super_saiyan = False
    morto = False
    vita = 100
    potere = 1
    vite = 7
    
    def __init__(self):
        pass
    def miagola(self):
        if not self.morto:
            if self.super_saiyan:
                return "Super Miao!"
            if self.potere == math.inf:
                return "I gatti immortali non hanno bisogno di miagolare!!"
            return "Miao"
        else:
            return "I gatti morti non miagolano"
    
    def picchia(self, danno):
        if (self.morto):
            print("Non puoi picchiare i gatti morti!")
        elif (self.vita - danno <= 0 and danno > self.potere):
            self.vita = 0
            self.uccidi()
            print("Ahia, mi hai ucciso!")
        elif (self.vita - danno > 0 and danno > self.potere):
            self.vita -= danno
            print(f"Maledetto, mi hai fatto {danno} di danno!")
        elif (danno < self.potere):
            print("HAHA! Il mio potere è troppo alto!")
        elif (danno == self.potere):
            print("Sei un degno avversario!")
        if (self.super_saiyan):
            if self.vita < 200//15:
                print("Sono sfinito! Non sono più super saiyan!")
                self.super_saiyan = False
                self.potere = 1
                
    def diventaSuperSaiyan(self):
        if (not self.super_saiyan and not self.morto):
            self.vita += 100
            self.super_saiyan = True
            self.potere = 50
            self.vite += 1
            print("WAAAA! Mi illumino d'immenso!")
        else:
            print("Sono già super saiyan!")
            
    def diventaGorla(self):
        if not self.morto:        
            self.potere = math.inf
            self.vita = math.inf
            print("So, this is the power of ultra instinct?")
        print("Dio è morto! - cit. Nietzche")
        
    def setVita(self,vita):
        if not self.morto:
            self.vita = vita
        
    def resuscita(self):
        if (self.morto):
            self.morto = False
            self.vita = True
            self.vite = 7
            print("Che bello, adesso sono vivo!")
        else:
            print("Sono già vivo! E' una predizione questa?")
     
    def getPotere(self):
        if (self.potere == math.inf):
            return f"Stupido mortale, non puoi farmi niente! Il mio potere è infinito!"
        return f"Il mio potere è {self.potere}!"
    
    def getVita(self):
        if (self.vita == math.inf):
            return f"Stupido mortale, non puoi farmi niente! La mia vita è infinita!"
        return f"Mi rimangono {self.vita} punti vita!!"
    
    def infarto(self):
        for i in range(self.vite):
            self.uccidi()
        
    def uccidi(self):
        if (self.potere == math.inf):
            print("Non puoi uccidere un essere immortale.")
            return
        if self.vite > 0: 
            self.vite -= 1
            self.vita = round(100 * (1/(7-self.vite)))
            self.potere = 1
            self.super_saiyan = False
            if self.vite == 0:
                self.vita = 0
                self.potere = 0
                self.morto = True
                print("Sono morto...")
            else:
                print(f"AHAH, mi rimangono ancora {self.vite} vite!")
            return
        self.vita = 0
        self.super_saiyan = False
        self.morto = True
        self.potere = 0
        
