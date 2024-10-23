from kivy.uix.screenmanager import Screen

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

'''
To access the global values, you can simply import appData from Global.
- add or replace a global value: appData.abc = 123
- get an existing global value: v = appData.abc
'''
from Global import appData

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
