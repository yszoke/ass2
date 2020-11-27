import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
import mybackend

import mybackend as backend
class MyGrid(Widget):
    location = ObjectProperty(None)
    time = ObjectProperty(None)
    reco = ObjectProperty(None)
    def btn(self):
        # results= backend.calcResults(self.location.text,self.time.text,self.reco.text) add to backend
        results="results" #need to change
        self.pop_results(results)
        self.location.text=""
        self.time.text=""
        self.reco.text=""
        # self.database.view()

    def pop_results(self,results):
        pop = Popup(title='Recommended Locations',
                    content=Label(text=results),
                    size_hint=(None, None), size=(400, 400))

        pop.open()

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    # database=mybackend.database()
    MyApp().run()
