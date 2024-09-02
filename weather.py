from tkinter import *
from tkinter import ttk, messagebox
from geopy.geocoders import Nominatim
from datetime import datetime
import requests
import pytz


root = Tk()
root.title('Weather App')
root.geometry('900x500+300+200')
root.resizable(False, False)

root.mainloop()