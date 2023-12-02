from tkinter import*
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

def getWeather():
    try:
        
        city=textfield.get()

        geolocator=Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)


        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        #weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=100a80210a09fc24793fb81920300490"

        json_data = requests.get(api).json()
        condition = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"]-273)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))

        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=description)
        p.config(text=pressure)


    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")
#search box
Search_image=PhotoImage(file="D:\Weather's icon\R2.png")
myimage=Label(image=Search_image)
myimage.place(x=1,y=10)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=140,y=70)
textfield.focus()

Search_icon=PhotoImage(file="D:\Weather's icon\pal.png")
myimage_icon=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=500,y=73)

#logo
Logo_image=PhotoImage(file="D:\Weather's icon\icons8-partly-cloudy-day-24.png")
logo=Label(image=Logo_image)
logo.place(x=250,y=200)

#Bottom box
Frame_image=PhotoImage(file="D:\Weather's icon\pranshuPNG32.png")
frame_myimage=Label(image=Frame_image)
frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=200)
clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=230)

#label
Label1=Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label1.place(x=200,y=350)

Label2=Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label2.place(x=300,y=350)

Label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label3.place(x=420,y=350)

Label4=Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
Label4.place(x=590,y=350)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=175)
c=Label(font=("arial",15,"bold"))
c.place(x=400,y=270)

w=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=210,y=400)
h=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=330,y=400)
d=Label(text=".......",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=430,y=400)
p=Label(text="....",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=630,y=400)
'''
frame=Frame(root,borderwidth=100,bg='cyan',relief=SUNKEN)
frame.pack(side=RIGHT,anchor='nw')
b1= Button(frame,fg='magenta',text='Go to calender')
b1.pack()'''

root.mainloop()
