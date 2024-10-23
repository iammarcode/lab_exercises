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
        username = self.ids.txt_fullname.text
        password = self.ids.txt_email.text
        print(f'{appData.topic}: {username}/{password}.')

    def register(self):
        fullname = self.ids.txt_fullname.text
        email = self.ids.txt_email.text
        password = self.ids.txt_password.text
        reEnterPassword = self.ids.txt_re_enter_password.text
        phone = self.ids.txt_phone_number.text

        if any(not field.strip() for field in [fullname, email, password, reEnterPassword, phone]):
            self.show_dialog("One or more fields are empty.")
        elif password != reEnterPassword: 
            self.show_dialog("Password and Re-enter Password not match")
        else:
            print(f'{appData.topic}fullname:{fullname}, email:{email}, password: {password}, re-enter password: {reEnterPassword}, phone: {phone}.')

    def cancel(self):
        username = self.ids.txt_fullname.text
        password = self.ids.txt_email.text
        print(f'{appData.topic}: {username}/{password}.')

    
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


# class ShowDialogScreen(Screen):
#     ### This method will be invoked when the user clicks the "Click Me" button
#     def show_dialog(self, text):
#         dialog = MDDialog(
#             title = 'Dialog',
#             text = text,
#             buttons = [
#                 MDRaisedButton(
#                     text = 'Close',
#                     on_press = lambda x: dialog.dismiss()
#                 ),
#             ]
#         )
#         dialog.open()
