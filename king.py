import kivy
kivy.require('2.0.0') 
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout  
from kivy.uix.progressbar import ProgressBar
from kivy.uix.popup import Popup 
from kivy.config import Config
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window

Config.set('graphics','width',40)
Config.set('graphics','height',400)



class mygrid(GridLayout):

    def presionarBoton(self,evento):
        pedido=self.pedido.text
        nombre=self.nombre.text
        telefono=self.telefono.text
       
        self.pedido.text=''
        self.nombre.text=''
        self.telefono.text=''

        popup = Popup(title ='Demo Popup')   
        popup.open()    
 


    def __init__(self,**kwargs):
        super(mygrid,self).__init__(**kwargs)

        self.cols=2
        self.cuadro1=GridLayout()
        self.cuadro1.cols=2



        self.cuadro1.add_widget(Label(text="pedido",font_size=26))
        self.pedido=TextInput(multiline=1,font_size=26)
        self.cuadro1.add_widget(self.pedido)

        self.cuadro1.add_widget(Label(text="nombre",font_size=26))
        self.nombre=TextInput(multiline=0,font_size=26)
        self.cuadro1.add_widget(self.nombre)

        self.cuadro1.add_widget(Label(text="telefono",font_size=26))
        self.telefono=TextInput(multiline=0,font_size=26)
        self.cuadro1.add_widget(self.telefono) 

        self.botonGuardar=Button(text='Agregar', font_size=26, size_hint=(1,.5),background_color=(1,0,0))
        self.botonGuardar.bind(on_press=self.presionarBoton)
        self.cuadro1.add_widget(self.botonGuardar)

        #self.cuadro1.add_widget(ScrollView(size_hint=(1, None), size=(Window.width, Window.height)))

        #text_size=(800,600),valign='top',halign='left'
        self.add_widget(self.cuadro1)


        self.info=TextInput(text="aqui va la info",multiline=1,font_size=20,scroll_y=1,disabled=1)
        self.add_widget(self.info) 



        
        

        # self.pb = ProgressBar(max = 100)
        # self.add_widget(self.pb)

        




class MyApp(App):
    title="king"

    def build(self):
        return mygrid()

if __name__ == '__main__':
    MyApp().run()



