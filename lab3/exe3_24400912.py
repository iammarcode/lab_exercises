from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.utils import platform
from kivy.app import Builder

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

class InputScreen(Screen):
    def clear(self):
        self.ids.txt_fullname.text = ''
        self.ids.txt_email.text = ''
        self.ids.txt_password.text = ''
        self.ids.txt_reenter_password.text = ''
        self.ids.txt_phone_number.text = ''

    def register(self):
        fullname = self.ids.txt_fullname.text
        email = self.ids.txt_email.text
        password = self.ids.txt_password.text
        reenterPassword = self.ids.txt_reenter_password.text
        phone = self.ids.txt_phone_number.text

        if any(not field.strip() for field in [fullname, email, password, reenterPassword, phone]):
            self.show_dialog("One or more fields are empty.")
        if password != reenterPassword:
            self.show_dialog("The Password and re-enter password are different")
    
        print(f'You inputted: {fullname}/{email}/{password}/{reenterPassword}/{phone}.')

    def cancel(self):
        self.clear()
        print("CANCEL")

    
    def show_dialog(self, text):
        dialog = MDDialog(
            title = 'Dialog',
            text = text,
            buttons = [
                MDRaisedButton(
                    text = 'Close',
                    on_press = lambda x: dialog.dismiss()
                ),
            ]
        )
        dialog.open()


if platform in ('win', 'macosx'):
    Window.size = (400, 400)

class MyApp(MDApp):
    screenmanager = None

    def build(self):
        self.title = 'Lab3 exercise'
        Builder.load_file('exe3_24400912.kv')

        self.screenmanager = ScreenManager()
        self.screenmanager.add_widget(InputScreen(name='InputScreen'))

        return self.screenmanager

MyApp().run()