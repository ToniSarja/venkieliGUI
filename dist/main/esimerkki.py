from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
import json
import random
from kivy.uix.progressbar import ProgressBar
import csv
import pandas as pd

Builder.load_file('esimerkki2/esimerkki.kv')

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

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__=="__main__":
    MainApp().run()
