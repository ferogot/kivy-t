

from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from test_dir.test1 import main
Config.set('graphics', 'width', '288')
Config.set('graphics', 'heaight', '512')


class MyApp(App):
    title = 'My app'
    root_widget = None

    def initialize_app(self):
        self.root_widget = Button(text=main())

    def build(self):
        self.initialize_app()
        return self.root_widget


MyApp().run()
