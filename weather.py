from tkinter import *
from tkinter import ttk
import requests

# data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+"delhi"+"&appid=").json()
# print( data )

# {'coord': {'lon': 77.2167, 'lat': 28.6667},
# 'weather': [{'id': 701, 'main': 'Mist', 'description': 'mist', 'icon': '50d'}],
# 'base': 'stations',
# 'main': {'temp': 303.2, 'feels_like': 310.2, 'temp_min': 303.2, 'temp_max': 303.2, 'pressure': 1004, 'humidity': 89, 'sea_level': 1004, 'grnd_level': 980},
# 'visibility': 2800, 'wind': {'speed': 4.12, 'deg': 80}, 'clouds': {'all': 75}, 'dt': 1723526333, 'sys': {'type': 1, 'id': 9165, 'country': 'IN', 'sunrise': 1723508362, 'sunset': 1723555967},
# 'timezone': 19800, 'id': 1273294, 'name': 'Delhi', 'cod': 200}

def get_city():
    city_name1= city_name.get()
    data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name1+"&appid=").json()
    print( data )
    weather_label2.config(text = (int(data['main']['temp'])-273.15))
    rain_label2.config(text = str(data['main']['humidity'])+"%")
    
    



win = Tk()
win.title("Weather App")
win.config(bg = "red")
win.geometry("500x500")
name_label = Label(win , text = "Weather app",font = ("Times New Roman",35,"bold"))
name_label.place(x= 25 , y= 50, height= 50 , width = 400 )
city_name = StringVar()
states = ["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]
com = ttk.Combobox( win , text = "Weather app", values = states, font = ("Times New Roman",15,"bold"), textvariable= city_name)
com.place(x= 25 , y= 120, height= 50 , width = 400)
done_button = Button(win , text = "Calculate",font = ("Times New Roman",15,"bold") ,command=get_city)
done_button.place(x= 150 , y= 190, height= 50 , width = 100)

weather_label = Label(win , text = "Temperature",font = ("Times New Roman",15,"bold"))
weather_label.place(x= 25 , y= 260, height= 30 , width = 150 )
weather_label2 = Label(win , text = "",font = ("Times New Roman",15,"bold"))
weather_label2.place(x= 200 , y= 260, height= 30 , width = 200 )

rain_label = Label(win , text = "Rain",font = ("Times New Roman",15,"bold"))
rain_label.place(x= 25 , y= 300, height= 30 , width = 150 )
rain_label2 = Label(win , text = "",font = ("Times New Roman",15,"bold"))
rain_label2.place(x= 200 , y= 300, height= 30 , width = 200 )




win.mainloop()
    