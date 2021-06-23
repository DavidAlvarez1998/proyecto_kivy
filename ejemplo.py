import kivy
kivy.require('2.0.0') 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button








def cuadro(**kwargs): 
    super(cuadro).__init__(**kwargs)
    cols=2 
    add_widget(Label(text="pedido"))
    pedido=TextInput(multiline=1)
    add_widget(pedido)
    add_widget(Label(text="nombre"))
    nombre=TextInput(multiline=0)
    add_widget(nombre)
    add_widget(Label(text="telefono"))
    telefono=TextInput(multiline=0)
    add_widget(telefono)

        #self.submit=Button





class MyApp(App):
    def build(self):
        return cuadro()

if __name__ == '__main__':
    MyApp().run()



