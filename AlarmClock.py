#                                        *Welcome to my Alarm Clock*
#Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
import winsound

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        # print("The Set Date is:",date)
        # print("Current time",now)
        if now == set_alarm_timer:
            print("TIME TO WAKE UP ...")
            winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()
clock.title("Alarm Clock")
clock.geometry("400x400")
clock.config(bg="skyblue")

time_format=Label(clock, text= "Enter time in 24 hour format !", fg="red",bg="black",font="Arial",width=40).place(x=20,y=170)
addTime = Label(clock,text = "Hour     Min     Sec",font=60).place(x = 160,y=30)
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=50)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

#Time required to set the alarm clock:
hourTime= Entry(clock,textvariable = hour,bg = "pink",width = 25).place(x=160,y=50)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 25).place(x=200,y=50)
secTime = Entry(clock,textvariable = sec,bg = "lightgreen",width = 25).place(x=250,y=50)

### wakeupEntry = Entry(clock,justify=CENTER,bd=2,width=20,font="Arial 25",fg="blue",bg="red").place(x=20,y=160)
#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =110,y=100)
quitB = Button(clock,text = "QUIT",fg="red",width = 10,command = quit).place(x =220,y=100)

clock.mainloop()

