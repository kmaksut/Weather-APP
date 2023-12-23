from PIL import ImageTk
import customtkinter as ctk
from CTkToolTip import *
from datetime import datetime
from urllib.request import urlopen
from tksvg import SvgImage
import dotenv, os, re, requests

# get time
current = datetime.now()
# Default theme
ctk.set_appearance_mode("light")
# global vars
start_size:int = 250 
max_size:int = 300
city:str = ""
# Api Key
dotenv.load_dotenv()
api_key = os.environ.get("API_KEY")

# funcs
def ip_and_location(ip:bool=False, city:bool=False)->str: 
    try:
        response = requests.get("https://ipinfo.io")
        parse_json = response.json()
        if ip == True:
            return parse_json["ip"]
        if city == True:
            return parse_json["city"]
    except:
         return "bağlantı hatası"

def cLocat():
    global city, location
    city = location
    try:
        weather_api = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5&lang=tr"
        response = requests.get(weather_api)
        response_parse = response.json()
        day_label = [today_label, tomorrow_label, days_3_frame_label, days_4_frame_label, days_5_frame_label]
        degree_label = [today_degree,tomorrow_degree,days_3_degree,days_4_degree,days_5_degree]
        icon_label = [today_icon,tomorrow_icon,days_3_icon,days_4_icon,days_5_icon]
        status_label = [today_status,tomorrow_status,days_3_status,days_4_status,days_5_status]
        for index,value in enumerate(day_label):
            value.configure(text=response_parse['forecast']['forecastday'][index]['date']) 
        for index,value in enumerate(degree_label):
            value.configure(text=f"{response_parse['forecast']['forecastday'][index]['day']['avgtemp_c']}"u"\N{DEGREE SIGN}")
        for index,value in enumerate(icon_label):
            icon_open = urlopen(f"https:{response_parse['forecast']['forecastday'][index]['day']['condition']['icon']}")
            raw_data = icon_open.read()
            icon_open.close()
            _photo = ImageTk.PhotoImage(data=raw_data, size=100)
            value.configure(image=_photo)
        for index,value in enumerate(status_label):
            status_text = response_parse['forecast']['forecastday'][index]['day']['condition']['text']
            value.configure(text=response_parse['forecast']['forecastday'][index]['day']['condition']['text'])
            status_regex_1 = re.search("Bölgesel düzensiz yağmur yağışlı",status_text)
            status_regex_2 = re.search("Orta kuvvetli yağmurlu",status_text)
            status_regex_3 = re.search("Yoğun kar yağışlı",status_text)
            status_regex_4 = re.search("Orta kuvvetli veya yoğun ve sağnak şeklinde kar",status_text)
            status_regex_5 = re.search("Hafif dondurucu yağmurlu",status_text)
            status_regex_6 = re.search("Parçalı Bulutlu",status_text)
            status_regex_7 = re.search("Düzensiz orta kuvvetli karlı",status_text)
            status_regex_8 = re.search("Çok bulutlu",status_text)
            status_regex_9 = re.search("Şiddetli yağmurlu",status_text)
            if status_regex_1:
                value.configure(text="Hafif\nYağışlı")
            if status_regex_2:
                value.configure(text="Orta\nYağışlı")
            if status_regex_3:
                value.configure(text="Yoğun\nKarlı")
                value.place(x=44,y=60)
            if status_regex_4:
                value.configure(text="Karlı")
                value.place(x=49,y=60)
            if status_regex_5:
                value.configure(text="Soğuk\nYağmurlu")
                value.place(x=33,y=60)
            if status_regex_6:
                value.configure(text="Parçalı\nBulutlu")
            if status_regex_7:
                value.configure(text="Hafif\nKarlı")
                value.place(x=48,y=60)
            if status_regex_8:
                value.configure(text="Bulutlu")
            if status_regex_9:
                value.configure(text="Şiddetli\nYağmur")
                
    except Exception as err:
        print("Hata :",err)

