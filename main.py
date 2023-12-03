from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout


from bs4 import BeautifulSoup
import requests

class MyApp(App):

    def build(self):
        al = AnchorLayout()
        bl = BoxLayout(orientation="vertical", size_hint=[.3, .3])

        self.t1 = TextInput()
        bl.add_widget(self.t1)
        bl.add_widget(Button(text = "Узнать курс!", on_press=self.change))


        al.add_widget(bl)
        return al
    
    def change(self, instance):
        instance.background_color = [0, 0, .7, 1]
        link = "https://finance.rambler.ru/calculators/converter/1-RUB-KGS/"
        start = requests.get(link).text

        block = BeautifulSoup(start, "lxml")

        info = block.find("div", class_ = "_2TC8G commercial-branding")
        info2 = info.find("div", class_ = "_10LUV")
        info3 = info2.find("div", class_ = "_1pfVA g2z3W")
        info4 = info3.find("div", class_ = "_2j-9_")
        info5 = info4.find("div", class_ = "_2TuTy")
        info6 = info5.find("div", class_ = "_19xHg")

        number = info6.find_all("span")[3].text
        self.t1.text = f"1 rub = {number}"

        instance.background_color = [0, 0, .3, 1]
        

if __name__ == "__main__":
    MyApp().run()