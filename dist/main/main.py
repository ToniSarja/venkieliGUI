from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import random
from kivy.uix.progressbar import ProgressBar
import csv
import pandas as pd

Builder.load_file('kielioppi/ruutu.kv')

class Osio(Screen):

    def valikko(self):
        self.manager.current = "subosio"  
    
    def valikko2(self):
        self.manager.current = "kyr"

    def valikko3(self):
        self.manager.current = "verbiosio"

    def valikko4(self):
        self.manager.current = "adjosio"
    
    def valikko5(self):
        self.manager.current = "pron"
    
    def valikko6(self):
        self.manager.current = "luku"

class Subosio(Screen):

    def alaosio(self):
        self.manager.current = "sub"
    
    def back(self):
        self.manager.current = "osiot"
    
    def yksnom(self):
        self.manager.current = 'yksmon'
    
    def akk(self):
        self.manager.current = 'akk'
    
    def gen(self):
        self.manager.current = 'gen'
    
    def dat(self):
        self.manager.current = 'dat'
    
    def ins(self):
        self.manager.current = 'ins'
    
    def prep(self):
        self.manager.current = 'prep'

class Pronominit(Screen):

    def back(self):
        self.manager.current = "osiot"
    
    def perpro(self):
        self.manager.current = 'perpro'

    def dempro(self):
        self.manager.current = 'dempro'
    
    def kyspro(self):
        self.manager.current = 'kyspro'

    def kielpro(self):
        self.manager.current = 'kielpro'
    
    def indpro(self):
        self.manager.current = 'indpro'

    def relpro(self):
        self.manager.current = 'relpro'

class Adjektiivit(Screen):

    def back(self):
        self.manager.current = "osiot"
    
    def komp(self):
        self.manager.current = 'komp'
    
    def super(self):
        self.manager.current = 'super'
    
    def nomadj(self):
        self.manager.current = 'nomadj'
    
    def akkadj(self):
        self.manager.current = 'akkadj'
    
    def genadj(self):
        self.manager.current = 'genadj'
    
    def datadj(self):
        self.manager.current = 'datadj'
    
    def insadj(self):
        self.manager.current = 'insadj'
    
    def prepadj(self):
        self.manager.current = 'prepadj'

    def lyhyet(self):
        self.manager.current = 'lyhyet'

class Verbiosio(Screen):

    def back(self):
        self.manager.current = "osiot"
    
    def asp(self):
        self.manager.current = 'asp'
    
    def per(self):
        self.manager.current = 'per'
    
    def prees(self):
        self.manager.current = 'prees'
    
    def pret(self):
        self.manager.current = 'pret'
    
    def fut(self):
        self.manager.current = 'fut'

    def inf(self):
        self.manager.current = 'inf'
    
    def imp(self):
        self.manager.current = 'imp'

    def kond(self):
        self.manager.current = 'kond'
    
    def sja(self):
        self.manager.current = 'sja'
    
    def byt(self):
        self.manager.current = 'byt'
    
    def liike(self):
        self.manager.current = 'liike'
    
    def ger(self):
        self.manager.current = 'ger'
    
    def part(self):
        self.manager.current = 'part'

    def pas(self):
        self.manager.current = 'pas'

class Pronominit(Screen):

    def back(self):
        self.manager.current = "osiot"

class Lukusanat(Screen):

    def back(self):
        self.manager.current = "osiot"
    
    def perus(self):
        self.manager.current = "perus"
    
    def kol(self):
        self.manager.current = "kol"
    
    def jarj(self):
        self.manager.current = "jarj"

class Yksmon(Screen):

    def valikko(self):
        self.manager.current = "subosio"  
    
    def nomi(self):
        self.manager.current = "nomi"

    def nommon(self):
        self.manager.current = "nommon"

    def osio(self):
        self.manager.current = 'sub'
    
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"
  
class Nominatiivi(Screen):
    
    def kysy(self):
        with open('kielioppi/nomkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/nomkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkinom.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_nom.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_nom.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class NominatiiviMON(Screen):
    
    def kysy(self):
        with open('kielioppi/nommonkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/nommonkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkinommon.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_nomnom.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_nom.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Akkusatiivi(Screen):
    
    def kysy(self):
        with open('kielioppi/akkkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/akkkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/akkvinkki.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_akk.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_akk.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Genetiivi(Screen):
    
    def kysy(self):
        with open('kielioppi/genkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/genkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/genvinkki.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_gen.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_gen.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Datiivi(Screen):
    
    def kysy(self):
        with open('kielioppi/datkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/datkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/datvinkki.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_dat.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_dat.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Instrumentaali(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Prepositionaali(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "subosio"

class Komparatiivi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class Superlatiivi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class NominatiiviADJ(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class AkkusatiiviADJ(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class GenetiiviADJ(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class DatiiviADJ(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class InstrumentaaliADJ(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class PrepositionaaliADJ(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class Lyhyet(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "adjosio"

class Aspekti(Screen):
    
    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Persoonamuodot(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Preesens(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Preteriti(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Futuuri(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Infinitiivi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Imperatiivi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Konditionaali(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Sjaverbit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Byt(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Liikeverbit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Gerundi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Partisiippi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Passiivi(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "verbiosio"

class Persoonapronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Demonstratiivipronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Kysymyspronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Indefiniittipronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Kieltopronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Relatiivipronominit(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "pronosio"

class Perusluvut(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "luku"

class Kollektiiviluvut(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "luku"

class Jarjestysluvut(Screen):

    def kysy(self):
        with open('kielioppi/subskys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kys.text = random.choice(kysymykset)

    def clear(self):
        self.ids.teksti.text = ''

    def vastaa(self,sub,joo):
        with open('kielioppi/subkys.json','r',encoding='utf8') as file:
            substantiivi = json.load(file)
        with open('kielioppi/vinkkisub.json','r',encoding='utf8') as file:
            vinkki = json.load(file)
        joo += 1 
        sub = sub.lower()
        oik = 0
        if sub in substantiivi:
            self.ids.edsub.value = joo
            self.ids.teksti.text = 'Oikein!'
            oik += 1
        elif sub in vinkki:
            self.ids.teksti.text = vinkki[sub]['vinkki']
        else:
            self.ids.teksti.text = 'Virhe!'

        with open('kielioppi/oikein_sub.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))

    def keepcountsub(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_sub.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatsub.text = str(len(oikein))
    
    def back(self):
        self.manager.current = "luku"

class Kyrilliset(Screen):
    def osio(self):
        self.manager.current = 'kyr'
    
    def kysykyr(self):
        with open('kielioppi/kyrkys.txt','r',encoding='utf8') as file:
            kysymykset = file.readlines()
        self.ids.kyskyr.text = random.choice(kysymykset)

    def clearkyr(self):
        self.ids.tekstikyr.text = ''

    def vastaakyr(self,kyr,joo):
        with open('kielioppi/kyrkys.json','r',encoding='utf8') as file:
            kyrilliset = json.load(file)
        joo += 1
        oik = 0
        kyr = kyr.lower()
        if kyr in kyrilliset:
            self.ids.tekstikyr.text = 'Oikein!'
            self.ids.edkyr.value = joo
            oik += 1
        else:
            self.ids.tekstikyr.text = 'Virhe!'
            
        with open('kielioppi/oikein_kyr.csv','a',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(str(oik))
    
    def back(self):
        self.manager.current = "osiot"

    def keepcountkyr(self,oikein):
        pisteet = pd.read_csv('kielioppi/oikein_kyr.csv')
        oikein = pisteet[pisteet['pisteet']==1]
        self.ids.oikeatkyr.text = str(len(oikein)) 

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()
