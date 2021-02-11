from json import dumps
from kivy import Config
from kivy.core import window
from kivy.network.urlrequest import UrlRequest
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.card import MDCard
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextField
from kivy.core.window import Window

Config.set('graphics', 'multisamples', '0')
Window.size = (600, 600)


class LoginScreen(MDScreen):
    def request(self, *args):
        email = self.input_email.text
        senha = self.input_senha.text

        def on_success(req, res):
            print(str(res))

        def on_error(*args):
            print(str(args))

        def on_redirect(*args):
            print(f'redirect: {str(args)}')

        self.req = UrlRequest("http://127.0.0.1:5000/",
                              on_success=on_success, on_error=on_error, verify=False, on_redirect=on_redirect, req_body=dumps({'email': email, 'senha': senha}), req_headers={'Content-Type': 'application/json'})

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.card = MDCard()
        self.card.text = "Valida"
        self.box = BoxLayout()
        self.box.orientation = 'vertical'
        self.card.add_widget(self.box)

        self.button_login = MDRaisedButton(text="Login")
        self.input_senha = MDTextField(password=True)
        self.button_login.bind(on_press=self.request)
        self.card.padding = "20dp"
        self.input_email = MDTextField()
        self.input_email.hint_text = "E-mail"
        self.input_senha.hint_text = "Senha"
        self.box.add_widget(self.input_email)
        self.box.add_widget(self.input_senha)
        self.box.add_widget(self.button_login)
        self.add_widget(self.card)


class Tela2(MDScreen):
    ...

    def __init__(self, **kwargs):
        super(Tela2, self).__init__(**kwargs)
        self.button_screen = MDRaisedButton(text="Login")
        self.ids['btn'] = self.button_screen
        self.add_widget(self.button_screen)


class MyApp(MDApp):
    ...

    def trocar_tela(self, *args):
        self.manager.current = "login_screen"

    def build(self):
        self.tela2 = Tela2()
        self.tela2.ids.btn.bind(on_press=self.trocar_tela)
        self.manager = ScreenManager()
        self.manager.add_widget(LoginScreen(name="login_screen"))
        self.manager.add_widget(self.tela2)
        self.theme_cls.primary_palette = "Teal"
        self.theme_cls.primary_hue = '700'
        return self.manager


MyApp().run()