def search_func(event):
    global city
    input = search_input_field.get().capitalize()
    city = input
    try:
        weather_api = f"http://api.weatherapi.com/v1/forecast.json?key={api_key}&q={city}&days=5&lang=tr"
        response = requests.get(weather_api)
        response_parse = response.json()
        if response.status_code == 200:
            current_location.configure(text=input, font=("arial",15))
            day_label = [today_label, tomorrow_label, days_3_frame_label, days_4_frame_label, days_5_frame_label]
            degree_label = [today_degree,tomorrow_degree,days_3_degree,days_4_degree,days_5_degree]
            icon_label = [today_icon,tomorrow_icon,days_3_icon,days_4_icon,days_5_icon]
            status_label = [today_status,tomorrow_status,days_3_status,days_4_status,days_5_status]
            for index,value in enumerate(day_label):
                value.configure(text=response_parse['forecast']['forecastday'][index]['date']) 
            for index,value in enumerate(degree_label):
                value.configure(text=f"{response_parse['forecast']['forecastday'][index]['day']['avgtemp_c']}"u"\N{DEGREE SIGN}")
            for index,value in enumerate(icon_label):
                icon_open = urlopen(f"https:{response_parse['forecast']['forecastday'][index]['day']['condition']['icon']}")
                raw_data = icon_open.read()
                icon_open.close()
                today_photo = ImageTk.PhotoImage(data=raw_data, size=100)
                value.configure(image=today_photo)
            for index,value in enumerate(status_label):
                value.configure(text=response_parse['forecast']['forecastday'][index]['day']['condition']['text'])
                status_text = response_parse['forecast']['forecastday'][index]['day']['condition']['text']
                print(response_parse['forecast']['forecastday'][index]['day']['condition']['text'])
                status_regex_1 = re.search("Bölgesel düzensiz yağmur yağışlı",status_text)
                status_regex_2 = re.search("Orta kuvvetli yağmurlu",status_text)
                status_regex_3 = re.search("Yoğun kar yağışlı",status_text)
                status_regex_4 = re.search("Orta kuvvetli veya yoğun ve sağnak şeklinde kar",status_text)
                status_regex_5 = re.search("Hafif dondurucu yağmurlu",status_text)
                status_regex_6 = re.search("Parçalı Bulutlu",status_text)
                status_regex_7 = re.search("Düzensiz orta kuvvetli karlı",status_text)
                status_regex_8 = re.search("Çok bulutlu",status_text)
                status_regex_9 = re.search("Şiddetli yağmurlu",status_text)
                status_regex_10 = re.search("Hafif çisenti",status_text)
                status_regex_11 = re.search("Düzensiz hafif karlı",status_text)                
                status_regex_12 = re.search("Hafif sağnak şeklinde kar",status_text)    
                status_regex_13 = re.search("Düzensiz yoğun kar yağışlı",status_text)    
                status_regex_14 = re.search("Orta kuvvetli karlı",status_text)                                                        
                if status_regex_1:
                    value.configure(text="Hafif\nYağışlı")
                if status_regex_2:
                    value.configure(text="Orta\nYağışlı")
                if status_regex_3:
                    value.configure(text="Yoğun\nKarlı")
                    value.place(x=44,y=60)
                if status_regex_4:
                    value.configure(text="Karlı")
                    value.place(x=49,y=60)
                if status_regex_5:
                    value.configure(text="Soğuk\nYağmurlu")
                    value.place(x=33,y=60)
                if status_regex_6:
                    value.configure(text="Parçalı\nBulutlu")
                if status_regex_7:
                    value.configure(text="Hafif\nKarlı")
                    value.place(x=48,y=60)
                if status_regex_8:
                    value.configure(text="Bulutlu")
                if status_regex_9:
                    value.configure(text="Şiddetli\nYağmur")
                if status_regex_10:
                    value.configure(text="Hafif\nÇisenti")
                if status_regex_11:
                    value.configure(text="Hafif\nKarlı")
                if status_regex_12:
                    value.configure(text="Karlı")
                if status_regex_13:
                    value.configure(text="Yoğun\nKarlı")
                if status_regex_14:
                    value.configure(text="Hafif\nKarlı")
        else:
            current_location.configure(text="Konumun", font=("Arial",15))
            cLocat()
    except Exception as err:
        print("Hata :", err)
    search_input_field.delete(0,ctk.END)

def set_theme():
    if theme_switcher.get() == "on":
        ctk.set_appearance_mode("dark")
        theme_switcher.configure(text="Dark")
    else:
        ctk.set_appearance_mode("light")
        theme_switcher.configure(text="Light")

