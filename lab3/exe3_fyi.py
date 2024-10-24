from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager

from kivymd.app import MDApp
from kivy.app import Builder


class InputScreen(Screen):
    dialog = None

    def clear(self):
        # Clear all text fields
        self.ids.txt_fullname.text = ''
        self.ids.txt_emailaddress.text = ''
        self.ids.txt_password.text = ''
        self.ids.txt_repassword.text = ''
        self.ids.txt_phonenumber.text = ''

    def register(self):
        fullname = self.ids.txt_fullname.text
        email = self.ids.txt_emailaddress.text
        password = self.ids.txt_password.text
        repassword = self.ids.txt_repassword.text
        phone = self.ids.txt_phonenumber.text

        # Validate input
        if not all([fullname, email, password, repassword, phone]):
            self.show_dialog("Error", "All fields must be filled out.")
            return
        
        if password != repassword:
            self.show_dialog("Error", "Passwords do not match.")
            return

        # Print the values to the terminal
        print(f"Full Name: {fullname}")
        print(f"Email: {email}")
        print(f"Password: {password}")
        print(f"Phone Number: {phone}")
        
    def cancel(self):
        # Print "CANCEL" and clear all text fields
        print("CANCEL")
        self.clear()



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