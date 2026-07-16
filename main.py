from tkinter import *
from tkinter import ttk
import requests
from datetime import datetime
import pandas as pd


# OpenWeather API Key


with open("Weather_API.txt") as f:
   content = f.read()

# ---------------- WEATHER FUNCTION ----------------

def data_get():

    city = city_name.get()

    if city == "":
        W_value.config(text="Select City")
        return

    try:

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={content}&units=metric"

        data = requests.get(url).json()


        W_value.config(
            text=data["weather"][0]["main"]
        )


        desc_value.config(
            text=data["weather"][0]["description"].title()
        )


        temp_value.config(
            text=str(data["main"]["temp"])+" °C"
        )


        pressure_value.config(
            text=str(data["main"]["pressure"])+" hPa"
        )


    except:

        W_value.config(text="Error")
        desc_value.config(text="City Not Found")



# ---------------- LIVE TIME ----------------

def show_time():

    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%d-%m-%Y")


    time_value.config(
        text=current_time+"\n"+current_date
    )


    time_value.after(
        1000,
        show_time
    )



# ---------------- WINDOW ----------------

win = Tk()

win.title("WeatherWise")

win.geometry("700x550")

win.config(
    bg="#111827"
)



# ---------------- TITLE ----------------

title = Label(
    win,
    text="🌤 WeatherWise",
    font=("Helvetica",42,"bold"),
    bg="#111827",
    fg="#38BDF8"
)


title.place(
    x=100,
    y=10,
    width=500,
    height=70
)



# ---------------- CITY DATABASE ----------------

indian_cities = [

"Agartala",
"Agra",
"Ahmedabad",
"Aizawl",
"Ajmer",
"Alappuzha",
"Aligarh",
"Allahabad",
"Amaravati",
"Amritsar",
"Anantapur",
"Arunachal Pradesh",

"Aurangabad",

"Bareilly",
"Ballari",
"Bathinda",
"Belagavi",
"Belgaum",
"Bhagalpur",
"Bhilai",
"Bhavnagar",
"Bhimpur",
"Bhivandi",
"Bilaspur",
"Bikaner",
"Bokaro",
"Bengaluru",
"Bhopal",
"Bhubaneswar",

"Chandigarh",
"Chennai",
"Chittoor",
"Coimbatore",
"Cuttack",

"Darbhanga",
"Davanagere",
"Dehradun",
"Delhi",
"Dimapur",
"Dibrugarh",
"Dhanbad",
"Dharamshala",
"Durgapur",

"Eluru",

"Faridabad",

"Gandhinagar",
"Gangtok",
"Gaya",
"Ghaziabad",
"Gorakhpur",
"Greater Noida",
"Guntur",
"Gurugram",
"Guwahati",
"Gwalior",

"Haridwar",
"Hisar",
"Howrah",
"Hubli",
"Hyderabad",

"Imphal",
"Indore",
"Itanagar",

"Jabalpur",
"Jaipur",
"Jaisalmer",
"Jalandhar",
"Jammu",
"Jamnagar",
"Jamshedpur",
"Jhansi",
"Jodhpur",

"Kakinada",
"Kalaburagi",
"Kanpur",
"Karimnagar",
"Karnal",
"Kochi",
"Kohima",
"Kolkata",
"Kollam",
"Kota",
"Kozhikode",
"Kurnool",

"Leh",
"Lucknow",
"Ludhiana",

"Madurai",
"Mangalore",
"Margao",
"Mathura",
"Meerut",
"Moradabad",
"Mumbai",
"Muzaffarpur",
"Mysuru",

"Nagpur",
"Nainital",
"Nashik",
"Navi Mumbai",
"Nellore",
"Noida",
"New Delhi",
"Nizamabad",

"Panaji",
"Panipat",
"Patiala",
"Patna",
"Puducherry",
"Pune",
"Puri",
"Purnia",

"Raipur",
"Rajahmundry",
"Rajkot",
"Ranchi",
"Rewa",
"Rishikesh",
"Rohtak",
"Rourkela",

"Salem",
"Sambalpur",
"Shillong",
"Shimla",
"Silchar",
"Siliguri",
"Solan",
"Sonipat",
"Srinagar",
"Surat",

"Thane",
"Thanjavur",
"Tezpur",
"Thiruvananthapuram",
"Thrissur",
"Tiruchirappalli",
"Tirupati",
"Tirunelveli",
"Tiruppur",
"Tawang",
"Tumakuru",

"Udaipur",
"Ujjain",

"Vadodara",
"Varanasi",
"Vasco da Gama",
"Vellore",
"Vijayawada",
"Visakhapatnam",
"Vizianagaram",

"Warangal"

]




city_name = StringVar()


# Combobox Styling

style = ttk.Style()

style.configure(
    "TCombobox",
    padding=5
)



city_box = ttk.Combobox(
    win,
    values=indian_cities,
    textvariable=city_name,
    font=("Helvetica",25),
    justify="center"
)


city_box.place(
    x=130,
    y=95,
    width=440,
    height=45
)



# ---------------- BUTTON ----------------

button = Button(
    win,
    text="Get Weather ☁",
    font=("Helvetica",16,"bold"),
    bg="#38BDF8",
    fg="black",
    relief="flat",
    command=data_get
)


button.place(
    x=250,
    y=150,
    width=200,
    height=40
)



# ---------------- WEATHER DASHBOARD CARD ----------------

card = Frame(
    win,
    bg="#1E293B"
)

card.place(
    x=70,
    y=220,
    width=560,
    height=260
)



# ---------------- LABEL FUNCTION ----------------

def create_label(text, x, y):

    label = Label(
        card,
        text=text,
        font=("Helvetica",18,"bold"),
        bg="#1E293B",
        fg="white"
    )

    label.place(
        x=x,
        y=y,
        width=220,
        height=40
    )

    return label



def create_value(x,y):

    label = Label(
        card,
        text="--",
        font=("Helvetica",18,"bold"),
        bg="#1E293B",
        fg="#38BDF8"
    )

    label.place(
        x=x,
        y=y,
        width=220,
        height=40
    )

    return label



# ---------------- WEATHER INFORMATION ----------------


# Weather

create_label(
    "🌥 Weather",
    20,
    20
)

W_value = create_value(
    300,
    20
)



# Description

create_label(
    "🌫 Description",
    20,
    70
)

desc_value = create_value(
    300,
    70
)



# Temperature

create_label(
    "🌡 Temperature",
    20,
    120
)

temp_value = create_value(
    300,
    120
)



# Pressure

create_label(
    "🔽 Pressure",
    20,
    170
)

pressure_value = create_value(
    300,
    170
)



# Time

create_label(
    "⏰ Time",
    20,
    220
)

time_value = Label(
    card,
    text="--",
    font=("Helvetica",16,"bold"),
    bg="#1E293B",
    fg="#38BDF8"
)

time_value.place(
    x=300,
    y=215,
    width=220,
    height=50
)



# ---------------- START CLOCK ----------------

show_time()



# ---------------- RUN APPLICATION ----------------

win.mainloop()