# Main APP
app = ctk.CTk()
# App Configs
app.geometry("800x500+500+130")
app.title("Weather APP")
app.iconbitmap("img/app.ico")
app.resizable(False,False)
# İmages
svg_image = SvgImage(file="img/loc_1.svg")
# image = ctk.CTkImage(Image.open("img/path"),size=(200,200))
# Vars
switch_value = ctk.StringVar(value="off")
# Widgets
theme_switcher = ctk.CTkSwitch(app,text="Light", variable=switch_value, onvalue="on", offvalue="off", command=set_theme)
theme_switcher.place(x=690, y=20)
search_input_field = ctk.CTkEntry(app, width=280,height=35, corner_radius=10, placeholder_text="şehir ara ...")
search_input_field.place(x=250 , y=100)
current_location = ctk.CTkLabel(app, image=svg_image, text="Konumun", compound="left", font=("Arial",15), padx=10)
current_location.place(x=330, y=150)
# main
main_frame = ctk.CTkFrame(app, width=778, height=270, corner_radius=30)
main_frame.place(x=10, y=210) 
# today
today_frame = ctk.CTkFrame(main_frame, width=120, height=230, corner_radius=30)
today_frame.place(x=20, y=20)
today_label = ctk.CTkLabel(today_frame, text="", font=("Bahnschrift",16))
today_label.place(x=23, y=19)
today_status = ctk.CTkLabel(today_frame, text="", font=("Bahnschrift",13))
today_status.place(x=43, y=60)
today_icon = ctk.CTkLabel(today_frame, text="")
today_icon.place(x=35, y=100)
today_degree = ctk.CTkLabel(today_frame, text="", font=("Bahnschrift",20))
today_degree.place(x=47, y=180)
# tomorrow
tomorrow_frame = ctk.CTkFrame(main_frame,width=120, height=230, corner_radius=30)
tomorrow_frame.place(x=172, y=20)
tomorrow_label = ctk.CTkLabel(tomorrow_frame, text="", font=("Bahnschrift",16))
tomorrow_label.place(x=23, y=19)
tomorrow_status = ctk.CTkLabel(tomorrow_frame, text="", font=("Bahnschrift",13))
tomorrow_status.place(x=43, y=60)
tomorrow_icon = ctk.CTkLabel(tomorrow_frame, text="")
tomorrow_icon.place(x=36, y=100)
tomorrow_degree = ctk.CTkLabel(tomorrow_frame, text="", font=("Bahnscgrift",20))
tomorrow_degree.place(x=40, y=180)
# days_3
days_3_frame = ctk.CTkFrame(main_frame,width=120, height=230, corner_radius=30)
days_3_frame.place(x=325, y=20)
days_3_frame_label = ctk.CTkLabel(days_3_frame, text="", font=("Bahnschrift",16))
days_3_frame_label.place(x=22, y=19)
days_3_status = ctk.CTkLabel(days_3_frame, text="", font=("Bahnschrift",13))
days_3_status.place(x=43, y=60)
days_3_icon = ctk.CTkLabel(days_3_frame, text="")
days_3_icon.place(x=40, y=100)
days_3_degree = ctk.CTkLabel(days_3_frame, text="", font=("Bahnscgrift",20))
days_3_degree.place(x=40, y=180)
# days_4
days_4_frame = ctk.CTkFrame(main_frame,width=120, height=230, corner_radius=30)
days_4_frame.place(x=475, y=20)
days_4_frame_label = ctk.CTkLabel(days_4_frame, text="", font=("Bahnschrift",16))
days_4_frame_label.place(x=25, y=19)
days_4_status = ctk.CTkLabel(days_4_frame, text="", font=("Bahnschrift",13))
days_4_status.place(x=43, y=60)
days_4_icon = ctk.CTkLabel(days_4_frame, text="")
days_4_icon.place(x=37, y=100)
days_4_degree = ctk.CTkLabel(days_4_frame, text="", font=("Bahnscgrift",20))
days_4_degree.place(x=40, y=180)
# days_5
days_5_frame = ctk.CTkFrame(main_frame,width=120, height=230, corner_radius=30)
days_5_frame.place(x=630, y=20)
days_5_frame_label = ctk.CTkLabel(days_5_frame, text="", font=("Bahnschrift",16))
days_5_frame_label.place(x=22, y=19)
days_5_status = ctk.CTkLabel(days_5_frame, text="", font=("Bahnschrift",13))
days_5_status.place(x=43, y=60)
days_5_icon = ctk.CTkLabel(days_5_frame, text="")
days_5_icon.place(x=36, y=100)
days_5_degree = ctk.CTkLabel(days_5_frame, text="", font=("Bahnscgrift",20))
days_5_degree.place(x=40, y=180)

# ToolTips
theme_switcher_tooltip = CTkToolTip(theme_switcher, message="Tema Değiştir", delay=1.2, border_width=2, alpha=0.90)
# Binds
search_input_field.bind("<Return>", search_func)

if __name__ == "__main__":
    if current.hour >= 0 and current.hour <= 6 or current.hour >=19:
        theme_switcher.toggle()
        pass
    else:
        pass
    location = ip_and_location(city=True)
    cLocat()
    app.mainloop()