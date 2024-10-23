### the following three lines are used for SSL problem on some computers.
### do NOT forget to add the following three lines to your code if you want to download something from the Internet
import certifi
import os
os.environ['SSL_CERT_FILE'] = certifi.where()

from kivy.core.window import Window
from kivy.utils import platform
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivy.app import Builder

from Global import appData

from InputScreen import InputScreen

### Set window size if the app runs on Windows or MacOS
if platform in ('win', 'macosx'):
    Window.size = (400, 600)

class MyApp(MDApp):

    ### The app starts with a screen. The screen defination is loaded from the KV file
    def build(self):
        self.title = 'Example'
        Builder.load_file('InputScreen.kv')

        screenmanager = ScreenManager()
        screenmanager.add_widget(InputScreen(name='InputScreen'))

        return screenmanager

### appData is a global name defined in Global.py
### Now appData.app refers to the app
### We can add anything to appData and get them back in different py files
appData.topic = 'Lab3 execises: '
appData.app = MyApp()
appData.app.run()
