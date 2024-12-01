from kivy.app import App
from kivy.base import runTouchApp
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text:'Street Fighter'
            on_press:root.manager.current='Boton1'
        Button:
            text:'Mortal Kombat'
            on_press:root.manager.current='Boton2'
        Button:
            text:'King of Fighters'
            on_press:root.manager.current='Boton3'
<Boton1>:
    BoxLayout:
        Image:
            source:'stf.png'
            allow_stretch:False
            keep_ratio:False
        Button:
            text:"Back to menu"  
            on_press:root.manager.current='menu'                        
<Boton2>:
    BoxLayout:
        Image:
            source:'mk.png'
            allow_stretch:False
            keep_ratio:False
        Button:
            text:"Back to menu"
            on_press:root.manager.current='menu'

<Boton3>:
    BoxLayout:
        Image:
            source:'kof.png'
            allow_stretch:False
            keep_ratio:False
        Button:
            text:'Back to menu'
            on_press:root.manager.current='menu'
""")
class MenuScreen(Screen):
    pass
class Boton1(Screen):
    pass
class Boton2(Screen):
    pass
class Boton3(Screen):
    pass
sm= ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(Boton1(name='Boton1'))
sm.add_widget(Boton2(name='Boton2'))
sm.add_widget(Boton3(name='Boton3'))
class TestApp(App):
    def build(self):
        return sm 
if __name__=='__main__':
    TestApp().run()