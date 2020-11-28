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

    """ This function is called when the user press the button.
        The function checks the user's input and calls to the backend function ______-
        which returns the results according to the input"""
    def btn(self):
        if(self.time.text=="" or self.location.text=="" or self.reco.text==""):
            self.pop_results("Error", "Please fill in all the text boxes")
            self.location.text = ""
            self.time.text = ""
            self.reco.text = ""
        elif (not all(x.isalpha() or x.isspace() for x in self.location.text)):
            self.pop_results("Error", "Location must contain only letters")
            self.location.text = ""
            self.time.text = ""
            self.reco.text = ""
        elif (not self.time.text.isdecimal()):
            self.pop_results("Error", "Time must contain only numbers")
            self.location.text = ""
            self.time.text = ""
            self.reco.text = ""
        elif (not self.reco.text.isdecimal()):
            self.pop_results("Error", "Numbers of recommendation must contain only numbers")
        elif (int(self.time.text)<1):
            self.pop_results("Error", "The time must larger than 0")
            self.location.text = ""
            self.time.text = ""
            self.reco.text = ""
        elif (int(self.reco.text) < 1):
            self.pop_results("Error", "The Numbers of recommendation must larger than 0")
            self.location.text = ""
            self.time.text = ""
            self.reco.text = ""
        else:
            results= database.find_recommends(self.location.text,self.time.text,self.reco.text)
            results="results" #need to change
            self.pop_results('Recommended Locations',results)
            self.location.text=""
            self.time.text=""
            self.reco.text=""
            # self.database.view()

    def pop_results(self,title,results):
        pop = Popup(title='Recommended Locations',
                    content=Label(text=results),
                    size_hint=(None, None), size=(400, 400))

        pop.open()


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    database=mybackend.Database()
    MyApp().run()
