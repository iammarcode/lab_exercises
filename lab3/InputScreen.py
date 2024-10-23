from kivy.uix.screenmanager import Screen

'''
To access the global values, you can simply import appData from Global.
- add or replace a global value: appData.abc = 123
- get an existing global value: v = appData.abc
'''
from Global import appData

class InputScreen(Screen):
    def button_click(self):
        username = self.ids.txt_username.text
        password = self.ids.txt_password.text
        print(f'{appData.topic}: {username}/{password}.')

    def clear(self):
        username = self.ids.txt_fullname.text
        password = self.ids.txt_email.text
        print(f'{appData.topic}: {username}/{password}.')
