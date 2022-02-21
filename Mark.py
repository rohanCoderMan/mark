# importing libs
import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import pyautogui
import os
import pyjokes
from PyDictionary import PyDictionary as dicti
import datetime
from playsound import playsound as ps
#Blame rohan for any sus things....
import time as TiMeSus
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup as BS

# setting up voice engine
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',170)

#Function to say anything....
def Say(Text):
    print("     ")
    print(f'Mark X: {Text}')
    engine.say(text=Text)#Says the text
    engine.runAndWait()#Waits for code to end , or it will auto shutdown 
    print("     ")

#Listen function...
def Listen():
    # print('listening....')
    r= sr.Recognizer() # building recognizer
    with sr.Microphone(0) as source: # Microphone(0) means the deafault mic
        r.pause_threshold = 1
        audio = r.listen(source,0 ,5) # Giving mic as source , then 
        #Timeout as 0 , and time limit as 5
        #(so that mark dosent stop listening as soon as he starts to listen....)


    try:
        # print('recognizing....')
        query = r.recognize_google(audio,language='en-in') #sending audio file to google , google makes it text and saves the text in {query
        print(f'you: {query}')
    except Exception as Error:
        return ''
    query = str(query)
    return query.lower()


#All the tasks that mark can perform...just some tasks ok?
def MainTasks():
    Say('Mark is online!!')
    def Music():
        Say("what is the name of the music")
        musicName = Listen()
        Say(f'Playing {musicName} on youtube')
        pywhatkit.playonyt(musicName)
    def OpenApps(query):
        Say('ok sir...')
        query = query.replace("mark","")
        query = query.replace("open","")
        pyautogui.hotkey('ctrl', 'esc')
        pyautogui.write(query, interval = 0.2)
        pyautogui.hotkey('enter')
    def ChromeAuto():
        # pyautogui.hotkey('')
        Say('Started chrome automation')
        while True:
            comm = Listen()
            if('new window' in comm):
                pyautogui.hotkey('ctrl','n')
            elif('new tab' in comm):
                pyautogui.hotkey('ctrl','t')
            elif('reopen' in comm):
                pyautogui.hotkey('ctrl','shift','t')
            elif('devloper' in comm):
                pyautogui.hotkey('ctrl','shift','i')
            elif('full screen' in comm):
                pyautogui.press('f11')
            elif('close' in comm):
                pyautogui.hotkey('ctrl','w')
            elif('exit' in comm):
                Say('closing chrome automation')
                break
    def YoutubeAuto():
        # pyautogui.hotkey('')
        Say('Started youtube automation')
        while True:
            comm = Listen()
            if('play' in comm or 'pause' in comm):
                pyautogui.press('k')
            elif('mute' in comm or 'unmute' in comm):
                pyautogui.press('m')
            elif('fullscreen' in comm):
                pyautogui.press('f11')
            elif('exit' in comm):
                Say('closing youtube automation')
                break

            
    while True:
        query = Listen()
        
         #We have done that mark sleeps if there is sleep in query   
        if("sleep" in query):
            Say("Okay sir....")
            Say('Just say Wake up to wake me up')
            Say('Mark is offline')
            break
        elif("hello" in query):
            Say("Hello sir!")
        elif('youtube search' in query): #simple!
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("youtube","")
            query = query.replace("search","")
            Say(f"searching for{query}")
            url = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(url)
        elif('google search' in query):#simple!
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("google","")
            query = query.replace("search","")
            Say(f"searching for{query}")
            pywhatkit.search(query)
        elif('website' in query):#simple!
            Say("Ok sir launching...")
            query = query.replace("mark","")
            query = query.replace("website","")
            query = query.replace("open","")
            query = query.replace("of","")
            web = f"https://www.{query}.com"
            webbrowser.open(web)
        elif('music' in query):
            Music()#just play it on utube
        elif('wikipedia' in query):
            Say("Ok sir...")
            query = query.replace("mark","")
            query = query.replace("search","")
            query = query.replace("on","")
            query = query.replace("wikipedia","")
            query = query.replace("who is","")
            query = query.replace("about","")
            wiki = wikipedia.summary(query,2)
            Say(f'according to wikipidea:{wiki}')
        elif ('screenshot' in query):
            pyautogui.hotkey('win','shift','s')
        elif('open' in query):
            OpenApps(query)  
        elif('chrome automation' in query or 'chrome tools'in query):
            ChromeAuto()
        elif('youtube automation' in query or 'youtube tools'in query):
            YoutubeAuto()
        elif('joke' in query):
            get = pyjokes.get_joke()
            Say(get)
        #Sry, We couldn't get a module for maps
        elif('where am i'in query or 'maps'in query):
            webbrowser.open('https://www.google.com/maps/')
        #Dictionary module helped us A LOT
        elif('meaning' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('meaning','')
            query = query.replace('of','')

            result = dicti.meaning(query)

            Say(f'the meaning of {query} is {result}')
        elif('synonym' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('synonym','')
            query = query.replace('of','')

            result = dicti.synonym(query)
            Say(f'the synonym of {query} is {result}')
        elif('antonym' in query):
            query = query.replace('what','')
            query = query.replace('is','')
            query = query.replace('the','')
            query = query.replace('antonym','')
            query = query.replace('of','')

            result = dicti.synonym(query)
            Say(f'the antonym of {query} is {result}')
        #Chrome Automation, Sounds cool? It is cool too
        elif('new window' in query):
                pyautogui.hotkey('ctrl','n')
        elif('new tab' in query):
                pyautogui.hotkey('ctrl','t')
        elif('reopen' in query):
                pyautogui.hotkey('ctrl','shift','t')
        elif('devloper' in query):
                pyautogui.hotkey('ctrl','shift','i')
        elif('full screen' in query):
                pyautogui.press('f11')
        elif('close' in query):
                pyautogui.hotkey('ctrl','w')
        elif('play' in query or 'pause' in query):
                pyautogui.press('k')
        elif('mute' in query or 'unmute' in query):
                pyautogui.press('m')
        elif('alarm' in query):
            Say('enter the time (IN 24 hour)')
            time = input('enter the time: ')
        #The Alarm clock...All set up for you
            while True:
                timeAc = datetime.datetime.now()
                now = timeAc.strftime("%H:%M:%S")

                if now == time:
                    Say("alarm opening")
                    ps(".\\ringtone.mp3")
                elif now>time:
                    break
        #The date, time section
        elif('date'in query):
            today = datetime.date.today()
            day = today.strftime("%B %d, %Y")
            Say(f"Today's date: {day}")
        elif('time' in query):
            now = datetime.datetime.now()
            dt_string = now.strftime("%H:%M:%S")
            Say(f"the time is: {dt_string}")
             #This is the wikipedia integration
        elif('how to'in query):
            Say('Surfing the internet')
            op = query.replace('Mark','')
            op = query.replace('tell','')
            op = query.replace('me','')
            op = query.replace('how','')
            op = query.replace('to','')
            max_result = 1
            how_to_func = search_wikihow(op , max_result)
            assert len(how_to_func) == 1
            Say(how_to_func[0].summary)
        elif('what is'in query):
            Say('Surfing the internet')
            op = query.replace('Mark','')
            op = query.replace('tell','')
            op = query.replace('me','')
            op = query.replace('what is','')
            pywhatkit.search(op)
        elif('who is'in query):
            Say('Surfing the internet')
            op = query.replace('Mark','')
            op = query.replace('tell','')
            op = query.replace('me','')
            op = query.replace('who is','')
            pywhatkit.search(op) 
            #Yeah we *tell* them the temprature...pretty cool huh?
        elif('temperature' in query):
            search =  'temperature'
            url = f'https://www.google.com/search?q={search}'
            r = requests.get(url)
            data = BS(r.text , 'html.parser')
            temp = data.find('div',class_ = 'BNeawe').text
            Say(f'the temperature is {temp}')
            #Shutdown, restart, logout...Sleep next update
         elif('shutdown' in query):
            #take input from user to confirm shutdown or not
            Say('are you sure?')
            choice = input("Shutdown your computer? ( y or n ) : ") 
            if choice == "y" or choice == "Y":
                os.system("shutdown /s /t  3") # 1 is time that is for after what time we want to shutdown 
   
            else:
                Say('canceled')
        elif('restart' in query):
            #take input from user to confirm shutdown or not
            Say('are you sure?')
            choice = input("restart your computer? ( y or n ) : ") 
            if choice == "y" or choice == "Y":
                os.system("shutdown /r /t  3") # 1 is time that is for after what time we want to shutdown 
   
            else:
                Say('canceled')
        elif('logout' in query):
            os.system("shutdown /l /t  3")  
MainTasks()
#Yeah those were some tasks only and we plan to add more....
