
import os
import sys
import time
from gtts import gTTS

# from chores import mytts
language = 'en'



def mytts(mytext, language):
    # language = 'en'
    ttsobj = gTTS(text=mytext, lang=language, slow=False)
    ttsobj.save("respond.mp3")
    os.system("mpg321 respond.mp3")
    os.system("rm respond.mp3")

time_measures = ["minutes", "hours", "seconds"]

def min_timer(minutes, reminder_name):
    sec = 0
    min = 0
    

    while True:
        sec += 1
        time.sleep(1)
        os.system("clear")
        
        print("seconds:"+str(sec))
        
        if sec == 60:
            min += 1
            print("minutes: "+str(min))
            sec = 0
        if min == int(minutes):
            if "null"  in reminder_name:
                mytts("your "+str(minutes)+" timer has ended.", "en")
                break
            else:
                mytts("Time to "+str(reminder_name), "en")
                break

    return

def hour_timer(hours, reminder_name):
    sec = 0
    min = 0
    hour = 0
    while True:
        sec += 1
        time.sleep(1)
        os.system("clear")
        
        print("seconds:"+str(sec))
        
        if sec == 60:
            min += 1
            print("minutes: "+str(min))
            sec = 0
        if min == 60:
            hour +=1
            print("hours: "+str(hour))
            min = 0
        if hour == hours:
            if "null"  in reminder_name:
                mytts("your "+str(minutes)+" timer has ended.", "en")
                break
            else:
                mytts("Time to "+str(reminder_name), "en")
                break

            
        

    return

def second_timer(seconds, reminder_name):
    print(seconds)
    sec = 0
    while True:
        sec += 1
        time.sleep(1)
        os.system("clear")
        
        print("seconds:"+str(sec))
        
        if sec == int(seconds):
            if "null"  in reminder_name:
                mytts("your "+str(seconds)+"second timer has ended.", "en")
                break
            else:
                mytts("Time to "+str(reminder_name), "en")
                break

    return


f = open("time.txt", "r")
data = f.read()
f.close()

def timer1():
    

    
    data_list = data.split(" ")

    start_name = data_list.index("to")
    end_name = data_list.index("in")

    reminder_name = data_list[3:-3]

    for measurement in time_measures:
        if data_list[-1] == measurement:
            time_frame = measurement
        
    amount = ""
    amount = str(data_list[-2])

    if measurement == "seconds":
        outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
        print(outputstr)
        mytts(outputstr, "en")
        second_timer(amount, reminder_name)
    elif measurement == "minutes":
        outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
        print(outputstr)
        mytts(outputstr, "en")
        min_timer(amount, reminder_name)
    elif measurement == "hours":
        outputstr = "I will remind you to "+str(reminder_name)+" in "+str(amount)+" "+time_frame
        print(outputstr)
        mytts(outputstr, "en")
        hour_timer(amount, reminder_name)
    else:
        mytts("Sorry, I dont recognize that", "en")

def timer2():
    data_list = data.split(" ")
    if data_list[-1] == time_measures[0]:
        mytts("setting a timer for "+data_list[-2]+" "+data_list[-1], "en")
        min_timer(int(data_list[-2]), "null")
    elif data_list[-1] == time_measures[1]:
        mytts("setting a timer for "+data_list[-2]+" "+data_list[-1], "en")
        hour_timer(int(data_list[-2]), "null")
    elif data_list[-1] == time_measures[2]:
        mytts("setting a timer for "+data_list[-2]+" "+data_list[-1], "en")
        second_timer(int(data_list[-2]), "null")
    



if "remind me" in data:
    timer1()
if "set a timer" in data:
    timer2()


            


#example string -- "remind me to x in y minutes" or "set a timer for x (time)"


        



