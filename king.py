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
from kivy.uix.floatlayout import FloatLayout
import time
import pymongo


cliente = pymongo.MongoClient("mongodb+srv://admin:33sqQMSJRct-Erz@cluster0.nfxzs.mongodb.net/King?retryWrites=true&w=majority")
db = cliente.King
db=cliente['King']
cicloBeneficio=2

class mygrid(GridLayout):

    def presionarBoton(self,evento):
        global cicloBeneficio
        Vpedido=self.pedido.text
        Vtelefono=self.telefono.text
        Vnombre=self.nombre.text
        Vdireccion=self.direccion.text
        if Vpedido=='' or Vtelefono=='' or Vnombre=='' or Vdireccion=='':
            print("digite vcalores")
        else:
            self.pedido.text=''
            self.telefono.text=''
            self.nombre.text=''
            self.direccion.text=''
            Numeropedidos=0
            pedidos=db['pedidos']
            pedidos=pedidos.find()
            for docu in pedidos:
                Numeropedidos+=int(docu['contador'])
            fecha=time.strftime("%H:%M  %e/%m/%Y")
            self.info.text+="#   "+str(Numeropedidos+1)+"\n"+"-   "+Vpedido+"\n"+"-   "+Vtelefono+"\n"+"-   "+Vnombre+"\n"+"-   "+Vdireccion+"\n"+"-   "+fecha+"\n_______________________________________\n"
            pedidos = db['pedidos']
            buscar=pedidos.find_one({
                'telefono':Vtelefono
                })
            if buscar==None:
                contador=1
                pedidos.insert_one({
                'pedido':Vpedido,           
                'telefono':Vtelefono,
                'nombre':Vnombre,
                'direccion':Vdireccion,
                'fecha':fecha,
                'contador':contador,
                })
            else:
                contador=str(int(buscar['contador'])+1)
                pedidos.update_one({
                'telefono':Vtelefono
                },{
                    "$set":{
                        'pedido':Vpedido,
                        'telefono':Vtelefono,
                        'nombre':Vnombre,
                        'direccion':Vdireccion,
                        'fecha':fecha,
                        'contador':contador,
                    }
                })
            if int(contador)%cicloBeneficio==0:
                print("ya ha pedido "+contador+" veces")


        #popup = Popup(title ='Demo Popup')   
        #popup.open()    

    def __init__(self,**kwargs):
        super(mygrid,self).__init__(**kwargs)

        self.root=FloatLayout()

        self.root.add_widget(Label(text="Pedido :",font_size=26,size_hint=(None,None),pos_hint={'x':.1, 'y':5},halign='right'))
        self.pedido=TextInput(multiline=1,font_size=18,size_hint=(None,None),pos_hint={'x':1.2, 'y':5},width=300)
        self.root.add_widget(self.pedido)
        
        self.root.add_widget(Label(text="Telefono :",font_size=26,size_hint=(None,None),pos_hint={'x':.1, 'y':4.3},halign='right',height=50))
        self.telefono=TextInput(multiline=0,font_size=26,size_hint=(None,None),pos_hint={'x':1.2, 'y':4.3},width=300,height=50)
        self.root.add_widget(self.telefono)

        self.root.add_widget(Label(text="Nombre :",font_size=26,size_hint=(None,None),pos_hint={'x':.1, 'y':3.6},halign='right',height=50))
        self.nombre=TextInput(multiline=0,font_size=26,size_hint=(None,None),pos_hint={'x':1.2, 'y':3.6},width=300,height=50)
        self.root.add_widget(self.nombre)

        self.root.add_widget(Label(text="Direccion :",font_size=24,size_hint=(None,None),pos_hint={'x':.1, 'y':2.9},halign='right',height=50))
        self.direccion=TextInput(multiline=0,font_size=26,size_hint=(None,None),pos_hint={'x':1.2, 'y':2.9},width=300,height=50)
        self.root.add_widget(self.direccion)

        self.botonGuardar=Button(text='Agregar', font_size=26,background_color=(1,0,0),size_hint=(None,None),pos_hint={'x':1.75, 'y':2.2},halign='right',height=50)
        self.botonGuardar.bind(on_press=self.presionarBoton)
        self.root.add_widget(self.botonGuardar)

        self.info=TextInput(multiline=1,font_size=16,scroll_y=1,disabled=1,size_hint=(None,None),pos_hint={'x':4.5, 'y':1},width=300,height=500)
        self.root.add_widget(self.info) 

        self.add_widget(self.root)




class MyApp(App):
    title="king"

    def build(self):
        return mygrid()
if __name__ == '__main__':
    MyApp().run()



